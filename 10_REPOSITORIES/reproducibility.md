# Reproducibility Guide

**Status:** CANONICAL

---

## Requirements

- **Python:** 3.10+
- **Core packages:** numpy, scipy, matplotlib, pytest
- **Optional:** astropy, pandas, h5py, tqdm, numba (for some repos)
- **OS:** Windows, Linux, macOS

---

## How to Reproduce — One Command

The canonical entry point is [`ssz-all-tests`](https://github.com/error-wtf/ssz-all-tests):

```bash
git clone https://github.com/error-wtf/ssz-all-tests
cd ssz-all-tests
pip install -r requirements.txt
python setup_and_run.py
```

This automatically:
1. Clones all 13 active SSZ repos into `repos/`
2. Installs all dependencies
3. Runs all tests
4. Generates `full-output.md`, `really-full-output.md`, `analysis-index.json`

Subsequent runs (repos already cloned):
```bash
python setup_and_run.py --skip-clone --skip-install
```

---

## Manual Reproduction (Individual Repos)

```bash
git clone https://github.com/error-wtf/segmented-calculation-suite
git clone https://github.com/error-wtf/ssz-qubits
git clone https://github.com/error-wtf/frequency-curvature-validation
git clone https://github.com/error-wtf/ssz-lensing
git clone https://github.com/error-wtf/ssz-metric-pure
git clone https://github.com/error-wtf/ssz-schumann
git clone https://github.com/error-wtf/g79-cygnus-tests
git clone https://github.com/error-wtf/ssz-paper-plots
git clone https://github.com/error-wtf/segmented-energy
git clone https://github.com/error-wtf/Segmented-Spacetime-Mass-Projection-Unified-Results
git clone https://github.com/error-wtf/ssz-trajectories
git clone https://github.com/error-wtf/ssz-lagrange
```

```bash
pip install numpy scipy matplotlib pytest astropy pandas h5py tqdm numba
```

```bash
# Run individual repos
python -m pytest segmented-calculation-suite/tests/ -v
python -m pytest ssz-qubits/tests/ -v
python -m pytest ssz-lensing/tests/ -v
python -m pytest ssz-trajectories/tests/ -v
python -m pytest frequency-curvature-validation/tests/ -v
python ssz-lagrange/test_lagrange_ssz.py   # custom runner
```

---

## Verify Key Results

After any run, check these canonical values:

```
Ξ_max    = 0.80171  (= 1 − e^−φ)
D_min    = 0.55503  (= 1/(1+Ξ_max))   ← FINITE at r_s, not 0!
r*/r_s   = 1.387    (Ξ_weak = Ξ_strong intersection)
r_ph/r_s = 1.595    (photon sphere — different from r*!)
β = γ    = 1        (PPN)
φ        = 1.6180339887498949
```

> ⚠️ **Do not confuse r*/r_s = 1.387 (regime intersection) with r_ph/r_s = 1.595 (photon sphere).** These are two distinct values with distinct physical meaning.

---

## Validation Levels

| Level | Description | Pass Criteria |
|-------|-------------|---------------|
| L1: Unit | Individual function tests | All assertions pass |
| L2: Integration | Multi-function tests | Consistent results |
| L3: Cross-repo | Same calculation in multiple repos | Values agree to 6 sig. fig. |
| L4: Observational | Comparison to real data | Within measurement error |

---

## Live Test Status (2026-04-29)

| Metric | Value |
|--------|-------|
| Repos tested | 13 |
| Tests passed | 1,125+ |
| Tests failed | 3 (platform-specific, Windows/Python 3.12) |
| Pass rate | 99.7% |
| Runner | `ssz-all-tests/setup_and_run.py` |

---

## Unified Test Suite

The `Unified-Results` repository runs 25 test suites:
- 97.9% ESO accuracy (46/47 cases)
- Full report: `reports/full-output.md`

---

## Commit Hashes

For exact reproduction, each repo's commit hash at validation time is documented in the `ssz-all-tests` `analysis-index.json`.

---

© 2025–2026 Carmen N. Wrede, Lino P. Casu
