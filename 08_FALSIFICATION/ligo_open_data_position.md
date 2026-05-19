# LIGO Open Data — Methodology Position

**Date:** 2026-05-19 | **Cross-ref:** `ssz-ligo-tests/reports/OPEN_DATA_METHODOLOGY_POSITION.md`

## Central Conclusion

> Public LIGO release products are useful for standard GR/CBC analyses, but they are not sufficient, by themselves, for a fully independent, anti-circular test of alternative metric theories.

This repo does **not** claim LIGO data are fake or useless.  
This repo does **not** claim SSZ is confirmed or falsified by current LIGO releases.

## Strain Is Data; Posterior Products Are Interpretation

LIGO measures calibrated detector strain `h(t)`. Everything above that level is inferred.

| Layer | What it is | Status |
|-------|-----------|--------|
| h(t) — strain time series | Raw observable | Directly measured |
| f(t), ḟ(t) — instantaneous frequency | Extracted from h(t) | Model-assisted |
| ℳ, m₁, m₂, χ — source parameters | Inferred from h(t) under GR/CBC | Model-dependent |
| f_QNM, τ_QNM — ringdown parameters | Inferred under Kerr assumption | Model-dependent |

**m₁ and m₂ do not exist as numbers anywhere in the detector.**

## Chirp Mass Is Not a Direct Measurement

Chirp mass is mathematically well-motivated (not arbitrary):
```
M_chirp = (m1·m2)^(3/5) / (m1+m2)^(1/5)
ḟ ∝ ℳ^(5/3) · f^(11/3)
```

But it is defined and inferred **inside a GR/CBC waveform model**. For alternative metric theories, ℳ is not a neutral model-free measurement.

**Canonical statement:**
> LIGO measures strain h(t). Chirp mass ℳ is a model-conditioned inference, not a raw measurement. For alternative metric tests, raw strain must be used directly — not GR posteriors as inputs.

## Model-Bound Self-Confirmation

Using GR-posterior outputs (masses, spins, QNM frequencies) as independent proof of GR creates a circularity: the model's own outputs confirm the model.

**Correct test framing for SSZ:**
```
Can an SSZ forward model generate h_SSZ(f) that explains the calibrated strain
at least as well as a GR control, without using GR/Kerr posteriors as truth?
```

## Gate

```
READY_FOR_REAL_LIGO_SSZ_CLAIM:  NO
SSZ_SUPPORT_CLAIM_MADE:         NO
SSZ_FALSIFICATION_CLAIM_MADE:   NO
```
