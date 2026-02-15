# Test Methodology

**Status:** CANONICAL

---

## Validation Philosophy

SSZ validation follows a **forward-prediction pipeline**:

```
Mass M → r_s → Ξ(r) → D(r) → Observable → Compare to data
```

The chain is one-directional. Reverse inference (observable → Ξ → M) is used only for consistency checks, never for calibration.

---

## Anti-Circularity Principle

SSZ formulas must never be calibrated against the data they predict:

1. Ξ formulas are derived from φ-geometry, not data
2. Regime boundaries are from Ξ_weak = Ξ_strong intersection, not fitting
3. Δ(M) is from φ-geometry, not object-specific tuning
4. No per-object parameter adjustment is allowed

Test: `test_anti_circularity.py` in segmented-calculation-suite

---

## Test Categories

### 1. Weak-Field Validation (SSZ ≡ GR)

SSZ must reproduce all confirmed GR results to measurement precision.

| Test | Measurement | SSZ Prediction | Status |
|------|-------------|----------------|--------|
| GPS time correction | 45.85 μs/day | 45.85 μs/day | ✅ PASS |
| Pound-Rebka | Δν/ν = 2.46×10⁻¹⁵ | 2.46×10⁻¹⁵ | ✅ PASS |
| Mercury perihelion | 42.98"/century | 42.98"/century | ✅ PASS |
| Eddington lensing | 1.75" | 1.75" (PPN) | ✅ PASS |
| Cassini Shapiro | γ = 1.000021±0.000023 | γ = 1 (exact) | ✅ PASS |
| S2 star redshift | z = 0.00018 | 0.00018 | ✅ PASS |

### 2. Strong-Field Predictions (SSZ ≠ GR)

| Prediction | GR Value | SSZ Value | Testable? |
|-----------|----------|-----------|----------|
| NS redshift excess | z_GR | z_GR + 13% | NICER (2025-2027) |
| Shapiro strong-field | Δt_GR | Δt_GR + 12% | SKA (2028+) |
| BH shadow diameter | d_GR | d_GR - 1.3% | ngEHT (2028-2030) |
| D(r_s) | 0 | 0.555 | Indirect |
| Pulsar timing | Δt_GR | Δt_GR + 30% | NANOGrav (2025-2028) |

### 3. Internal Consistency

| Check | What it verifies | Status |
|-------|-----------------|--------|
| C² continuity at blend | Ξ, dΞ/dr, d²Ξ/dr² | ✅ |
| r* intersection | Ξ_weak(r*) = Ξ_strong(r*) | ✅ |
| Asymptotic flatness | D → 1 as r → ∞ | ✅ |
| PPN recovery | β = γ = 1 in weak field | ✅ |
| Energy conditions | WEC, DEC, SEC for r ≥ 5r_s | ✅ |

---

## Test Infrastructure

### Repositories with Tests

| Repository | # Tests | Focus |
|-----------|---------|-------|
| segmented-calculation-suite | 24 | Core Ξ/D/regime |
| ssz-qubits | 12 | GPS, Pound-Rebka, S2, qubits |
| frequency-curvature-validation | 11 | PPN, Shapiro, lensing |
| ssz-lensing | 23 | Gravitational lensing |
| ssz-metric-pure | 7 | 4D tensors, Einstein eq. |
| ssz-schumann | 12 | Schumann resonance |
| g79-cygnus-tests | 7 | G79 LBV nebula |
| ssz-paper-plots | 6 | Plot consistency |
| Unified-Results | 47 | All 25 test suites |
| Starmaps | 46 | Star map validation |
| **TOTAL** | **195+** | |

### Unified Validation (25 Suites)

The `Unified-Results` repository runs all 25 test suites in 231 seconds:
- 97.9% ESO accuracy
- 31/31 core tests passed
- Full report: `reports/full-output.md`

### Reproducibility

- All repos are public on GitHub (github.com/error-wtf)
- Python 3.10+ with numpy, scipy, matplotlib
- Automated test runner: `run_consistency_suite.ps1`
- Commit hashes documented for exact reproduction

---

## Method Assignment in Tests

**CRITICAL:** Tests must use the correct method for each observable:

| Observable | Method | Test file |
|-----------|--------|-----------|
| Time dilation | Ξ-based | test_time_dilation.py |
| Redshift | Ξ-based | test_redshift.py |
| Lensing | PPN (1+γ) | test_ppn_lensing.py |
| Shapiro | PPN (1+γ) | test_shapiro_delay.py |
| Perihelion | PPN (β,γ) | test_perihelion.py |

Using Ξ-only for null observables gives 50% of GR — this is NOT a bug, it's the g_tt-only contribution.

---

© 2025–2026 Carmen N. Wrede, Lino P. Casu
