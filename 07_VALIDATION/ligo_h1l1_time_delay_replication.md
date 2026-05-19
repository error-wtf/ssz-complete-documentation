# LIGO H1/L1 Time-Delay Replication — GW240925

**Date:** 2026-05-19 | **Script:** run_h1_l1_time_delay_replication.py | **Claim:** NO

## Method
FFT xcorr lag scan ±50 ms coarse / ±10 ms fine. 6 subbands (20-40, 40-80, 80-120, 120-160, 160-210, 20-210 Hz). Off-source window at t-500s. Sign-flip test for L1.

## Results

| Window | Band | Verdict | Peak dt | xcorr |
|--------|------|---------|---------|-------|
| TRIGGER | 20-40 Hz | PHYSICAL_DELAY_COHERENT | -0.24 ms | -0.9998 |
| TRIGGER | 20-210 Hz | PHYSICAL_DELAY_COHERENT | 0 ms | -0.9959 |
| OFF_m500 | 20-40 Hz | PHYSICAL_DELAY_COHERENT | 0 ms | -0.9998 |
| OFF_m500 | 20-210 Hz | PHYSICAL_DELAY_COHERENT | 0 ms | -0.9999 |

**TRIGGER_SPECIFIC: NO — PERSISTENT_SYSTEMATIC**

## Critical Finding

Trigger and off-source yield identical verdicts. The H1/L1 anti-correlation (xcorr≈-1 at dt=0) is persistent throughout the file — not specific to the GW240925 trigger. Cause: persistent environmental common-mode correlation (Schumann resonances, shared noise floor) and/or H1/L1 opposite arm-orientation sign convention.

The negative xcorr sign is physically expected: H1 and L1 have opposite strain sign conventions due to detector arm orientations.

**This result CANNOT be used to claim GW signal replication or SSZ support.**

## Gate

```
TRIGGER_SPECIFIC:              NO
READY_FOR_REAL_LIGO_SSZ_CLAIM: NO
SSZ_SUPPORT_CLAIM_MADE:        NO
SSZ_FALSIFICATION_CLAIM_MADE:  NO
```
