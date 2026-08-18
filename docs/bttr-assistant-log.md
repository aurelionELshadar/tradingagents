# BTTR Assistant Log

Dokumentation der Claude-Session-Arbeit für Adrian Grüdl / Back to the Roots (Aurelion). Stand: 18.08.2026.

## 1. Kosmischer Kompass → Google Kalender

Der Nutzer hat einen selbst erstellten astrologischen "Kosmischen Kompass" (Juli–Dezember 2026) als HTML-Dokument bereitgestellt. Umsetzung:

- **39 Einzeltermine** im Google Kalender (adrian.gruedl@gmail.com) angelegt — jeder Neumond, Vollmond, jede Finsternis, jeder relevante Planetenwechsel/Rückläufigkeit, mit Uhrzeit (Zeitzone Europe/Berlin), Positionsangabe und der vollständigen Deutung (Energie / Für dich / So nutzt du sie) als Beschreibung.
- Farbliche Markierung: Portal-/Sonnentage golden, die beiden Finsternisse (12.8. Sonnenfinsternis auf dem Nordknoten, 28.8. Mondfinsternis) rot.
- **Täglicher Reminder** "🧭 Kompass-Check" dreimal täglich (09:00 / 14:00 / 20:00), wiederkehrend bis 31.12.2026.

## 2. Google Drive — vollständige Bestandsaufnahme & Bereinigung

### Ausgangslage
2.166 Dateien, 2,25 GB, größtenteils unsortiert im Root ("Meine Ablage") liegend. Das Drive ist die reine Ablage-/Backup-Ebene; das eigentliche operative "BTTR Memory-Loop-System" (00–90-Kategorienstruktur, 11 Module) lebt lokal auf dem Mac unter `/Users/adrian/Documents/Claude/Projects/BTTR/`.

### Analyse
- **255 Gruppen exakter Duplikate** gefunden (307 überzählige Kopien, ~256 MB), plus 201 "nahe" Duplikate (echte Revisionen, z. B. Brand-Manual-Versionen, Businessplan-Fassungen).
- Ein kompletter fremder Projektbaum ("BurningMan2026/.../BAFA-Creator-AI", ~300 Dateien) identifiziert — gehört `froeba.kevin@gmail.com`, nicht dem Nutzer. **Bewusst nicht angefasst.**
- 28 vermeintlich "verwaiste" Root-Level-Dateien (Leads-Listen, caller_report etc.) geprüft — stellten sich als fremdes Eigentum verschiedener anderer Accounts heraus, nicht des Nutzers. Ebenfalls unangetastet.
- Zwei Versionsketten inhaltlich aufgeklärt: aktueller Businessplan (`Businessplan_BTTR_Aurelion_zusammengefuehrt`, 04.08.) ersetzt die alte `Businessplan_Back_to_the_Roots_V2.pdf`; die finale Widerspruch-Handwerksrolle-Fassung (17.07.) ersetzt den Entwurf vom 15.07.
- "ARCHITECTURE.md" im Root erwies sich als fachfremdes Dokument (beschreibt ein unabhängiges SaaS-Projekt "Aurelius", nicht BTTR/Aurelion) — auf Nutzerwunsch archiviert statt gelöscht.

### Durchgeführte Bereinigung
- **16 Duplikate der Kerndokumente** gelöscht (Selbstauskunft, Gewerbeanmeldung, Gründungsvorhaben-PDFs, Businessplan-Dateien, caller_report u. a.)
- **223 + 194 = insgesamt 417 Foto-/Video-Dateien** dedupliziert bzw. konsolidiert (~231 MB freigegeben durch Löschung, plus vollständige Konsolidierung aller verbleibenden Root-Einzelfotos in den Fotoordner)
- **133 Dokumente** aus dem Root in passende bestehende bzw. neu angelegte Ordner einsortiert
- Neue Ordner: `Archiv` (mit Unterordnern `Kevin-Zusammenarbeit`, `Alte-Versionen`, `Terminal-Logs`, `Sonstiges`), `Sonstige Projekte` (für BTTR-fremde Recherchen wie Cannabis-/Food-Tech-Förderung)
- Vier Mail-Postfach-ZIP-Exporte, ein 117,7-MB-ElsterAuthenticator.dmg und eine kryptisch benannte memStream-PDF ins Archiv verschoben
- Zwischenzeitlich angelegter "BTTR-System"-Ordner wieder aufgelöst und mit dem bereits existierenden Ordner "Notizen & Learnings" zusammengeführt
- Ein neues Dokument **"Drive-Inhaltsverzeichnis"** im Root angelegt: vollständige, aktuelle Übersicht aller Ordner mit Kurzbeschreibung, Bereinigungshistorie und offenen Prüfpunkten
- **Root ist jetzt vollständig frei von losen Dokumenten und Fotos/Videos** — nur noch Ordner.

### Offene Punkte für Adrian
- Auffällige Größenanomalien zur Prüfung: eine 28,6-MB-Version des KfW067-Pitchdecks (normale Version: 34 KB) und ein 23,7-MB-Dokument "Agentur für Arbeit Vorlage" (normale vergleichbare Dokumente: wenige 10 KB).
- Ordner "Aus Chrome gespeichert" könnte inhaltlich mit "Amtliche Dokumente" zusammengelegt werden (aktuell getrennt).

## 3. Claude-Code-Remote-Sessions konsolidiert

- Die verbundene lokale Mac-Session wurde als zentrale Session umbenannt: **"BTTR Terminal — Adrian's Mac"**.
- Zwei veraltete, getrennte lokale Sessions ("local-cosmic-prism", "Aurelion MVP Setup") archiviert.
- Eine blockierte Session ("Commit changes") mit einem ungeklärten `rtk proxy`-Befehl ("bypass filtering") auf `COCKPIT.html` bewusst **nicht** angefasst — erfordert die eigene Prüfung des Nutzers, da von hier aus kein voller Gesprächsverlauf einsehbar war.
- Festgestellt: aktuell keine aktiven Scheduled Tasks/Routines auf dem Account.

## 4. Lokales Mac-Aufräumen (Desktop, Downloads etc.)

Aus dieser Cloud-Session heraus **nicht möglich** — kein Zugriff auf das lokale Dateisystem. Dafür ist eine lokale Claude-Code-Session auf dem Mac nötig (`npm install -g @anthropic-ai/claude-code`, dann `claude` im gewünschten Ordner starten, z. B. `~/Desktop` oder `~/Documents/Claude/Projects/BTTR`).

## 5. TradingAgents-CLI (dieses Repo) getestet

Im Rahmen einer Nebenaufgabe wurde die CLI dieses Repositories (`tradingagents/`) end-to-end durchgesteuert (Ticker-, Datums-, Analysten-, Provider-Auswahl) bis zur erwarteten Grenze: fehlender LLM-API-Key. Kein Fehlverhalten der App festgestellt.

## 6. Repo-Erstellung

Ein Versuch, ein eigenständiges neues GitHub-Repository für diese Dokumentation anzulegen, scheiterte an fehlender Berechtigung der GitHub-Integration dieser Session (403, "Resource not accessible by integration" — die Integration ist auf bestehende Repos beschränkt, keine Repo-Erstellung möglich). Diese Datei liegt deshalb stattdessen hier im bestehenden `tradingagents`-Repo, auf einem eigenen Branch.

---
*Diese Dokumentation wurde automatisiert aus dem Sitzungsverlauf erstellt.*
