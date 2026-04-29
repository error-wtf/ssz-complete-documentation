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
| GPS gravitational drift | 45.9 μs/day | 45.9 μs/day | ✅ PASS |
| GPS net drift (GR − SR) | 38.4 μs/day | 38.7 μs/day | ✅ PASS (<1%) |
| Pound-Rebka | Δν/ν = 2.46×10⁻¹⁵ | 2.46×10⁻¹⁵ | ✅ PASS |
| Mercury perihelion | 43.1″/century | 42.99″/century | ✅ PASS |
| Eddington lensing | 1.75″ | 1.75″ (PPN) | ✅ PASS |
| Cassini Shapiro | γ = 1.000021±0.000023 | γ = 1 (exact) | ✅ PASS |
| S2 star redshift | z = 0.00198 | 0.00198 | ✅ PASS |

### 2. Strong-Field Predictions (SSZ ≠ GR)

| Prediction | GR Value | SSZ Value | Testable? |
|-----------|----------|-----------|----------|
| NS redshift excess | z_GR | z_GR + 13% | NICER (2025–2027) |
| Shapiro strong-field | Δt_GR | Δt_GR + 12% | SKA (2028+) |
| BH shadow diameter | d_GR | d_GR − 1.3% | ngEHT (2028–2030) |
| D(r_s) | 0 (singularity) | **0.55503** (finite) | Indirect (LISA 2034+) |
| Pulsar timing | Δt_GR | Δt_GR + 30% | NANOGrav (2025–2028) |

### 3. Internal Consistency

| Check | What it verifies | Status |
|-------|-----------------|--------|
| C² continuity at blend | Ξ, dΞ/dr, d²Ξ/dr² match | ✅ |
| r* intersection | Ξ_weak(r*) = Ξ_strong(r*) → r*/r_s = 1.387 | ✅ |
| Asymptotic flatness | D → 1 as r → ∞ | ✅ |
| PPN recovery | β = γ = 1 in weak field | ✅ |
| Energy conditions | WEC, DEC, SEC for r ≥ 5r_s | ✅ |

---

## Test Infrastructure

### Canonical Runner

```bash
git clone https://github.com/error-wtf/ssz-all-tests
cd ssz-all-tests
python run_all_live.py
```

Runs all 12 active repos, generates structured output files.

### Live Test Counts (2026-04-29)

| Repository | Tests | Passed | Status | Focus |
|-----------|-------|--------|--------|-------|
| ssz-qubits | 184 | 184 | ✅ 100% | GPS, Pound-Rebka, S2, qubits |
| ssz-lensing | 279 | 279 | ✅ 100% | Gravitational lensing |
| ssz-trajectories | 63 | 63 | ✅ 100% | Geodesic integration |
| frequency-curvature-validation | 82 | 82 | ✅ 100% | PPN, Shapiro, Cassini |
| ssz-lagrange | 54 | 54 | ✅ 100% | Lagrange/Hamilton |
| chord-partition (local) | 103 | 103 | ✅ 100% | Eigenmodes, φ resonance |
| ssz-metric-pure | 36 | 36 | ✅ 100% | 4D tensors, Einstein eq. |
| ssz-schumann | 178 | 178 | ✅ 100% | Schumann resonance |
| segmented-calculation-suite | 158 | 158 | ✅ 100% | Core Ξ/D/regime |
| Unified-Results | 147 | 147 | ✅ 100% | 25 test suites |
| segmented-energy | 7 | 7 | ✅ 100% | 129 astronomical objects |
| g79-cygnus-tests | 5 | 5 | ✅ 100% | G79 LBV nebula |
| **TOTAL** | **1,296** | **1,296** | **✅ 100%** | |

### Reproducibility

- All repos public on GitHub (`github.com/error-wtf`)
- Python 3.10+ with numpy, scipy, matplotlib, pytest
- Canonical runner: `ssz-all-tests/run_all_live.py`
- Live status: `ssz-all-tests/LIVE_STATUS.json`

---

## Method Assignment in Tests

**CRITICAL:** Tests must use the correct method for each observable:

| Observable | Geodesic type | Method | Note |
|-----------|--------------|--------|------|
| Time dilation | time-like (static) | Ξ-based | D = 1/(1+Ξ) |
| Redshift | time-like (static) | Ξ-based | z = Ξ |
| Lensing | null (ds²=0) | PPN (1+γ) | α = (1+γ)r_s/b |
| Shapiro | null (ds²=0) | PPN (1+γ) | Δt = (1+γ)Δt_Ξ |
| Perihelion | massive orbit | PPN (β,γ) | standard |

> Using Ξ-only for null observables gives 50% of GR — this is NOT a bug, it is the g_tt-only contribution. PPN applies the full (g_tt + g_rr) factor.

**Mnemonic:** Clocks → Ξ. Light → PPN. Orbits → PPN.

---

© 2025–2026 Carmen N. Wrede, Lino P. Casu
