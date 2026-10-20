#!/bin/bash
# Installs graphify (via pipx) and its Claude skill in cloud sessions.
set -euo pipefail

[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] || exit 0

export PATH="$HOME/.local/bin:$PATH"

if ! command -v pipx >/dev/null 2>&1; then
  pip install --quiet --user --ignore-installed pipx
fi

if ! command -v graphify >/dev/null 2>&1; then
  pipx install --quiet graphifyy
fi

[ -f "$HOME/.claude/skills/graphify/SKILL.md" ] || graphify install >/dev/null

if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export PATH=\"$HOME/.local/bin:\$PATH\"" >> "$CLAUDE_ENV_FILE"
fi
