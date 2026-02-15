# Regime Definitions & Transitions

---

## Canonical Boundaries (segcalc)

| Regime | r/r_s | Formula | Description |
|--------|-------|---------|-------------|
| very_close | < 1.8 | Ξ = 1-exp(-φ·r_s/r) | Near-horizon |
| blended | 1.8–2.2 | Hermite C² | Transition |
| photon_sphere | 2.2–3.0 | SSZ optimal | Photon ring |
| strong | 3.0–10.0 | SSZ with Δ(M) | Strong field |
| weak | > 10.0 | Ξ = r_s/(2r) | Weak field |

---

## Hermite C² Interpolation

```
t = (r/r_s - 1.8) / 0.4
H₅(t): Quintic Hermite matching value, 1st & 2nd derivatives
```

Properties: C⁰ + C¹ + C² continuous.

---

## g₁ / g₂ Convention

| Symbol | Regime | Characteristics |
|--------|--------|-----------------|
| g₁ | Weak | Ξ ≪ 1, SSZ ≡ GR |
| g₂ | Strong | Ξ → 0.8, SSZ ≠ GR |

Transition g₁ → g₂ is **irreversible** (coherence-collapse, Paper 25).

---

## Common Mistakes

- ❌ Using 90/110 as regime boundaries (those are PROBE_RADII)
- ❌ Skipping the blend zone (creates curvature discontinuities)
- ❌ Applying Δ(M) in weak field (weak field = exact GR)
