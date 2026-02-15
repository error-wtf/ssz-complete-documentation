# Structural Constants

**Status:** CANONICAL

---

## Primary Constants

| Constant | Symbol | Value | Role in SSZ |
|----------|--------|-------|-------------|
| Golden Ratio | φ | 1.618033988749895 | Fundamental segmentation constant |
| Pi | π | 3.141592653589793 | Division constant |
| Fine-structure | α | 1/137.036 | Geometric origin in SSZ |
| Coupling factor | φ/2 | 0.80902 | Appears in coupling radius |
| Speed of light | c | 299,792,458 m/s | Local invariant |
| Gravitational const. | G | 6.67430×10⁻¹¹ m³/(kg·s²) | Mass→geometry |
| Planck constant | ℏ | 1.054571817×10⁻³⁴ J·s | Quantum link |
| Solar mass | M☉ | 1.98892×10³⁰ kg | Reference mass |

---

## The Role of φ (Golden Ratio)

φ appears in SSZ as a **structural constraint**, not a fitted parameter:

1. **Strong-field Ξ:** `Ξ_strong = 1 - exp(-φ · r_s/r)` — φ sets the exponential scale
2. **Horizon value:** `Ξ(r_s) = 1 - e^(-φ) = 0.80171` — determined by φ
3. **Coupling radius:** `r_φ = (φ/2) · r_s · [1 + β·Δ(M)]` — φ/2 as coupling
4. **Frequency grid:** `R = φ^N` — discrete redshift scaling
5. **Logarithmic spiral:** `b = ln(φ)/Δθ ≈ 0.306` — geometric growth

The claim: without φ-geometry, SSZ loses predictive sharpness.

---

## The Role of π

| Context | How π enters |
|---------|-------------|
| Schwarzschild radius | r_s = 2GM/c² (implicitly via 3D geometry) |
| Perihelion precession | Δω = 6πGM/[a(1-e²)c²] |
| Curvature detection | Triangular frequency comparison |
| Fine-structure | α = e²/(4πε₀ℏc) |

SSZ treats φ and π as the two fundamental geometric constants of segmented spacetime.

---

## Key Derived Values

| Quantity | Expression | Value |
|----------|-----------|-------|
| Ξ_max | 1 - e^(-φ) | 0.80171 |
| D_min (at r_s) | 1/(1 + Ξ_max) | 0.55503 |
| z_max (at r_s) | Ξ_max | 0.80171 |
| r*/r_s (weak-strong intersection) | solved from Ξ_w = Ξ_s | 1.59481 |
| D(r*) | D_SSZ(r*) = D_GR(r*) | 0.61071 |

---

## Mass-Dependent Correction Δ(M)

```
Δ(M) = A · exp(-α / M^B)
A = 98.01
α = 2.7177 × 10⁴
B = 1.96
```

This correction is derived from φ-geometry, **NOT from data fitting**. It modulates the coupling radius for different mass scales.

---

## PPN Parameters (Exact)

| Parameter | Value | Status |
|-----------|-------|--------|
| β | 1 | Exact in SSZ |
| γ | 1 | Exact in SSZ |

Confirmed by Cassini (2003): γ = 1.000021 ± 0.000023

---

## Fundamental Physical Constants Used

| Constant | Symbol | Value | Unit |
|----------|--------|-------|------|
| Speed of light | c | 299,792,458.0 | m/s |
| Gravitational constant | G | 6.67430 × 10⁻¹¹ | m³/(kg·s²) |
| Planck constant | ℏ | 1.054571817 × 10⁻³⁴ | J·s |
| Boltzmann constant | k_B | 1.380649 × 10⁻²³ | J/K |
| Solar mass | M☉ | 1.98892 × 10³⁰ | kg |
| Electron mass | m_e | 9.10938 × 10⁻³¹ | kg |
| Elementary charge | e | 1.60218 × 10⁻¹⁹ | C |

---

© 2025–2026 Carmen N. Wrede, Lino P. Casu
