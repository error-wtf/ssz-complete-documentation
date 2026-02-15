# Additive Light-Travel Time Decomposition

**Paper:** 23 (Additive Decomposition of the Observed Light-Travel Time)

---

## Decomposition

```
Δt_total = Δt_flat + Δt_grav
```

The observed light-travel time splits into:
- **Δt_flat:** travel time in flat spacetime (= distance/c)
- **Δt_grav:** gravitational contribution from segmentation

---

## Gravitational Contribution

```
Δt_grav = ∫ (s(r) - 1) dr/c = ∫ Ξ(r) dr/c
```

This integral over the segment density gives the additional time delay due to gravity.

---

## Connection to Shapiro Delay

The Shapiro delay is the round-trip version of this gravitational time contribution, with the PPN correction:

```
Δt_Shapiro = (1 + γ) · (r_s / c) · ln(4 r₁ r₂ / d²)
```

**Important:** One-way delay vs round-trip radar echo (factor 2) is **separate** from the PPN factor (1+γ).

**Test:** `test_travel_time.py`
