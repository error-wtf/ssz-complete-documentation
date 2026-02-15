# Prime Directive

**Status:** ALWAYS FOLLOW

---

## The Prime Directive

> **Never use a single method for all observables.**

Always classify the observable first (null vs timelike vs orbit) and select the correct method (PPN vs Ξ) accordingly.

---

## Observable Classification → Method

### A) NULL / Light-Path Observables
**Examples:** Lensing, Shapiro, VLBI/group delay, lens time-delays

**Method:** PPN completion — multiply Ξ-only by (1+γ)
```
result = Ξ_only × (1 + γ)
```
- For GR-equivalent: γ = 1.0 → factor 2
- Ξ-only = g_tt contribution only (half of full GR)

### B) TIMELIKE STATIC / Clock Observables
**Examples:** Time dilation, gravitational redshift, GPS, Pound-Rebka

**Method:** Ξ-based directly
```
D(r) = 1/(1 + Ξ(r))
```
- Keep local c invariant by construction
- Differences are comparative (between clocks/frames)

### C) TIMELIKE ORBIT Observables
**Examples:** Perihelion advance, precession, frame dragging

**Method:** PPN orbit machinery (β, γ)
- NOT Ξ-only shortcuts

---

## Factor-2 Rule (CRITICAL)

If a null-observable comes out at **50% of GR**:
- **This is NOT a bug**
- It indicates "Ξ-only = g_tt piece"
- Full GR requires PPN: (1+γ), γ=1

---

## Regime Check (MANDATORY)

Before using any Ξ formula, determine regime via r/r_s:

| Regime | r/r_s | Formula |
|--------|-------|---------|
| Weak | > 10 | Ξ = r_s/(2r) |
| Blend | 1.8–2.2 | Hermite C² |
| Strong | < 1.8 | Ξ = 1-exp(-φr_s/r) |

---

## Quick Reference

```
Observable Type     → Method
─────────────────────────────────
NULL (light)        → PPN (1+γ)
TIMELIKE (clocks)   → Ξ-proxy
TIMELIKE (orbits)   → PPN (γ,β)
```

---

## The Mantra

> **Observable → Class → Method → Scope → Then calculate.**
