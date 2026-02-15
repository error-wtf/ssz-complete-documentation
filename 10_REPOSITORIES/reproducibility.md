# Reproducibility Guide

---

## Requirements

- **Python:** 3.10+
- **Packages:** numpy, scipy, matplotlib
- **Optional:** sympy (for symbolic computation in ssz-metric-pure)

---

## Quick Start

```bash
# Clone any repository
git clone https://github.com/error-wtf/<repo-name>.git
cd <repo-name>

# Install dependencies
pip install numpy scipy matplotlib

# Run tests
python -m pytest tests/ -v
```

---

## Key Repositories to Start With

1. **segmented-calculation-suite** — Core formulas and regime logic
2. **ssz-qubits** — Real-data validation (GPS, Pound-Rebka, S2)
3. **frequency-curvature-validation** — PPN tests (Shapiro, lensing)
4. **ssz-metric-pure** — 4D tensor formulation

---

## Automated Test Runner

```powershell
# PowerShell (Windows)
.\run_consistency_suite.ps1
```

---

## Symbolic Computation (ssz-metric-pure)

3 modes:
- **complete:** 10–30 min (full proofs)
- **fast:** 1–3 min (key results)
- **sparse:** 1–2 min (minimal check)

---

## Anti-Circularity Verification

To verify that no circular dependencies exist:
```bash
cd segmented-calculation-suite
python -m pytest tests/test_anti_circularity.py -v
```

This test verifies the acyclic dependency graph (Level 0→5).

---

## Data Sources (External)

All validation data comes from published external sources:
- GPS timing: BIPM/US Naval Observatory
- Pound-Rebka: Pound & Rebka (1960)
- S2 star: ESO/GRAVITY Collaboration
- Neutron stars: NASA/NICER
- BH shadow: EHT Collaboration

None of this data was used for SSZ calibration (anti-circularity).
