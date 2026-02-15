# Segmented Spacetime (SSZ) — Overview

**Authors:** Carmen N. Wrede, Lino P. Casu

---

## What is Segmented Spacetime?

Segmented Spacetime (SSZ) is a falsifiable extension of General Relativity (GR) built around a single additional, operational quantity: a **dimensionless segment density field Ξ(r)**. The intuitive idea is that spacetime can become "more segmented" in regions of strong gravitational influence, and that this segmentation manifests observationally as modified time dilation and related strong-field effects.

SSZ is designed to behave like GR in the weak field while producing systematic, testable deviations in the strong field — especially around neutron stars and near compact-object regimes.

---

## Core Postulate: A Minimal Time Dilation Law

```
D_SSZ(r) = 1 / (1 + Ξ(r))    ⟹    dτ = D_SSZ · dt
```

Here:
- **t** is coordinate time
- **τ** is local proper time measured by a physical clock
- **Ξ(r)** is the segment density, given by explicit regime formulas

Ξ is **not** a free per-object parameter. It must be given by explicit formulas tied to mass, radius, and regime classification.

---

## Two Regimes

### g₁ (Weak Field) — r/r_s > 10
```
Ξ_weak(r) = r_s / (2r)
D_SSZ ≈ 1 - Ξ + O(Ξ²)
```
Recovers GR to high accuracy.

### g₂ (Strong Field) — r/r_s < 1.8
```
Ξ_strong(r) = 1 - exp(-φ · r_s / r)
Ξ_max = Ξ(r_s) = 1 - exp(-φ) ≈ 0.802
```
Saturation principle: segmentation cannot diverge. Yields D_min = 0.555 (finite!).

### Blend Zone — 1.8 ≤ r/r_s ≤ 2.2
Quintic Hermite C² interpolation for smooth, curvature-continuous transition.

---

## φ-Geometry

The golden ratio φ = (1+√5)/2 enters as a structural scaling constant:
- Strong-field formula: exp(-φ · r_s/r)
- Coupling radius: r_φ = (φ/2) · r_s · [1 + β · Δ(M)]
- Saturation value: Ξ(r_s) = 1 - e^(-φ) ≈ 0.802

φ is a constraint reducing arbitrariness, not decorative numerology.

---

## "No Free Parameters" Discipline

- Don't curve-fit, don't add knobs
- Derive Ξ(r) from regime formulas with fixed constants
- Or treat Ξ as explicit input and immediately run falsification tests
- Test harness approach: forward calculator returning predicted deviations

---

## What SSZ Explains

1. **Time dilation / gravitational redshift** in strong fields
2. **Energy-related observables** under strong segmentation
3. **Systematic offsets** vs GR, small in weak fields, non-negligible at high compactness

---

## How SSZ Relates to GR

- GR provides curvature that works extremely well
- SSZ keeps GR in weak fields
- SSZ adds Ξ whose primary footprint is modified time dilation saturating in strong fields
- Not "anti-GR" — rather **"GR + structured strong-field correction"**

---

## Falsifiability Targets

| Test | SSZ Prediction | Instrument | Timeline |
|------|---------------|------------|----------|
| NS surface redshift | +13% vs GR | NICER, XMM-Newton | 2025–2027 |
| Pulsar timing | +30% vs GR | NANOGrav, SKA | 2025–2028 |
| BH shadow diameter | -1.3% vs GR | ngEHT | 2028–2030 |
| Universal intersection | r*/r_s = 1.595 | Multi-NS comparison | 2027+ |

If SSZ can be "killed" quickly by a clean counterexample, it should be. Quick rejection is a feature, not a bug.
