# Segmented Spacetime (SSZ) — Complete Documentation

**Authors:** Carmen N. Wrede, Lino P. Casu
**AI Assistants:** Bingsi, Akira
**Status:** Canonical Reference — Single Source of Truth
**Last Updated:** 2026-02-20

---

## What is SSZ?

Segmented Spacetime (SSZ) is a falsifiable extension of General Relativity (GR) built around a single additional quantity: a **dimensionless segment density field Ξ(r)**. SSZ reproduces GR exactly in weak fields while producing systematic, testable deviations in strong fields — especially around neutron stars and compact objects.

**Core equation:**
```
D_SSZ(r) = 1 / (1 + Ξ(r))
```

At the Schwarzschild radius: **D(r_s) = 0.555** (finite!) vs GR: D(r_s) = 0 (singularity).

---

## Documentation Structure

| # | Section | Contents |
|---|---------|----------|
| 01 | [Overview](01_OVERVIEW/) | What is SSZ, core postulates, relation to GR |
| 02 | [Foundations](02_FOUNDATIONS/) | Ξ(r), D(r), regimes, φ-geometry |
| 03 | [Formulas](03_FORMULAS/) | Complete formula compendium, symbol table, quick reference |
| 04 | [Kinematics](04_KINEMATICS/) | Dual velocities, Lorentz v=0, kinematic closure |
| 05 | [Electromagnetism](05_ELECTROMAGNETISM/) | Maxwell gauge, rotating space, group velocity, redshift |
| 06 | [Strong Field](06_STRONG_FIELD/) | BH metric, singularities, cosmic censorship, dark star |
| 07 | [Validation](07_VALIDATION/) | Test methodology, cross-repo results, GR vs SSZ tables |
| 08 | [Falsification](08_FALSIFICATION/) | Testable predictions, instruments, falsification criteria |
| 09 | [Papers](09_PAPERS/) | All 25 papers, bibliography, preprints |
| 10 | [Repositories](10_REPOSITORIES/) | All 35 repos, test index, reproducibility |
| 11 | [Guardrails](11_GUARDRAILS/) | Prime directive, method assignment, confusion prevention |
| 12 | [Glossary](12_GLOSSARY/) | EN/DE terminology |

---

## Key Numbers

| Metric | Value |
|--------|-------|
| Papers | 25 primary + 7 additional |
| Repositories | 35 total (17 SSZ, 2 math, 3 research, 3 tools, 8 web, 2 private) |
| Tests | 747+ validated, 200+ test files |
| Documentation files | 1,803+ across all repos |
| Consistency checks | 171/171 PASS |
| Book chapters | 32 (9 parts + appendices A–G) |
| Book (EN) | 445 pages, 4.8 MB ([PDF](BOOKS/SSZ_BOOK_EN.pdf)) |
| Book (DE) | 549 pages, 4.9 MB ([PDF](BOOKS/SSZ_BOOK_DE.pdf)) |

---

## Quick Start

1. **New to SSZ?** → Start with [01_OVERVIEW/ssz_overview.md](01_OVERVIEW/ssz_overview.md)
2. **Need formulas?** → Go to [03_FORMULAS/formula_compendium.md](03_FORMULAS/formula_compendium.md)
3. **Quick card** → See [03_FORMULAS/quick_reference.md](03_FORMULAS/quick_reference.md)
4. **Method selection** → Read [11_GUARDRAILS/prime_directive.md](11_GUARDRAILS/prime_directive.md)
5. **Validation data** → Check [07_VALIDATION/gr_vs_ssz_tables.md](07_VALIDATION/gr_vs_ssz_tables.md)
6. **Reproduce results** → Follow [10_REPOSITORIES/reproducibility.md](10_REPOSITORIES/reproducibility.md)

---

## The SSZ Mantra

> **Observable → Class → Method → Scope → Then calculate.**

| Observable Type | Method | Formula |
|----------------|--------|---------|
| Timelike (clocks) | Ξ-based | D = 1/(1+Ξ) |
| Null (light) | PPN (1+γ) | α = 2r_s/b |
| Orbit (precession) | PPN (β,γ) | Standard PPN |

---

## Books

The complete SSZ monograph is available in two languages and two formats:

| Edition | Format | Size | File |
|---------|--------|------|------|
| **English** | PDF | 4.8 MB | [SSZ_BOOK_EN.pdf](BOOKS/SSZ_BOOK_EN.pdf) |
| **English** | Markdown | 970 KB | [SSZ_COMPLETE_BOOK_EN.md](BOOKS/SSZ_COMPLETE_BOOK_EN.md) |
| **German** | PDF | 4.9 MB | [SSZ_BOOK_DE.pdf](BOOKS/SSZ_BOOK_DE.pdf) |
| **German** | Markdown | 1.1 MB | [SSZ_COMPLETE_BOOK_DE.md](BOOKS/SSZ_COMPLETE_BOOK_DE.md) |

**Structure (9 Parts, 32 Chapters + 7 Appendices):**

| Part | EN | DE |
|------|----|----|
| I | Foundations | Grundlagen |
| II | Kinematics | Kinematik |
| III | Electromagnetism and Light Propagation | Elektromagnetismus und Lichtausbreitung |
| IV | Frequency Framework and Curvature Detection | Frequenz-Rahmenwerk und Krümmungsdetektion |
| **V** | **Action Principle and Extended Formalism** | **Wirkungsprinzip und erweiterter Formalismus** |
| VI | Strong-Field Objects | Starke-Feld-Objekte |
| VII | Astrophysical Applications | Astrophysikalische Anwendungen |
| VIII | Regime Transitions | Regimeübergänge |
| IX | Validation and Reproducibility | Validierung und Reproduzierbarkeit |

**New in v2 (2026-02-20):** Part V — Lagrangian/Hamiltonian formulation, rotating metrics, quantum corrections, and numerical relativity (Chapters 31–32).

---

## License

This project is licensed under the **Anti-Capitalist Software License v1.4**.

See [LICENSE.md](LICENSE.md) for the full license text.

**Core Principle:** Science should serve humanity, not profit.

### You are free to:
- Use, study, share, and modify this documentation for personal, educational, or non-profit purposes
- Publish scientific results based on this documentation (with attribution)

### You may not:
- Use this documentation for commercial purposes or in the service of capitalist enterprises
- Use this documentation in military, surveillance, or law enforcement contexts
- Incorporate this documentation into closed-source commercial products

### Citation

If you use this documentation in scientific work, please cite:

```bibtex
@misc{wrede2026sszdocs,
  title={Segmented Spacetime (SSZ) -- Complete Documentation},
  author={Wrede, Carmen N. and Casu, Lino P.},
  year={2026},
  note={Available at https://github.com/error-wtf/ssz-complete-documentation}
}
```

© 2025–2026 Carmen N. Wrede, Lino P. Casu
