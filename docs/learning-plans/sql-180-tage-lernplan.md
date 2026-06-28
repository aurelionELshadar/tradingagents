# SQL / Datenbanken — 180-Tage-Lernplan

**Profil:** Anfänger ohne Vorkenntnisse · 90+ Minuten/Tag verfügbar · Engine: PostgreSQL
**Methoden:** Spaced Repetition, Interleaving, Feynman-Technik, Active Recall
**Laufzeit:** 26 Wochen (Tag 1–180)

---

## 1. Funktionsprinzipien (kein Theorie-Ballast, nur Regeln)

| Prinzip | Konkrete Umsetzung in diesem Plan |
|---|---|
| **Spaced Repetition** | Jedes neue Konzept kommt in ein Anki-Deck (Tags = Phase/Woche). Wiederholintervalle: Tag+1, Tag+3, Tag+7, Tag+14, Tag+30. Die tägliche "Recall"-Phase nutzt Anki im Standard-Algorithmus — keine manuelle Terminplanung nötig. |
| **Interleaving** | Jeder "Interleaving"-Block kombiniert IMMER den heutigen Stoff mit mindestens einem Thema aus einer früheren Woche. Nie isoliert ein einzelnes Thema üben. |
| **Feynman-Technik** | 1× pro Tag: das Tageskonzept in 3–5 einfachen Sätzen erklären (schriftlich, in eine `feynman-log.md` schreiben), als würde man es einer Person ohne Vorwissen beibringen. Stocken/Unklarheit = Lücke → am Folgetag zuerst klären. |
| **Active Recall** | Nie Notizen/Doku zuerst öffnen. Erst aus dem Kopf abrufen/versuchen, dann erst nachschlagen. Gilt für Anki-Karten UND für die täglichen Übungsaufgaben. |

---

## 2. Standard-Tagesstruktur (Mo–Fr, 90 Minuten)

| Block | Dauer | Inhalt |
|---|---|---|
| 1. Active Recall | 15 Min | Anki-Review der Fälligkeiten (alte Konzepte aus Vorwochen) |
| 2. Neuer Stoff | 45 Min | Theorie kurz (≤10 Min) + sofort an Übungsaufgaben anwenden |
| 3. Interleaving | 20 Min | 3–5 Aufgaben, die heutiges Thema mit ≥1 älterem Thema kombinieren |
| 4. Feynman | 10 Min | Tageskonzept in eigenen Worten erklären, Lücken markieren |

**Samstag (60–90 Min):** Wochenprojekt — alle Wochenthemen in einer zusammenhängenden Aufgabe anwenden (Konsolidierung).
**Sonntag:** Puffer/Nachholtag bei Rückstand, sonst frei (kein neuer Stoff, kein Anki-Backlog aufbauen lassen).

Diese Struktur wird unten **nicht** pro Woche wiederholt — nur die Inhalte pro Tag sind angegeben.

---

## 3. Setup (vor Tag 1 erledigen)

1. PostgreSQL lokal installieren (oder Docker: `docker run --name pg-learn -e POSTGRES_PASSWORD=learn -p 5432:5432 -d postgres:16`)
2. GUI-Client: DBeaver oder pgAdmin
3. Übungsdatenbank: **Pagila** (Postgres-Port der Sakila-DB, realistische Kunden/Filme/Vermietungen-Daten) importieren
4. Anki installieren, ein Deck `SQL-180` mit Tags je Phase anlegen
5. Bookmarks: SQLBolt, PGExercises (pgexercises.com), Use The Index Luke (use-the-index-luke.com), LeetCode/HackerRank SQL, SQL Murder Mystery (mystery.knightlab.com)
6. Datei `feynman-log.md` anlegen für die täglichen Feynman-Einträge

---

## 4. Phasenüberblick

| Phase | Wochen | Tage | Fokus | Abschluss-Artefakt |
|---|---|---|---|---|
| 1 | 1–4 | 1–28 | Querying-Grundlagen | Quiz ≥85%, Feynman-Doku "SQL-Grundlagen" |
| 2 | 5–8 | 29–56 | Datenmodellierung | Eigenes 3NF-Schema, ≥6 Tabellen |
| 3 | 9–12 | 57–84 | Fortgeschrittenes SQL | Window Functions/CTE-Kompetenz, View+Function im eigenen Schema |
| 4 | 13–16 | 85–112 | Performance | Optimierungs-Case-Study mit Vorher/Nachher-Zahlen |
| 5 | 17–20 | 113–140 | Engines, Trigger, Security | Audit-Trigger, Security-Review-Dokument |
| 6 | 21–26 | 141–180 | Abschlussprojekt | Vollständiges, optimiertes, dokumentiertes DB-Projekt |

---

## 5. Wochenpläne

### Phase 1 — Querying-Grundlagen

#### Woche 1 (Tag 1–7)
**Wochenziel:** Postgres + Pagila-DB lauffähig; SELECT/WHERE/ORDER/LIMIT sicher beherrschen.
- Mo: Setup (Postgres, DBeaver, Pagila-Import), erste `SELECT *`-Queries
- Di: WHERE mit `=, <>, <, >, BETWEEN, IN, LIKE` — 10 Filterabfragen auf Pagila
- Mi: NULL-Handling (`IS NULL`), `AND/OR/NOT`, Klammerlogik
- Do: `ORDER BY` (mehrere Spalten, ASC/DESC), `LIMIT/OFFSET`, `DISTINCT`
- Fr: Spalten-Aliasing, Arithmetik/String-Concat in SELECT, `CASE WHEN`-Basics
- Sa: SQLBolt Lektionen 1–8 + 5 eigene Fragen an Pagila formulieren und beantworten
**Meilenstein:** SQLBolt 1–8 abgeschlossen; 5 eigene Fragen korrekt ohne Syntax-Nachschlagen beantwortet.

#### Woche 2 (Tag 8–14)
**Wochenziel:** INNER/LEFT/RIGHT/FULL JOIN sicher anwenden.
- Mo: INNER JOIN (2 Tabellen), Tabellen-Aliasing
- Di: LEFT/RIGHT JOIN, Anwendungsfall "fehlende Daten finden"
- Mi: FULL OUTER JOIN, JOIN über 3+ Tabellen
- Do: Self-Join, CROSS JOIN, Kartesisches Produkt erkennen
- Fr: Interleaving — Join + WHERE + ORDER kombiniert (Stoff W1+W2)
- Sa: 10 Join-Aufgaben auf Pagila (z. B. "Kunden ohne jemals eine Vermietung")
**Meilenstein:** 10 PGExercises-Join-Aufgaben gelöst, ≥8/10 ohne Hilfe; erklärt mündlich, wann LEFT statt INNER nötig ist.

#### Woche 3 (Tag 15–21)
**Wochenziel:** GROUP BY/HAVING und Subqueries (scalar + korreliert) korrekt einsetzen.
- Mo: `COUNT/SUM/AVG/MIN/MAX`, `GROUP BY`
- Di: `HAVING` vs `WHERE`, Multi-Column GROUP BY
- Mi: Scalar Subqueries (in SELECT/WHERE)
- Do: Korrelierte Subqueries, `EXISTS`/`NOT EXISTS`
- Fr: Interleaving — Join + Aggregation + Subquery kombiniert
- Sa: 8 Analyse-Queries auf Pagila (Umsatz pro Kategorie, Top-5-Kunden)
**Meilenstein:** 3-stufige Analysefrage (Filter→Join→Aggregation) in <10 Min ohne Vorlage lösen.

#### Woche 4 (Tag 22–28) — Review Phase 1
**Wochenziel:** Set-Operationen, Datentypen, CASE vertieft; Phase 1 konsolidiert.
- Mo: `UNION/UNION ALL`, `INTERSECT`, `EXCEPT`
- Di: Datentypen (INT, NUMERIC, TEXT, DATE/TIMESTAMP, BOOLEAN), `::`-Casting
- Mi: `CASE WHEN` vertieft (mehrstufig, mit Aggregation kombiniert)
- Do: Datum/Zeit-Funktionen (`EXTRACT`, `DATE_TRUNC`, Intervalle)
- Fr: Großes Interleaving-Review — 15 gemischte Aufgaben aus W1–4 (60 Min Zeitlimit)
- Sa: Feynman-Dokument "SQL-Grundlagen" (1 Seite + 5 Beispielqueries)
- So: Phase-1-Abschlusstest, 20 Fragen, Zielscore ≥85%
**Meilenstein:** Test ≥85%; Feynman-Dokument fertig (wird Referenz für spätere Reviews).

---

### Phase 2 — Datenmodellierung

#### Woche 5 (Tag 29–35)
**Wochenziel:** ER-Modellierung (Entities, Kardinalitäten) korrekt anwenden.
- Mo: Entities & Attribute identifizieren (Beispiel: Bibliothek)
- Di: 1:1, 1:n, n:m, Junction Tables
- Mi: Crow's-Foot-Notation, Tool dbdiagram.io
- Do: Von Anforderungstext zu ER-Diagramm (Übungsfälle Bibliothek/Online-Shop)
- Fr: Interleaving — ER-Diagramm + passende SELECT-Fragen formulieren
- Sa: Eigenes ER-Diagramm für Wahlthema entwerfen (z. B. Fitness-Tracker)
**Meilenstein:** Eigenes ER-Diagramm, ≥5 Entities, korrekte Kardinalitäten, gegengeprüft ohne Strukturfehler.

#### Woche 6 (Tag 36–42)
**Wochenziel:** 1NF–3NF anwenden, Verstöße erkennen und beheben.
- Mo: 1NF (atomare Werte)
- Di: 2NF (partielle Abhängigkeiten entfernen)
- Mi: 3NF (transitive Abhängigkeiten entfernen)
- Do: Denormalisierung-Vorgeschmack, BCNF kurz
- Fr: Interleaving — unnormalisierte Tabelle aus W5-Projekt selbst normalisieren
- Sa: Eigenes Diagramm aus W5 auf 3NF prüfen/korrigieren
**Meilenstein:** 3 gegebene unnormalisierte Beispiele in <15 Min je korrekt bis 3NF zerlegt, 0 Fehler.

#### Woche 7 (Tag 43–49)
**Wochenziel:** `CREATE TABLE` mit PK/FK/UNIQUE/CHECK/DEFAULT sicher schreiben.
- Mo: PRIMARY KEY, natürliche vs. Surrogate Keys
- Di: FOREIGN KEY, `ON DELETE/UPDATE CASCADE/RESTRICT`
- Mi: UNIQUE, CHECK, DEFAULT, NOT NULL
- Do: DDL — `CREATE/ALTER/DROP TABLE`
- Fr: Interleaving — eigenes ER-Diagramm in DDL übersetzen
- Sa: Vollständiges Schema für Wahlthema in Postgres ausführen
**Meilenstein:** Schema läuft fehlerfrei, alle PK/FK/Constraints korrekt (per `\d+` verifiziert).

#### Woche 8 (Tag 50–56) — Review Phase 2
**Wochenziel:** Schema mit Testdaten befüllt; Phase 2 konsolidiert.
- Mo: Testdaten einfügen (`INSERT`, Mehrzeilen), Validierungsqueries
- Di: Schema-Review, Indexe auf FKs anlegen (Vorgriff Phase 4)
- Mi: Constraint-Verstöße bewusst provozieren, Fehlermeldungen verstehen
- Do: Großes Interleaving-Review — 15 Aufgaben aus W5–8
- Fr: Phase-2-Abschlusstest, 20 Fragen, Zielscore ≥85%
- Sa: Feynman-Dokument: Schema + Normalisierungsentscheidungen erklären (1 Seite)
**Meilenstein:** Test ≥85%; Schema ≥6 Tabellen, ≥50 Testzeilen, lauffähig.

---

### Phase 3 — Fortgeschrittenes SQL

#### Woche 9 (Tag 57–63)
**Wochenziel:** `ROW_NUMBER/RANK/DENSE_RANK/LAG/LEAD` mit `PARTITION BY` anwenden.
- Mo: `OVER()`, `PARTITION BY`, `ROW_NUMBER()`
- Di: `RANK()` vs `DENSE_RANK()`, Top-N pro Gruppe
- Mi: `LAG()/LEAD()`, Vorher-Nachher-Vergleiche
- Do: Aggregat-Window-Functions, laufende Summen
- Fr: Interleaving — Window Functions + Joins + Aggregation auf Pagila
- Sa: "Top 3 Filme pro Kategorie" + "laufende Umsatzsumme pro Monat"
**Meilenstein:** 8 PGExercises-Window-Aufgaben, ≥6/8 ohne Hilfe.

#### Woche 10 (Tag 64–70)
**Wochenziel:** CTEs (inkl. rekursiv) sicher nutzen, bewusst gegen Subquery abwägen.
- Mo: Einfache CTEs (`WITH`), Lesbarkeit vs. verschachtelte Subqueries
- Di: Mehrere CTEs verketten, CTE + Window Function kombiniert
- Mi: Rekursive CTEs — Grundkonzept (Hierarchien)
- Do: Rekursive CTE-Übung (Kategorie-Baum)
- Fr: Interleaving — gleiche Aufgabe als Subquery vs. CTE schreiben, vergleichen
- Sa: Eigene rekursive Hierarchie-Query (eigenes Schema oder `film_category`)
**Meilenstein:** 3 verschachtelte Subqueries in <10 Min je in lesbare CTE umgeschrieben, 0 Fehler.

#### Woche 11 (Tag 71–77)
**Wochenziel:** ACID erklären, Transaktionen korrekt mit COMMIT/ROLLBACK steuern.
- Mo: `BEGIN/COMMIT/ROLLBACK`
- Di: ACID an Beispielen
- Mi: Isolation Levels (Read Committed, Repeatable Read, Serializable), Dirty/Phantom Reads
- Do: Locking-Grundkonzepte, Deadlocks (konzeptuell)
- Fr: Interleaving — Transaktion + Constraint-Verstoß provozieren, Rollback beobachten
- Sa: Mehrschritt-Transaktion im eigenen Schema (z. B. Bestellung: Lager runter + Order anlegen) inkl. Fehlerfall
**Meilenstein:** ACID in <2 Min frei erklärt ohne Nachschlagen; Transaktionsdemo mit korrektem Rollback bei Fehler.

#### Woche 12 (Tag 78–84) — Review Phase 3
**Wochenziel:** Views und einfache Functions/Procedures erstellen; Phase 3 konsolidiert.
- Mo: `CREATE VIEW`, Materialized View Grundkonzept
- Di: Einfache Functions (PL/pgSQL), Parameter, `RETURN`
- Mi: Stored Procedures, Unterschied Function vs. Procedure
- Do: Großes Interleaving-Review — 15 Aufgaben aus W9–12
- Fr: Phase-3-Abschlusstest, 20 Fragen, Zielscore ≥85%
- Sa: Feynman: Entscheidungsbaum "View vs. Materialized View vs. Function"
**Meilenstein:** Test ≥85%; ≥1 View + ≥1 Function produktiv im eigenen Schema.

---

### Phase 4 — Performance

#### Woche 13 (Tag 85–91)
**Wochenziel:** B-Tree-Indexe verstehen, `EXPLAIN`/`EXPLAIN ANALYZE` lesen.
- Mo: Wie ein Index funktioniert (Analogie Buchregister)
- Di: `CREATE INDEX`, Selektivität
- Mi: `EXPLAIN` lesen — Seq Scan vs. Index Scan vs. Index Only Scan
- Do: `EXPLAIN ANALYZE` — geschätzte vs. tatsächliche Kosten
- Fr: Interleaving — gleiche Query mit/ohne Index, Vorher/Nachher-`EXPLAIN`
- Sa: 5 Slow-Queries identifizieren, Index testen, Verbesserung dokumentieren
**Meilenstein:** 5 `EXPLAIN`-Outputs korrekt interpretiert (Index hilft: ja/nein), 0 Fehler.

#### Woche 14 (Tag 92–98)
**Wochenziel:** Sargable Queries schreiben, häufige Performance-Fallen vermeiden.
- Mo: Sargability (keine Funktionen auf gefilterten Spalten)
- Di: `SELECT *` vermeiden, I/O-Auswirkung
- Mi: Composite Indexes, Spaltenreihenfolge, Covering Indexes
- Do: N+1-Problem, JOIN statt Mehrfachabfragen
- Fr: Interleaving — 5 "schlechte" Queries zu performanten Versionen refactorn
- Sa: Composite Index im eigenen Schema, `EXPLAIN`-Vergleich dokumentieren
**Meilenstein:** 5 ineffiziente Queries selbstständig optimiert, deckt sich mit Referenzlösung in Kernpunkten.

#### Woche 15 (Tag 99–105)
**Wochenziel:** Trade-offs Normalisierung/Denormalisierung/Partitionierung erklären.
- Mo: Wann/warum denormalisieren
- Di: Partitionierung — Range/List/Hash
- Mi: Partitionierung in Postgres anlegen (Beispiel nach Datum)
- Do: Caching-Grundprinzipien auf DB-Ebene
- Fr: Interleaving — 5 Szenarien durchspielen, richtige Strategie begründen
- Sa: Eine Tabelle im eigenen Schema partitionieren oder bewusst denormalisieren, begründen
**Meilenstein:** 5 Szenarien korrekt und begründet der passenden Strategie zugeordnet.

#### Woche 16 (Tag 106–112) — Review Phase 4
**Wochenziel:** Reale Slow-Query end-to-end diagnostizieren; Phase 4 konsolidiert.
- Mo: Optimierungsprozess (Identifizieren → EXPLAIN → Hypothese → Fix → Verifizieren)
- Di: `pg_stat_statements` — teuerste Queries finden
- Mi: Großes Interleaving-Review — 15 Aufgaben aus W13–16
- Do: Phase-4-Abschlusstest, 20 Fragen, Zielscore ≥85%
- Fr: Puffer/Nachholtag
- Sa: Feynman-Case-Study: 1 Slow Query, kompletter Prozess, Vorher/Nachher-Zahlen
**Meilenstein:** Test ≥85%; Case-Study mit messbarer Verbesserung (z. B. Laufzeit −70 %).

---

### Phase 5 — Engines, Praxis, Security

#### Woche 17 (Tag 113–119)
**Wochenziel:** Postgres/MySQL/SQLite-Kernunterschiede benennen; JSON-Spalten nutzen.
- Mo: Postgres vs. MySQL (`LIMIT/OFFSET`, `SERIAL` vs. `AUTO_INCREMENT`, String-Funktionen)
- Di: SQLite — Einsatzzweck, Limitierungen
- Mi: JSON/JSONB in Postgres — `->`, `->>`, GIN-Index
- Do: JSON-Spalte vs. eigene Tabelle — Trade-offs
- Fr: Interleaving — gleiche Aufgabe in Postgres- vs. gedanklicher MySQL-Syntax
- Sa: Sinnvolle JSONB-Spalte im eigenen Schema + Abfragen darauf
**Meilenstein:** Eigene Vergleichstabelle (Feature/Postgres/MySQL-SQLite), ≥10 Zeilen, selbst erstellt.

#### Woche 18 (Tag 120–126)
**Wochenziel:** Trigger korrekt einsetzen, Procedures mit Error Handling schreiben.
- Mo: `CREATE TRIGGER`, BEFORE/AFTER, Audit-Log-Anwendungsfall
- Di: Trigger-Funktionen in PL/pgSQL
- Mi: Error Handling (`EXCEPTION`, `RAISE`)
- Do: Procedure mit Transaktionslogik + Error Handling
- Fr: Interleaving — Trigger + Constraint + Transaktion kombiniert
- Sa: Audit-Trigger im eigenen Schema implementieren
**Meilenstein:** Audit-Trigger funktioniert nachweislich (INSERT/UPDATE/DELETE je korrekt geloggt, 3 Testfälle).

#### Woche 19 (Tag 127–133)
**Wochenziel:** SQL-Injection verstehen/verhindern, Rollen & Rechte verwalten.
- Mo: SQL-Injection-Mechanismus an verwundbarem Beispiel
- Di: Prepared Statements/parametrisierte Queries als Schutz
- Mi: `ROLE`, `GRANT/REVOKE`, Prinzip der minimalen Rechte
- Do: Row-Level Security (Grundkonzept), Datenschutz-Grundprinzipien
- Fr: Interleaving — Security-Review der eigenen Queries/des eigenen Schemas
- Sa: 2 Rollen im eigenen Schema anlegen (`read_only`, `app_user`) mit korrekten Rechten
**Meilenstein:** Schriftliches Beispiel mit verwundbarem + sicherem Code, Mechanismus korrekt erklärt.

#### Woche 20 (Tag 134–140) — Review Phase 5
**Wochenziel:** Relational vs. Dokumenten-DB abgrenzen; Phase 5 konsolidiert.
- Mo: Dokumenten-DB-Grundkonzept (konzeptionell, am Beispiel Dokumentstruktur)
- Di: Wann relational, wann NoSQL
- Mi: Großes Interleaving-Review — 15 Aufgaben aus W17–20
- Do: Phase-5-Abschlusstest, 20 Fragen, Zielscore ≥85%
- Fr: Puffer/Nachholtag
- Sa: Vergleichstabelle relational vs. dokumentenorientiert (≥8 Kriterien) + Entscheidungsleitfaden
**Meilenstein:** Test ≥85%; Vergleichsdokument fertig.

---

### Phase 6 — Abschlussprojekt

#### Woche 21 (Tag 141–147)
**Wochenziel:** Anforderungen + ER-Diagramm für das Abschlussprojekt stehen.
- Mo: Projektthema final wählen (≥8 Tabellen nötig)
- Di: Anforderungen sammeln (welche Fragen soll die DB beantworten?)
- Mi: ER-Diagramm entwerfen
- Do: Normalisierung bis 3NF prüfen
- Fr: Interleaving — Diagramm gegen Checkliste aus Phase 2 prüfen
- Sa: Peer-/Selbstreview des Diagramms
**Meilenstein:** Finales ER-Diagramm, ≥8 Entities, alle Beziehungen korrekt typisiert, 3NF-konform.

#### Woche 22 (Tag 148–154)
**Wochenziel:** Schema implementiert, mit realistischen Testdaten befüllt.
- Mo: DDL schreiben (alle Tabellen inkl. Constraints)
- Di: Indexe auf FKs/häufigen Filterspalten
- Mi: Testdaten generieren (≥500 Zeilen)
- Do: Constraint-Tests (Integrität verifizieren)
- Fr: Interleaving — 5 Validierungsqueries gegen Testdaten
- Sa: Backup/Restore einmal durchführen (`pg_dump`/`pg_restore`)
**Meilenstein:** Schema lauffähig, ≥500 Testzeilen, alle Constraints aktiv und verifiziert.

#### Woche 23 (Tag 155–161)
**Wochenziel:** ≥8 Reporting-Queries (Joins, Aggregation, Window Functions, CTEs).
- Mo: Kern-Reporting-Fragen definieren (8–10 Stück)
- Di: Queries mit Joins + Aggregation
- Mi: Queries mit Window Functions
- Do: Queries mit CTEs (ggf. rekursiv)
- Fr: Interleaving — alle Queries laufen lassen, Ergebnisse plausibilisieren
- Sa: Jede Query mit 1-Satz-Zweck dokumentieren
**Meilenstein:** ≥8 funktionierende, dokumentierte Queries, Ergebnisse verifiziert.

#### Woche 24 (Tag 162–168)
**Wochenziel:** Projekt-Queries performant; Projekt fehlerfrei erklärbar.
- Mo: `EXPLAIN ANALYZE` für alle Reporting-Queries
- Di: Indexe/Umschreibungen für die 2–3 langsamsten Queries
- Mi: Vorher/Nachher dokumentieren
- Do: Großes Interleaving-Review über das gesamte Projekt
- Fr: Feynman — Projekt (Schema + 3 Beispielqueries + 1 Optimierung) komplett erklären
- Sa: Lücken aus der Feynman-Session gezielt nacharbeiten
**Meilenstein:** Feynman-Erklärung beim 3. Versuch fehlerfrei und ohne Nachschlagen.

#### Woche 25 (Tag 169–175) — Generalüberholung
**Wochenziel:** Gesamtwissen aus 180 Tagen abrufbar und verknüpft.
- Mo: Quiz Phase 1 (20 Fragen, erst ohne Unterlagen, dann Fehleranalyse)
- Di: Quiz Phase 2
- Mi: Quiz Phase 3
- Do: Quiz Phase 4
- Fr: Quiz Phase 5
- Sa: Cross-Phase-Mixed-Test (30 Fragen aus allen Phasen, 90 Min Zeitlimit)
**Meilenstein:** Cross-Phase-Test ≥85%; alle 5 Phasentests erneut ≥85 % wiederholt (zeigt Retention).

#### Woche 26 (Tag 176–180) — Abschluss
**Wochenziel:** Externe Validierung der Skills + Portfolio fertig.
- Mo: LeetCode/HackerRank/StrataScratch — 5 Medium-SQL-Aufgaben
- Di: SQL Murder Mystery komplett lösen
- Mi: Projekt-Repo aufräumen, README (Schema-Erklärung, Beispielqueries, Case-Study-Link)
- Do: Self-Assessment — alle Testscores + Cross-Phase-Test dokumentieren, Lückenliste für Erhaltungs-Reviews
- Fr: Plan für Erhaltung danach (z. B. monatlicher Spaced-Repetition-Review-Tag)
**Meilenstein:** Portfolio fertig (Schema + ≥8 Queries + 1 Case-Study); ≥4/5 Medium-Aufgaben gelöst; SQL Murder Mystery gelöst.

---

## 6. Abschlusskriterien Tag 180

- [ ] Alle 5 Phasentests bestanden (≥85 %), Phase-1–5-Tests in Woche 25 erneut ≥85 % bestanden
- [ ] Eigenes Datenbankprojekt: ≥8 Tabellen, 3NF, ≥500 Testzeilen, ≥8 dokumentierte Reporting-Queries
- [ ] Mindestens 1 dokumentierte Performance-Optimierung mit Vorher/Nachher-Zahlen
- [ ] Mindestens 1 funktionierender Trigger, 1 View, 1 Function/Procedure im eigenen Schema
- [ ] Security-Review-Dokument (SQL-Injection-Beispiel + Rollen/Rechte) erstellt
- [ ] SQL Murder Mystery gelöst, ≥4/5 externe Medium-Aufgaben gelöst
- [ ] Anki-Deck mit allen Konzepten, Retention-Rate laut Anki-Statistik ≥85 %
