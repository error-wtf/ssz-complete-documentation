# SSZ Book Consolidation Plan: EN ↔ DE

**Status:** ACTIVE
**Stand:** 2026-02-24
**Ziel:** Beide Bücher inhaltlich 100% identisch machen, nur Sprache/Präsentation unterschiedlich

---

## 1. Grundprinzipien

| Prinzip | Umsetzung |
|---------|-----------|
| 1:1-Inhaltsgleichheit | Jeder Absatz, jede Formel, jede Tabelle identisch |
| Terminologische Konsistenz | Einheitliche Übersetzung aller Fachbegriffe (keine Synonyme) |
| Formeln unverändert | Punkt als Dezimaltrennzeichen in beiden Versionen (0.555) |
| Struktur identisch | Kapitelnummern, Abbildungsnummern, Gleichungsnummern exakt gleich |
| Kulturelle Anpassungen | Nur wo nötig (Literatur), keine inhaltlichen Änderungen |

---

## 2. Notation (vereinheitlicht)

- **Dezimaltrennzeichen:** Punkt (0.555) in beiden Versionen
- **Griechische Buchstaben:** Kursiv (*π*, *φ*, *Ξ*)
- **Vektoren/Tensoren:** Fettgedruckt (**r**, **g**_μν)
- **Indizes:** Konsistent (Ξ_max, D_min, r_s)
- **Formelnummern:** Identisch in EN/DE: (1.1), (1.2), ...
- **Abbildungen:** EN: Fig. X.Y / DE: Abb. X.Y — gleiche Nummerierung
- **Querverweise:** EN: Chapter X.Y / DE: Kapitel X.Y

---

## 3. Zehn Konsolidierungsschritte

### 3.1 Mathematische Notation vereinheitlichen
- Global Punkt als Dezimaltrennzeichen
- Einheitliche Symbolschreibweise (kursiv, fett)
- Formelnummern 1:1

### 3.2 Pädagogische Tiefe angleichen
- "Pedagogical Note"-Boxen in beiden Versionen
- Analogien beibehalten mit expliziten Einschränkungen
- EN: Kompakt + optional Box / DE: Ausführlich + optional Box

### 3.3 Querverweise und Literatur vereinheitlichen
- Primär englische Standardwerke, deutsche Alternativen in Fußnoten
- Querverweise: EN "Chapter X.Y" / DE "Kapitel X.Y"

### 3.4 Abbildungen konsistent
- Farbcodierung: g₁=grün, Übergang=gelb, g₂=rot
- EN-Beschriftungen als Standard, DE-Legende

### 3.5 Code-Referenzen angleichen
- GitHub-Links in beiden Büchern identisch
- DE: zusätzliche Erklärungen für Nicht-Programmierer

### 3.6 Key-Formulas-Tabellen standardisieren
- Einheitliches Format: Symbol | Formel | Gültigkeitsbereich | Referenz

### 3.7 Anhänge konsistent
- A (Symbole): EN-Symbole + DE-Entsprechungen
- D (Repos): Identische Links + DE-Einführung
- F (GR vs SSZ): 1:1 übersetzt

### 3.8 Falsifizierbare Vorhersagen (Kap. 30/32) — Master-Tabelle
- Eine gemeinsame Tabelle, identisch in beiden Büchern

### 3.9 Sprachliche Konsolidierung
- Fachbegriffe immer englisch belassen (PPN, nicht "PPN-Kennwert")
- DE: Englische Fachbegriffe kursiv + deutsche Erklärung beim ersten Auftreten
- Keine wörtlichen Übersetzungen von Idiomen

### 3.10 Automatisierte Konsistenzprüfung
- check_consistency.py: Formeln, Fachbegriffe, Querverweise
- translation_db.csv: Übersetzungsdatenbank
- GitHub-Action für Synchronisation (optional)

---

## 4. Übersetzungsdatenbank

Datei: `BOOKS/translation_db.csv`
Format: `en_term,de_term,notes`

---

## 5. Konsistenzprüfungs-Skript

Datei: `BOOKS/check_consistency.py`
Prüft:
1. Alle Formeln in EN/DE identisch
2. Alle Fachbegriffe konsistent übersetzt
3. Alle Querverweise übereinstimmend
4. Dezimaltrennzeichen einheitlich

---

## 6. Repo-Struktur (Ziel)

```
BOOKS/
├── SSZ_BOOK_EN.pdf
├── SSZ_BOOK_DE.pdf
├── SSZ_COMPLETE_BOOK_EN.md
├── SSZ_COMPLETE_BOOK_DE.md
├── 01_segments_index.md
├── BOOK_COMPARISON.md
├── BOOK_CONSOLIDATION_PLAN.md    ← dieses Dokument
├── translation_db.csv
└── check_consistency.py
```

---

## 7. Empfehlung nach Zielgruppe

| Leser | Version | Begründung |
|-------|---------|------------|
| Deutsche Studierende | DE | Didaktisch, vertraute Sprache |
| Internationale Forscher | EN | Kompakt, technische Details |
| Lehrende (D/A/CH) | DE | Anpassung an Lehrpläne |
| Entwickler (Code/Tests) | EN | Repos auf Englisch |
| Allgemein Interessierte | DE | Zugänglicher |

---

## 8. Zeitplan

| Schritt | Status |
|---------|--------|
| Konsolidierungsplan | ✅ Erstellt |
| Übersetzungsdatenbank | ✅ Erstellt |
| Konsistenzprüfungs-Skript | ✅ Erstellt |
| Pilotkapitel konsolidieren | 🔄 In Arbeit |
| Alle Kapitel konsolidieren | ⏳ Ausstehend |
| Testleser einbinden | ⏳ Ausstehend |
| Finale Version | ⏳ Ausstehend |

---

© 2025–2026 Carmen N. Wrede, Lino P. Casu
