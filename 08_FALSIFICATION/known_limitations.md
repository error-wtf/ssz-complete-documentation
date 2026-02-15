# Known Limitations and Open Questions

---

## Known Limitations

1. **Strong-field predictions untested:** The +13% NS redshift prediction has not been experimentally verified yet
2. **No quantum gravity connection:** SSZ is phenomenological, not derived from a quantum theory
3. **Rotating black holes:** The Kerr analog of the SSZ metric is not fully developed
4. **Cosmological coupling:** The cosmology scaffold is minimal (constraint-only)
5. **Gravitational waves:** SSZ modifications to GW waveforms are not yet calculated in detail

---

## Open Questions

1. **Why φ?** Is the golden ratio fundamentally necessary, or could another constant work?
2. **Microphysics:** What physical mechanism produces segmentation?
3. **Quantum regime:** How does SSZ connect to quantum gravity proposals?
4. **Kerr metric:** Full rotating black hole metric in SSZ?
5. **Cosmological perturbations:** Does SSZ modify structure formation?
6. **Gravitational wave ringdown:** Modified quasi-normal modes?

---

## Edge Cases in Implementation

- Numerical precision: ∇g < 10⁻¹⁰ (documented)
- Energy conservation: Drift < 10⁻⁶ (documented)
- Blend zone: C² continuity verified but not C∞
- z → 0 limit: Handled correctly in all repos
