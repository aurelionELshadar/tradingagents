"""Agentic OS - kleiner lokaler Server. Nur Python-Standardbibliothek.
Lauscht ausschliesslich auf 127.0.0.1 (nicht aus dem Netz erreichbar)."""
import contextlib
import json
import os
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

HOST, PORT = "127.0.0.1", 8765
ROOT = os.path.dirname(os.path.abspath(__file__))
DATA, BRAIN, STATIC = (os.path.join(ROOT, d) for d in ("data", "brain", "static"))
ALLOWED_HOSTS = {f"127.0.0.1:{PORT}", f"localhost:{PORT}"}

def load(name, default):
    try:
        with open(os.path.join(DATA, name), encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default

def save(name, obj):
    path = os.path.join(DATA, name)
    with open(path + ".tmp", "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    os.replace(path + ".tmp", path)

def log_event(text):
    ev = load("events.json", [])
    ev.insert(0, {"zeit": time.strftime("%Y-%m-%d %H:%M:%S"), "text": text})
    save("events.json", ev[:200])

def brain_notes():
    out = []
    for fn in sorted(os.listdir(BRAIN)):
        if fn.endswith(".md"):
            with open(os.path.join(BRAIN, fn), encoding="utf-8") as f:
                out.append({"name": fn[:-3], "text": f.read()})
    return out

class H(BaseHTTPRequestHandler):
    server_version = "AgenticOS"

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        if not isinstance(body, bytes):
            body = json.dumps(body, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _host_ok(self):
        # Schutz gegen DNS-Rebinding: nur Anfragen an localhost/127.0.0.1
        if self.headers.get("Host", "") not in ALLOWED_HOSTS:
            self._send(403, {"fehler": "Host nicht erlaubt"})
            return False
        return True

    def do_GET(self):
        if not self._host_ok():
            return
        p = urlparse(self.path).path
        if p == "/api/state":
            return self._send(200, {
                "agenten": load("agents.json", []),
                "ereignisse": load("events.json", [])[:20],
                "gehirn": brain_notes(),
                "nacht": load("night.json", []),
            })
        if p in ("/", "/index.html"):
            with open(os.path.join(STATIC, "index.html"), "rb") as f:
                return self._send(200, f.read(), "text/html; charset=utf-8")
        self._send(404, {"fehler": "nicht gefunden"})

    def do_POST(self):
        if not self._host_ok():
            return
        # Nur Aufrufe von der eigenen Seite zulassen
        origin = self.headers.get("Origin")
        if origin and urlparse(origin).netloc not in ALLOWED_HOSTS:
            return self._send(403, {"fehler": "Origin nicht erlaubt"})
        parts = urlparse(self.path).path.strip("/").split("/")
        if len(parts) == 4 and parts[:2] == ["api", "agenten"] and parts[3] == "umschalten":
            agents = load("agents.json", [])
            for a in agents:
                if a["id"] == parts[2]:
                    a["status"] = "pausiert" if a["status"] == "läuft" else "läuft"
                    save("agents.json", agents)
                    log_event(f'{a["name"]}: {a["status"]}')
                    return self._send(200, a)
        self._send(404, {"fehler": "nicht gefunden"})

    def log_message(self, fmt, *args):
        pass

if __name__ == "__main__":
    srv = ThreadingHTTPServer((HOST, PORT), H)
    print(f"Agentic OS läuft auf http://{HOST}:{PORT}  (Strg+C zum Beenden)", flush=True)
    with contextlib.suppress(KeyboardInterrupt):
        srv.serve_forever()
