# Regime Boundaries vs. Formula Domains — Canonical Clarification

**Status:** CANONICAL

---

## The Two Boundary Systems

SSZ uses two distinct boundary systems that must not be conflated:

### System 1: Formula Domains (Operative N-Segmentation Mapping)

These boundaries determine **which formula** is used to compute Ξ:

| Domain | r/rₛ | Formula |
|--------|-------|---------|
| g₁ domain | > 2.2 | Ξ = rₛ/(2r) |
| Blend zone | 1.8–2.2 | Hermite C² interpolation |
| g₂ domain | < 1.8 | Ξ = min(1−exp(−φr/rₛ), Ξ_max) |

### System 2: Physical Regimes (Interpretive Classification)

These boundaries classify the **physical environment**:

| Regime | r/rₛ | Physical context |
|--------|-------|-----------------|
| very_close | < 1.8 | At/near horizon |
| blended | 1.8–2.2 | Smooth transition |
| photon_sphere | 2.2–3.0 | Photon orbit zone |
| strong | 3.0–10.0 | Neutron stars, compact objects |
| weak | > 10.0 | Solar System, GPS, stars |

### The Key Difference

In the range 2.2 < r/rₛ < 10, the g₁ formula is used operatively,
but the physical regime is "strong" or "photon_sphere".

"g₁ formula for x > 2.2" does NOT mean "everything above 2.2 is weak field".
It means: "For computing Ξ, the g₁ branch is used above 2.2 because it
provides the physically correct approximation there."

---

## Numerical Evidence

| r/rₛ | Ξ_g1 | Ξ_g2 | Ξ operative | D operative | Regime | Formula | |g1−g2| |
|-------|------|------|-------------|------------|--------|---------|--------|
| 0.5 | 1.000000 | 0.554704 | 0.554704 | 0.643209 | very_close | g2 | 0.445296 |
| 1.0 | 0.500000 | 0.801712 | 0.801712 | 0.555028 | very_close | g2 | 0.301712 |
| 1.8 | 0.277778 | 0.801712 | 0.277778 | 0.782609 | blended | blend | 0.523934 |
| 2.2 | 0.227273 | 0.801712 | 0.801712 | 0.555028 | blended | blend | 0.574439 |
| 3.0 | 0.166667 | 0.801712 | 0.166667 | 0.857143 | photon_sphere | g1 | 0.635045 |
| 5.0 | 0.100000 | 0.801712 | 0.100000 | 0.909091 | strong | g1 | 0.701712 |
| 10.0 | 0.050000 | 0.801712 | 0.050000 | 0.952381 | strong | g1 | 0.751712 |
| 100.0 | 0.005000 | 0.801712 | 0.005000 | 0.995025 | weak | g1 | 0.796712 |

The |g1−g2| column proves that choosing the wrong formula produces catastrophic errors.
At r = rₛ: g1 would give D = 0.667 instead of the correct D = 0.555 (17% error).

---

## Saturation Form vs. Decay Form

| | Saturation (φr/rₛ) | Decay (φrₛ/r) |
|---|---|---|
| r → 0 | Ξ → 0 (regular) | Ξ → 1 (saturates) |
| r → ∞ | Ξ → Ξ_max (saturates) | Ξ → 0 (decays) |
| r = rₛ | Ξ = 0.802 | Ξ = 0.802 |
| Status | **OPERATIVE** | Didactic only |

The saturation form is canonical. The decay form is retained for pedagogical contrast only.

---

## Common Misunderstandings

1. **Ξ = rₛ/(r−rₛ) is NOT canonical.** It gives D(rₛ)=0, contradicting D_min=0.555. FORBIDDEN.
2. **"Above 2.2 = weak field" is WRONG.** Formula domain ≠ physical regime.
3. **The blend zone is NOT a numerical trick.** It is the unique C² interpolant.
4. **Lensing/Shapiro do NOT use Ξ.** They use PPN with γ=1.
5. **Coherence collapse is g₁→g₂ (irreversible).** NOT g₂→g₁.
6. **90/110 are probe radii, NOT regime boundaries.**

---

## Cross-References

- Segment density: `02_FOUNDATIONS/segment_density.md`
- Regime definitions: `02_FOUNDATIONS/regime_definitions.md`
- Formula compendium: `03_FORMULAS/formula_compendium.md`
- Forbidden formulas: `03_FORMULAS/forbidden_formulas.md`

---

© 2025–2026 Carmen N. Wrede, Lino P. Casu
