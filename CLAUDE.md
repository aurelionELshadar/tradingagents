# CLAUDE.md

Guidance for Claude Code (and other AI assistants) working in this repository.

## What this is

TradingAgents is a multi-agent LLM financial trading/research framework built on
**LangGraph**. Specialized agents (analysts, researchers, risk debators, managers)
run as nodes in a compiled state graph, pull market/news/fundamentals data through
a vendor-abstracted dataflows layer, and converge on a trade decision. It ships as
both a Python package (`tradingagents`) and an interactive CLI (`tradingagents` /
`python -m cli.main`). Research tool, not investment advice — see README.

## Setup & commands

```bash
pip install -e ".[dev]"        # editable install with ruff/pytest
pytest -q                      # full test suite
pytest -q -m unit              # just unit-marked tests
ruff check .                   # lint (strict, whole repo — CI runs this exact command)
tradingagents                  # launch interactive CLI
python -m cli.main             # same, run from source without installing
python main.py                 # minimal scripted example (NVDA / fixed date)
```

Python >= 3.10; CI matrix tests 3.10–3.13. There is no `ruff format` adoption yet
(line length / layout is intentionally not enforced — see `pyproject.toml` comment);
don't reformat unrelated code as a side effect of a change.

### CI (`.github/workflows/ci.yml`)

Three jobs, all must stay green: `pytest -q` across the Python matrix, a clean-install
smoke test (`pip install .` with **no** dev extras, then imports `tradingagents` and
`cli.main` — catches undeclared runtime deps), and `ruff check .` over the full repo.

## Repository layout

```
tradingagents/
  agents/
    analysts/        # market, fundamentals, news, sentiment (formerly "social") analysts
    researchers/      # bull_researcher, bear_researcher (structured debate)
    managers/         # research_manager, portfolio_manager (deep-think LLM, structured output)
    risk_mgmt/        # aggressive / neutral / conservative debators
    trader/           # trader.py — turns research into a trade plan
    utils/            # tool functions exposed to agents (one file per data domain),
                       # agent_states.py (LangGraph state schema), memory.py (decision log),
                       # structured.py (structured-output binding helper), schemas.py (pydantic)
  graph/
    trading_graph.py     # TradingAgentsGraph — the main orchestration class
    setup.py             # builds the LangGraph StateGraph (nodes + edges)
    analyst_execution.py # builds the analyst execution plan (order/concurrency)
    conditional_logic.py # should_continue_* routing functions (debate/risk loop limits)
    propagation.py        # initial state construction, graph invoke args
    reflection.py          # post-hoc reflection on realized returns
    signal_processing.py   # extracts BUY/SELL/HOLD from the final decision text
    checkpointer.py         # per-ticker SQLite LangGraph checkpointing (opt-in resume)
  dataflows/
    interface.py         # vendor routing: TOOLS_CATEGORIES, VENDOR_METHODS, dispatch
    config.py             # process-global mutable config (get_config/set_config)
    y_finance.py, alpha_vantage*.py, fred.py, polymarket.py, reddit.py, stocktwits.py,
    yfinance_news.py       # per-vendor data fetchers
    symbol_utils.py        # ticker normalization (e.g. XAUUSD -> GC=F), exchange suffixes
    market_data_validator.py, errors.py  # data-quality guards, vendor exception types
  llm_clients/
    factory.py            # create_llm_client(provider, model, base_url, **kwargs) — entry point
    base_client.py         # BaseLLMClient interface
    anthropic_client.py, google_client.py, azure_client.py, bedrock_client.py,
    openai_client.py       # OpenAI-compatible catch-all (OpenAI, DeepSeek, Qwen, GLM,
                            # MiniMax, OpenRouter, Ollama, xAI, ...) — see is_openai_compatible
    model_catalog.py       # known model IDs per provider (CLI dropdowns)
    capabilities.py        # per-provider/model feature table (e.g. tool_choice support)
    api_key_env.py         # provider -> env var name mapping
  default_config.py        # DEFAULT_CONFIG dict + TRADINGAGENTS_* env-var override machinery
cli/
  main.py                 # Typer app, interactive prompts, run loop, rendering
  config.py, models.py, utils.py, stats_handler.py, announcements.py
tests/                    # pytest, one file per concern (see Testing below)
scripts/                  # smoke_structured_output.py — manual structured-output check
main.py                   # top-level scripted usage example
```

## Core architecture

### The graph (`tradingagents/graph/`)

`TradingAgentsGraph` (`trading_graph.py`) is the main entry point:

1. Builds a `deep_thinking_llm` and `quick_thinking_llm` via `create_llm_client`
   (deep = `deep_think_llm` config key, used by Research Manager / Portfolio
   Manager; quick = `quick_think_llm`, used by everything else).
2. Builds `ToolNode`s per analyst category (`market`, `social`, `news`,
   `fundamentals`) from the abstract tool functions in `agents/utils/agent_utils.py`.
3. Delegates graph construction to `GraphSetup.setup_graph()`, which wires:
   `START -> analyst -> tools -> analyst -> clear -> next analyst -> ... ->
   Bull/Bear Researcher (debate loop) -> Research Manager -> Trader ->
   Aggressive/Conservative/Neutral risk debate loop -> Portfolio Manager -> END`.
4. `ConditionalLogic` enforces `max_debate_rounds` / `max_risk_discuss_rounds` to
   terminate the debate/risk loops.
5. `propagate(ticker, trade_date, asset_type)` runs one full analysis: resolves
   pending memory-log entries, optionally recompiles with a per-ticker SQLite
   checkpointer (`checkpoint_enabled`), builds initial state (including the
   deterministically-resolved instrument identity), invokes/streams the graph,
   writes results to `results_dir` and the memory log, and returns
   `(final_state, decision)`.

Analyst count/order is configurable via `selected_analysts` — see
`analyst_execution.py` for how the plan (and any concurrency) is built.

### LLM providers (`tradingagents/llm_clients/`)

`create_llm_client(provider, model, base_url, **kwargs)` is the single entry
point. Native SDKs (Anthropic, Google, Azure, Bedrock) get dedicated clients;
everything else funnels through `OpenAIClient` as "OpenAI-compatible"
(OpenAI, DeepSeek, Qwen/DashScope, GLM/Zhipu, MiniMax, OpenRouter, Ollama, xAI,
Mistral, Moonshot, Groq, Nvidia, and any custom endpoint via
`openai_compatible` + `backend_url`). Provider modules are imported lazily
inside `factory.py` so importing the factory never pulls in a provider SDK you
aren't using, and doesn't require that provider's API key to be set. When
adding a new provider, prefer extending `is_openai_compatible` / the registry
over adding a new native client, unless the provider truly needs a different
SDK/auth model (like Bedrock's SigV4).

Provider-specific "thinking"/reasoning-effort knobs (`google_thinking_level`,
`openai_reasoning_effort`, `anthropic_effort`) are mapped in
`TradingAgentsGraph._get_provider_kwargs()`; `temperature` is forwarded to
every provider uniformly. `capabilities.py` records which providers/models
don't support certain features (e.g. `tool_choice` on DeepSeek reasoner /
MiniMax M2.x) so structured-output binding can adapt automatically.

### Config (`tradingagents/default_config.py` + `tradingagents/dataflows/config.py`)

`DEFAULT_CONFIG` is a module-level dict, the single source of truth for
run behavior (models, debate rounds, vendor selection, paths, language,
benchmark, etc). `_ENV_OVERRIDES` in `default_config.py` maps
`TRADINGAGENTS_*` env vars onto config keys with type-aware coercion driven
by the *existing* default's type — **to expose a new config key for env
override, add one row there**, no other wiring needed.

`dataflows/config.py` holds a process-global mutable copy
(`get_config()`/`set_config()`) that `TradingAgentsGraph.__init__` seeds from
`self.config`; data-vendor tool functions read from it. `set_config` **merges**
rather than replacing, which is why tests reset it in an autouse fixture (see
Testing below) — don't rely on merge semantics to "clear" a key.

### Data vendors (`tradingagents/dataflows/interface.py`)

`TOOLS_CATEGORIES` groups tool functions by data domain; `VENDOR_METHODS` maps
each abstract tool name to its per-vendor implementation. `data_vendors`
(category-level) and `tool_vendors` (tool-level override) in config select
which vendor(s) actually get called — **the configured chain is exact, not a
suggestion**; nothing silently falls back to an unconfigured vendor. Comma-separated
values (e.g. `"yfinance,alpha_vantage"`) give an ordered fallback chain.

### Persistence

- **Decision log** (always on): `TradingMemoryLog`
  (`agents/utils/memory.py`) appends every completed decision to
  `~/.tradingagents/memory/trading_memory.md` (override via
  `TRADINGAGENTS_MEMORY_LOG_PATH`). On the next run for the same ticker, it
  resolves the realized return (raw + alpha vs. the resolved benchmark),
  generates a reflection, and injects recent same-ticker + cross-ticker
  history into the Portfolio Manager prompt.
- **Checkpoint resume** (opt-in, `checkpoint_enabled` / `--checkpoint`):
  per-ticker SQLite DBs under `data_cache_dir/checkpoints/<TICKER>.db`
  (`graph/checkpointer.py`), keyed by a `thread_id` derived from
  ticker+date, so a crashed run resumes and a new date starts fresh.
  Cleared automatically on success; `--clear-checkpoints` resets manually.

### Instrument identity & symbol normalization

`resolve_instrument_identity` (in `agent_utils.py`, `functools.lru_cache`d) does
a best-effort, fail-open yfinance lookup so agents anchor to the real company
name/sector instead of hallucinating one from price action alone (#814).
`symbol_utils.normalize_symbol` maps informal symbols to canonical Yahoo
tickers (e.g. `XAUUSD` -> `GC=F`) so identity resolution, price fetches, and
realized-return lookups all hit the same instrument (#983/#984). Ticker
values that reach the filesystem (log directories) go through
`dataflows/utils.safe_ticker_component` to reject path-traversal payloads.

## Conventions

- **Docstrings carry the "why", not the "what".** Comments/docstrings in this
  codebase consistently explain a non-obvious constraint or the bug/issue a
  piece of logic guards against (often with a `(#NNN)` GitHub issue
  reference), not a restatement of the code. Match that style — don't add
  comments that just narrate what a line does.
- **Fail open, not closed**, for best-effort enrichment (identity resolution,
  news fetches): catch broad exceptions, log at `debug`/`warning`, return an
  empty/neutral value, and let the pipeline continue rather than raising.
  Reserve hard failures for vendor misconfiguration / genuinely fatal cases
  (see `dataflows/errors.py`: `NoMarketDataError`, `VendorNotConfiguredError`,
  `VendorRateLimitError`).
- **Config keys, not hardcoded values.** New tunables belong in
  `DEFAULT_CONFIG`, with an `_ENV_OVERRIDES` entry if a `.env`-driven override
  makes sense. Don't hardcode a provider-specific URL as a shared default (see
  the `backend_url: None` comment — a stale default previously leaked between
  providers).
- **Lazy imports for optional/heavy dependencies**, especially provider SDKs
  in `llm_clients/factory.py` and vendor modules — keeps `import tradingagents`
  cheap and avoids failing at import time when an unrelated provider's SDK or
  key is missing.
- **Vendor routing is explicit.** Never add implicit cross-vendor fallback
  inside a tool function; the fallback chain is whatever the user configured
  in `data_vendors`/`tool_vendors`.
- Ruff-enforced style: `select = ["E", "W", "F", "I", "B", "UP", "C4", "SIM"]`,
  `E501` (line length) ignored, `__init__.py` re-exports exempted from F401.
  Run `ruff check .` before committing — CI lints the whole repo, not just a diff.

## Testing

- `tests/conftest.py` has two **autouse** fixtures: one stubs every provider
  API-key env var with a placeholder (so tests never hang on real network
  calls / missing keys), and one resets `dataflows.config._config` to a fresh
  deep copy of `DEFAULT_CONFIG` before and after every test (because
  `set_config` merges — without this, per-test vendor/config overrides leak
  across tests). If you add a new API-key env var for a provider, add it to
  `_API_KEY_ENV_VARS` in `conftest.py` too.
- A `mock_llm_client` fixture patches `llm_clients.factory.create_llm_client`
  for tests that need a graph/agent built without hitting a real LLM.
- Markers: `unit`, `integration`, `smoke` (registered in `conftest.py` and
  `pyproject.toml`). Prefer `unit` for anything that doesn't need network/LLM
  access.
- Test files are one-per-concern and named after what they cover (provider
  routing, symbol normalization, checkpoint resume, i18n coverage, etc.) —
  follow that granularity for new tests rather than growing one large file.
- `scripts/smoke_structured_output.py` is a manual (non-pytest) check for
  structured-output binding across providers; run it directly when touching
  `agents/utils/structured.py` or provider tool-calling behavior.

## Gotchas worth knowing before changing things

- Analyst named `"social"` in code/state (`AnalystType.SOCIAL`) is the
  user-facing **Sentiment Analyst** — the wire value was kept for saved-config
  backward compatibility even though the display name changed.
- The message-clearing placeholder between analysts (`create_msg_delete`)
  deliberately avoids a bare `"Continue"` string — some OpenAI-compatible
  providers treat it as the literal task and go off-topic (#888).
- `temperature`, when set, is forwarded to every provider; reasoning models
  largely ignore it, so don't expect it alone to produce reproducible runs
  (see README "Reproducibility" section before changing determinism-related code).
- `backend_url` in `DEFAULT_CONFIG` must stay `None` — provider-specific
  defaults live in each client; a shared default here previously leaked one
  provider's URL into another's requests.
- AWS Bedrock is an optional extra (`pip install ".[bedrock]"`, `langchain-aws`)
  — don't add it to the core dependency list.
