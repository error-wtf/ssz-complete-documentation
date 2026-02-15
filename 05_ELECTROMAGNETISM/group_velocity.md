# Segment-Based Group Velocity

**Paper:** 08 (Segment-Based Group Velocity)

---

## Definition

```
v_group = L_seg · f / N
```

Where:
- **L_seg:** segment length
- **f:** frequency
- **N:** number of segments

---

## Interpretation

In SSZ, light propagation through segmented spacetime can be described by a group velocity that depends on the local segment structure. The group velocity differs from c by the segmentation effect:

```
v_group = c / s(r) = c · D(r)
```

In flat spacetime (s=1): v_group = c (as expected).

**Test:** `test_group_velocity.py`
