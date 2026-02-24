# SSZ cosmology scaffold (CMB/BBN/Growth) — runnable prototype

This directory contains a minimal **forward-model** pipeline to test SSZ cosmology impacts:

- CMB acoustic scale: r_s(z*), D_A(z*), theta_*
- BBN proxy: H_SSZ/H_GR at very high redshift
- Linear growth: D(z), f(z)
- No-curve-fitting policy: you compute residuals vs. data; you do **not** fit.

## Coupling modes

This prototype supports two explicit conventions for how SSZ time dilation couples into background expansion:

- `coupling_mode='divide'`  ⇒ H_SSZ = H_GR / D(z)
- `coupling_mode='multiply'`⇒ H_SSZ = H_GR * D(z)

Both are computed so we can see what would be ruled out.

## Current default numerical summary

```json
{
  "divide": {
    "coupling_mode": "divide",
    "params": {
      "h": 0.674,
      "Omega_m": 0.315,
      "Omega_b": 0.049,
      "Omega_L": 0.685,
      "Tcmb": 2.7255,
      "Neff": 3.046,
      "Phi0": 1e-05,
      "Xi_const": null,
      "coupling_mode": "divide"
    },
    "CMB_theta_GR_rad": 11.346744367270961,
    "CMB_theta_SSZ_rad": 11.346750553954978,
    "CMB_theta_ratio": 1.0000005452386884,
    "CMB_rs_ratio": 0.9999882068118804,
    "CMB_DA_ratio": 0.9999876615799194,
    "BBN_H_ratio_at_z=4e9": 1.00001
  },
  "multiply": {
    "coupling_mode": "multiply",
    "params": {
      "h": 0.674,
      "Omega_m": 0.315,
      "Omega_b": 0.049,
      "Omega_L": 0.685,
      "Tcmb": 2.7255,
      "Neff": 3.046,
      "Phi0": 1e-05,
      "Xi_const": null,
      "coupling_mode": "multiply"
    },
    "CMB_theta_GR_rad": 11.346744367270961,
    "CMB_theta_SSZ_rad": 11.346738180652627,
    "CMB_theta_ratio": 0.9999994547671003,
    "CMB_rs_ratio": 1.0000117933332693,
    "CMB_DA_ratio": 1.0000123385728965,
    "BBN_H_ratio_at_z=4e9": 0.999990000099999
  }
}
```

## Key files

- `ssz_cosmo.py` — model + integrals + growth ODE
- `run_cosmo.py` — generates CSV + JSON summaries for both coupling modes
- `ssz_cosmo_results_divide.csv`, `ssz_cosmo_results_multiply.csv`
- `ssz_cosmo_summary_all.json`
- `Hratio_both.png`, `growth_both.png`
