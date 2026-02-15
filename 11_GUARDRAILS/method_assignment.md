# Method Assignment Table

---

## When to Use What

| Observable | Method | Formula | Why |
|-----------|--------|---------|-----|
| Time dilation | Ξ | D = 1/(1+Ξ) | Only g_tt component |
| Frequency shift | Ξ | ν_obs = ν_emit × D | Same as time dilation |
| **Light deflection** | **PPN (1+γ)** | α = (1+γ)r_s/b = 2r_s/b | Needs g_tt + g_rr |
| **Shapiro delay** | **PPN (1+γ)** | Δt = (1+γ)Δt_Ξ | Needs g_tt + g_rr |
| Perihelion precession | PPN | Standard formula | Standard PPN |

---

## Why the "Factor 2"?

```
Ξ-integration captures only g_tt (temporal component)
PPN captures g_tt + g_rr (temporal + spatial)

α_total = α_tt + α_rr = r_s/b + r_s/b = 2r_s/b ✓
```

Getting 50% of GR for a null observable means you used Ξ-only instead of PPN. This is the expected g_tt-only result, not a bug.

---

## PPN Parameters in SSZ

```
γ = 1 (exact in weak field)
β = 1 (exact)
```

These are exact, not approximations.

---

## Shapiro: One-Way vs Round-Trip

Always distinguish:
- **One-way signal delay** vs **Round-trip radar echo** (extra factor 2)
- This is **separate from** the PPN (1+γ) factor
- Never conflate them

---

## Energy Accounting

**NEVER** add SR + GR + "extra" energies linearly (triple counting).

**USE** multiplicative factor bookkeeping:
```
E_obs = E_rest × (transform factors)
```
