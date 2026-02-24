# Regime Definitions

**Status:** CANONICAL

---

## Overview

SSZ defines five regimes based on the ratio r/r_s (distance to Schwarzschild radius):

| Regime | r/r_s range | Ξ formula | Physical context |
|--------|------------|-----------|------------------|
| **very_close** | < 1.8 | Ξ_strong = min(1-exp(-φr/r_s), Ξ_max) | At/near horizon |
| **blended** | 1.8–2.2 | Hermite C² interpolation | Smooth transition |
| **photon_sphere** | 2.2–3.0 | Ξ_strong | Photon orbit zone |
| **strong** | 3.0–10.0 | Ξ_strong | Neutron stars, compact objects |
| **weak** | > 10.0 | Ξ_weak = r_s/(2r) | Solar System, GPS, stars |

---

## Regime Check (MANDATORY)

**Before using any Ξ formula, determine regime via r/r_s.**

The wrong formula in the wrong regime produces incorrect results. This is the most common source of apparent contradictions in SSZ.

```python
def get_regime(r, r_s):
    ratio = r / r_s
    if ratio < 1.8:
        return 'very_close'   # Ξ_strong
    elif ratio <= 2.2:
        return 'blended'      # Hermite C²
    elif ratio <= 3.0:
        return 'photon_sphere' # Ξ_strong
    elif ratio <= 10.0:
        return 'strong'       # Ξ_strong
    else:
        return 'weak'         # Ξ_weak
```

---

## Regime Transition: The Blend Zone

The transition between Ξ_weak and Ξ_strong is NOT a discontinuity. It uses Hermite C² interpolation:

```
t = (r/r_s - 1.8) / 0.4      (normalized: 0 at r/r_s=1.8, 1 at r/r_s=2.2)
Ξ_blend = H₅(t)               (quintic Hermite polynomial)
```

This guarantees:
- **C⁰ continuity:** Ξ matches at both boundaries
- **C¹ continuity:** dΞ/dr matches at both boundaries
- **C² continuity:** d²Ξ/dr² matches at both boundaries

**Never mix formulas without an explicit blend rule.**

---

## Irreversible Coherence-Collapse: g₁ → g₂

The transition from weak (g₁) to strong (g₂) is **unidirectional**:

```
g₁ → g₂: Irreversible
g₂ → g₁: FORBIDDEN
```

This is a fundamental postulate, not a computational convenience. Once spacetime enters the strong-field segmentation regime, it does not spontaneously return to weak-field behavior.

---

## IMPORTANT: 90/110 vs 1.8/2.2

Some repositories use r/r_s = 90–110 as boundaries. **These are NOT regime boundaries!**

They are **probe radii** (test sampling points) for continuity checks in `unified_validation.py`. The actual physical regime boundaries are at r/r_s = 1.8 and 2.2.

---

## Typical Ξ Values per Regime

| Regime | Ξ range | Example objects |
|--------|---------|----------------|
| very_close | 0.5–0.802 | Horizon, near-BH |
| blended | 0.22–0.5 | Compact NS, r* zone |
| photon_sphere | 0.13–0.22 | Photon orbits |
| strong | 0.05–0.13 | Outer NS envelope |
| weak | < 0.05 | Everything in Solar System |

---

## Cross-References

- Segment density: `02_FOUNDATIONS/segment_density.md`
- Hermite details: `03_FORMULAS/formula_compendium.md` §B.2
- Test: `test_regime_definitions.py` in segmented-calculation-suite

---

© 2025–2026 Carmen N. Wrede, Lino P. Casu
