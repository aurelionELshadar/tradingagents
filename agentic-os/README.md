# Agentic OS

Kleine lokale Web-App: Seitenleiste mit Cockpit, Agenten, Gehirn, Nacht.
Nur Python 3 nötig, nichts zu installieren. Erreichbar nur über `127.0.0.1` (dein Rechner).

## Starten
```bash
cd agentic-os
./start.sh
```
Dann im Browser öffnen: **http://127.0.0.1:8765**

## Stoppen
```bash
./stop.sh
```
Falls die Seite nicht lädt: `server.log` ansehen.

## Aufbau (4 Dateien)
- `server.py` – der Server (lauscht nur auf 127.0.0.1, prüft Host/Origin)
- `static/index.html` – die ganze Oberfläche
- `data/*.json` – Agenten, Ereignisse, Nacht-Jobs (einfach per Texteditor änderbar)
- `brain/*.md` – dein Gehirn: jede Textdatei erscheint unter „Gehirn“

## Stand
Beispieldaten. Pausieren/Starten ändert nur den Status in `data/agents.json`
und schreibt ein Ereignis. Echte Agenten hängst du später an.
Schriften (Cormorant Garamond, Jost) lädt der Browser von Google Fonts;
ohne Internet greift eine Ersatzschrift.
