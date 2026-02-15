# SSZ Quick Reference Card

---

## Core Equations

```
Ξ_weak(r)   = r_s / (2r)                  [r/r_s > 10]
Ξ_strong(r) = 1 - exp(-φ · r_s/r)         [r/r_s < 1.8]
D(r)        = 1 / (1 + Ξ(r))
z(r)        = Ξ(r)
s(r)        = 1 + Ξ(r) = 1/D(r)
r_s         = 2GM / c²
```

---

## Method Selection

```
Observable Type     → Method
─────────────────────────────────
NULL (light)        → PPN (1+γ)
TIMELIKE (clocks)   → Ξ-proxy
TIMELIKE (orbits)   → PPN (γ,β)
```

---

## Regime Selection

```
Regime              → Formula
─────────────────────────────────
r/r_s > 10          → Ξ = r_s/(2r)
1.8 < r/r_s < 2.2   → Hermite C² blend
r/r_s < 1.8         → Ξ = 1-exp(-φr_s/r)
```

---

## Key Values

```
Ξ(r_s) = 0.802       D(r_s) = 0.555
r*/r_s = 1.595       D*     = 0.611
φ/2    = 0.809       γ = β = 1
```

---

## Quick Formulas

```
s(r) = 1 + Ξ(r)              Scaling factor
D(r) = 1/s(r)                Time dilation
v_esc · v_fall = c²           Kinematic closure
R = φ^N                      Frequency lattice
dρ = s(r)dr                  Physical distance
1+z = D_obs/D_emit           Redshift
α = 2r_s/b                   Lensing (PPN)
Δt = 2(r_s/c)ln(...)         Shapiro (PPN)
```

---

## The Mantra

> **Observable → Class → Method → Scope → Then calculate.**

---

## Forbidden

```
❌ Ξ = (r_s/r)² exp(-r/r_φ)   DEPRECATED
❌ D = 1/(1+2Ξ)               WRONG
❌ r_s = GM/c²                 MISSING FACTOR 2
❌ PPN for time dilation       USE Ξ INSTEAD
❌ Δ(M) in weak field          WEAK = EXACT GR
```
