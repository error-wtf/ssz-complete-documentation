# SSZ Predictions

**Status:** CANONICAL

---

## Category 1: Confirmed Predictions (SSZ ≡ GR)

SSZ reproduces all confirmed GR weak-field results:

| Prediction | Value | Confirmed by |
|-----------|-------|--------------|
| GPS gravitational drift | 45.9 μs/day | US Naval Observatory |
| GPS net drift (GR − SR) | 38.4 μs/day | GPS operational data |
| Pound-Rebka redshift | Δν/ν = 2.46×10⁻¹⁵ | Pound & Rebka (1960) |
| Mercury perihelion | 42.99″/century | Planetary observations |
| Eddington lensing | 1.75″ | Eddington (1919) |
| Cassini Shapiro γ | 1.000021 ± 0.000023 | Bertotti et al. (2003) |
| S2 star redshift | z = 0.00198 | GRAVITY/ESO (2018, 2021) |
| S2 Schwarzschild precession | Confirmed | GRAVITY/ESO (2020) |
| G79.29+0.46 (6/6 predictions) | Confirmed | g79-cygnus-tests |

---

## Category 2: Testable Predictions (SSZ ≠ GR)

### Neutron Star Redshift (+13%)
```
z_SSZ = z_GR × 1.13  (systematic excess in strong field)
```

Specific objects:

| Object | z_GR | z_SSZ | Testable with |
|--------|------|-------|---------------|
| PSR J0030+0451 | 0.219 | 0.247 | NICER |
| PSR J0740+6620 | 0.346 | 0.391 | NICER |
| PSR J0348+0432 | 0.380 | 0.429 | XMM-Newton |

**Timeline:** 2025–2027 (NICER/ATHENA data releases)

---

### Pulsar Timing Delay (+30%)
```
Δt_SSZ = Δt_GR × 1.30  (strong-field Shapiro enhancement)
```
**Timeline:** 2025–2028 (NANOGrav/SKA)

---

### Black Hole Shadow (−1.3%)
```
d_SSZ = d_GR × 0.987  (slightly smaller shadow)
```
**Timeline:** 2028–2030 (next-generation EHT / ngEHT)

---

### Shapiro Delay Strong-Field (+12%)
```
Δt_SSZ = Δt_GR × 1.12  (near compact objects)
```
**Timeline:** 2028+ (SKA)

---

### QNM Frequency Shift (+3%)
```
f_QNM_SSZ / f_QNM_GR = 1.39  (ringdown frequency)
```
Connected to φ-lattice: f_SSZ/f_GR links to Ξ_max.
**Timeline:** 2025–2035 (LIGO A+, Einstein Telescope)

---

### Finite Horizon Values
```
D(r_s) = 0.55503  (not 0 — singularity-free)
Ξ(r_s) = 0.80171  (not ∞)
```
**Timeline:** Indirect, via gravitational wave ringdown (LISA, 2034+)

---

## Key Structural Constants (Non-Predictions — Derived)

| Constant | Value | Meaning |
|----------|-------|---------|
| r*/r_s | **1.387** | Regime intersection (Ξ_weak = Ξ_strong) — mass-independent |
| r_ph/r_s | **1.595** | Photon sphere radius — **distinct from r***! |
| Ξ_max | **0.80171** | 1 − e^−φ |
| D_min | **0.55503** | 1/(1+Ξ_max) |

> ⚠️ r*/r_s = 1.387 and r_ph/r_s = 1.595 are **two different quantities**. r* is where Ξ_weak = Ξ_strong (regime boundary). r_ph is the photon orbit radius.

---

## Category 3: Specific Object Predictions

### G79.29+0.46 LBV Nebula (6/6 Confirmed)

| Prediction | Value | Status |
|------------|-------|--------|
| Core mass | 8.7 M☉ | ✅ Confirmed |
| Velocity excess | ~15 km/s | ✅ Confirmed |
| Radio redshift | Observable | ✅ Confirmed |
| Recoupling energy | 150 K | ✅ Confirmed |
| Shell positions | 1.2, 2.3, 4.5 pc | ✅ Confirmed |
| NH₃ stability | Molecular consistency | ✅ Confirmed |

Repository: [g79-cygnus-tests](https://github.com/error-wtf/g79-cygnus-tests)

### ESO Spectroscopy (46/47 Cases)
- S-Stars (Sgr A*): S2, S38, S55
- White Dwarfs: Sirius B, Procyon B, 40 Eri B
- Neutron Stars: PSR J0740+6620, PSR J0348+0432
- **97.9% accuracy** vs GR (p < 0.0001)

### Universal Power Law (64/64 Stellar Systems)
```
E_obs/E_rest = 1 + 0.32·(r_s/R)^0.98   [R² = 0.997]
```

---

## Falsification Criteria

SSZ is **falsified** if any of the following are observed at sufficient precision:

| Observation | SSZ Prediction | Falsification if... |
|------------|----------------|---------------------|
| NS surface redshift | +13% vs GR | excess < 5% or > 25% |
| Pulsar timing correction | +30% | deviation < 10% or > 60% |
| BH shadow | −1.3% vs GR | no deficit detected at ngEHT precision |
| r*/r_s | 1.387 (mass-independent) | mass-dependent or ≠ 1.387 ± 0.01 |
| D(r_s) | 0.55503 (finite) | zero or divergent |

---

© 2025–2026 Carmen N. Wrede, Lino P. Casu
