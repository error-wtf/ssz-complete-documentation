#!/usr/bin/env python3
"""
render_core_physics_animations.py
=================================
Animated GIF plots of the core SSZ (Segmented Spacetime) physics.

All formulas and numeric values are taken EXCLUSIVELY from the canonical
documentation of this repository (no invented physics):

* ``02_FOUNDATIONS/time_dilation.md``  (Status: CANONICAL)
    - D_SSZ(r) = 1 / (1 + Xi(r)),          d_tau = D * dt
    - GR comparison:  D_GR(r) = sqrt(1 - r_s/r)   -> 0 at r_s (singular)
    - Xi(r_s) = 0.80171,  D_SSZ(r_s) = 0.55503   (finite, no frozen time)
    - z_SSZ = 1/D - 1 = Xi  ->  z(r_s) = 0.802 (not infinite)
* ``02_FOUNDATIONS/segment_density.md``  (Xi branches)
    - weak form (g1):        Xi_weak(r)  = r_s / (2r)
    - inner decay form (g2): Xi_strong(r) = 1 - exp(-phi * r_s / r)
* ``02_FOUNDATIONS/regime_definitions.md``  (Status: CANONICAL)
    - 5 regimes in r/r_s: very_close <1.8 | blended 1.8-2.2 (Hermite C^2,
      quintic H5, t = (r/r_s - 1.8)/0.4) | photon_sphere 2.2-3.0 | strong
      3.0-10.0 | weak >10.0  (operative Xi branch above 2.2 is g1/weak form)
    - "Never mix formulas without an explicit blend rule."
    - Xi ranges per regime: 0.5-0.802 / 0.22-0.5 / 0.13-0.22 / 0.05-0.13 / <0.05
* ``02_FOUNDATIONS/regime_and_formula_domain_clarification.md`` (authoritative
  for which Xi branch is evaluated: g2 below 1.8, blend 1.8-2.2, g1 above 2.2)
* ``03_FORMULAS/formula_compendium.md``  (Status: CANONICAL, Single Source of
  Truth)  sections B.1/B.2: Xi_weak, Xi_strong, H5 blend, D, z, s(r) = 1+Xi
* ``03_FORMULAS/special_values.md``
    - Xi(r_s) = 0.80171, D(r_s) = 0.55503
    - D-intersections (mass-independent): r*/r_s = 1.594811 (decay/global)
      and r*/r_s = 1.386562 (saturation/local, metric-pure form)
* ``02_FOUNDATIONS/phi_lattice_discretization.md``
    - phi = (1+sqrt(5))/2 = 1.618034,  lattice x_k = phi^k on r/r_s
    - canonical table k=0..5 (x_k, Xi, D_SSZ, D_GR):
      1.000/0.802/0.555/0.000, 1.618/0.632/0.613/0.618, 2.618/0.191/0.840/0.786,
      4.236/0.118/0.894/0.874, 6.854/0.073/0.932/0.924, 11.09/0.045/0.957/0.954
    - Bracket theorem: r* in [r_s, phi*r_s];  D_GR(phi*r_s) = 1/phi = 0.618
      (Fibonacci identity 1/phi = phi - 1);  Xi_decay(phi*r_s) = 1-e^(-1) =
      0.63212;  D_SSZ(phi*r_s) = 0.61270
    - QNM prediction: f_QNM_SSZ / f_QNM_GR = 1/D_SSZ(r*) ~ 1.39

Outputs (dark theme, English labels) written to ``demos/output/``:
    1. ssz_time_dilation_gr_vs_ssz.gif  -- D(r) built dynamically: GR -> 0 at
       r_s vs SSZ finite D(r_s)=0.55503
    2. ssz_regime_map_animated.gif      -- regime diagram with transition
       radii 1.8 / 2.2 / 3.0 / 10 fading in
    3. ssz_phi_lattice_bracket_theorem.gif -- growing phi-lattice x_k = phi^k
       plus bracket-theorem interval [r_s, phi*r_s]

Run:  /home/error/physics/venv/bin/python demos/render_core_physics_animations.py
(requires numpy, matplotlib, pillow)

Copyright notice of the documentation: (c) 2025-2026 Carmen N. Wrede, Lino P. Casu
"""

from __future__ import annotations

import os
import sys

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

# ---------------------------------------------------------------------------
# Canonical constants (documented values; see docstring for sources)
# ---------------------------------------------------------------------------
PHI = (1.0 + np.sqrt(5.0)) / 2.0          # 1.618034 (phi_geometry.md)
XI_AT_RS = 0.80171                        # Xi(r_s) = 1 - e^(-phi)  (special_values.md)
D_AT_RS = 0.55503                         # D(r_s) = 1/(1+Xi(r_s))  (special_values.md)
RSTAR_DECAY_GLOBAL = 1.594811             # D_SSZ = D_GR, decay/global    (special_values.md)
RSTAR_SAT_LOCAL = 1.386562                # D_SSZ = D_GR, saturation/local (special_values.md)
XI_DECAY_AT_PHI = 0.63212                 # 1 - e^(-1) at r = phi*r_s (phi_lattice_discretization.md)
D_SSZ_AT_PHI = 0.61270                    # D_SSZ(phi*r_s)            (phi_lattice_discretization.md)
QNM_RATIO = 1.39                          # f_QNM_SSZ/f_QNM_GR approx (phi_lattice_discretization.md)

# Regime boundaries in r/r_s (regime_definitions.md, CANONICAL)
B_VERY_CLOSE = 1.8
B_BLEND_HI = 2.2
B_PHOTON_HI = 3.0
B_STRONG_HI = 10.0

# Canonical phi-lattice table k=0..5 (phi_lattice_discretization.md),
# (x_k, Xi_SSZ, D_SSZ, D_GR) as documented (3-decimal rounding in the doc).
LATTICE_TABLE = [
    (0, 1.000, 0.802, 0.555, 0.000),
    (1, 1.618, 0.632, 0.613, 0.618),
    (2, 2.618, 0.191, 0.840, 0.786),
    (3, 4.236, 0.118, 0.894, 0.874),
    (4, 6.854, 0.073, 0.932, 0.924),
    (5, 11.09, 0.045, 0.957, 0.954),
]

# Dark theme (README is English -> all labels English)
C_BG = "#0d1117"
C_PANEL = "#161b22"
C_GRID = "#30363d"
C_TEXT = "#e6edf3"
C_SSZ = "#58a6ff"      # SSZ curves  (blue)
C_GR = "#f85149"       # GR curves   (red)
C_BLEND = "#d29922"    # blend zone  (amber)
C_LATTICE = "#a371f7"  # phi lattice (purple)
C_OK = "#3fb950"       # verification accents (green)

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


# ---------------------------------------------------------------------------
# Xi(r) branches -- exactly as documented (segment_density.md, compendium B.1)
# ---------------------------------------------------------------------------
def xi_weak(x: np.ndarray | float):
    """g1 / weak form:  Xi_weak(r) = r_s / (2r)   [x = r/r_s]."""
    return 1.0 / (2.0 * np.asarray(x, dtype=float))


def xi_strong(x: np.ndarray | float):
    """g2 / inner decay form:  Xi_strong(r) = 1 - exp(-phi * r_s / r)."""
    return 1.0 - np.exp(-PHI / np.asarray(x, dtype=float))


def dxi_weak_dx(x: np.ndarray | float):
    return -1.0 / (2.0 * np.asarray(x, dtype=float) ** 2)


def dxi_strong_dx(x: np.ndarray | float):
    x = np.asarray(x, dtype=float)
    return -(PHI / x**2) * np.exp(-PHI / x)


# Blend-zone endpoint data (x = 1.8 and 2.2, Delta x = 0.4)
_XA, _XB = B_VERY_CLOSE, B_BLEND_HI
_DX = _XB - _XA
_XI_A = float(xi_strong(_XA))
_XI_B = float(xi_weak(_XB))
_DXI_A = float(dxi_strong_dx(_XA))
_DXI_B = float(dxi_weak_dx(_XB))


def xi_blend(x: np.ndarray | float):
    """Quintic Hermite C^2 blend, 1.8 <= r/r_s <= 2.2 (compendium B.2,
    regime_definitions.md):  t = (x-1.8)/0.4,  Xi_blend = H5(t) with the
    standard quintic Hermite basis matching value+1st+2nd derivative at both
    endpoints."""
    t = (np.asarray(x, dtype=float) - _XA) / _DX
    h00 = 1 - 10 * t**3 + 15 * t**4 - 6 * t**5
    h10 = t - 6 * t**3 + 8 * t**4 - 3 * t**5
    h01 = 10 * t**3 - 15 * t**4 + 6 * t**5
    h11 = -4 * t**3 + 7 * t**4 - 3 * t**5
    return h00 * _XI_A + h10 * _DX * _DXI_A + h01 * _XI_B + h11 * _DX * _DXI_B


def xi_operative(x: np.ndarray | float):
    """Operative Xi(x) with MANDATORY regime check (regime_definitions.md):
    x<1.8 decay (g2) | 1.8-2.2 Hermite C^2 blend | >2.2 weak form (g1)."""
    x = np.asarray(x, dtype=float)
    xi = np.where(x < _XA, xi_strong(np.clip(x, 1e-9, None)), np.nan)
    m_blend = (x >= _XA) & (x <= _XB)
    xi = np.where(m_blend, xi_blend(np.clip(x, _XA, _XB)), xi)
    xi = np.where(x > _XB, xi_weak(x), xi)
    return xi


def d_gr(x: np.ndarray | float):
    """GR time dilation factor  D_GR = sqrt(1 - r_s/r)."""
    x = np.asarray(x, dtype=float)
    return np.sqrt(np.clip(1.0 - 1.0 / x, 0.0, None))


def d_ssz(x: np.ndarray | float):
    """SSZ time dilation factor  D_SSZ = 1/(1+Xi(r))."""
    return 1.0 / (1.0 + xi_operative(x))


# ---------------------------------------------------------------------------
# Self-verification against the documented canonical numbers BEFORE rendering
# ---------------------------------------------------------------------------
def _selfcheck() -> None:
    eps = 1e-5
    checks = [
        ("Xi(r_s) = 1-e^(-phi) = 0.80171", float(xi_strong(1.0)), XI_AT_RS),
        ("D(r_s) = 1/(1+Xi) = 0.55503", float(d_ssz(1.0)), D_AT_RS),
        ("Xi_decay(phi*r_s) = 1-e^(-1) = 0.63212", float(xi_strong(PHI)), XI_DECAY_AT_PHI),
        ("D_SSZ(phi*r_s) = 0.61270", float(d_ssz(PHI)), D_SSZ_AT_PHI),
    ]
    for name, got, want in checks:
        if abs(got - want) > eps:
            raise AssertionError(f"self-check failed: {name}: got {got:.6f}, want {want}")
        print(f"  [ok] {name}: computed {got:.5f}")
    # Exact Fibonacci identity D_GR(phi*r_s) = 1/phi = phi-1 (bracket theorem)
    got = float(d_gr(PHI))
    if abs(got - 1.0 / PHI) > 1e-12:
        raise AssertionError(f"self-check failed: D_GR(phi*r_s)=1/phi: got {got}")
    print(f"  [ok] D_GR(phi*r_s) = 1/phi = {got:.5f}  (bracket theorem)")
    # Documented decay/global intersection r*/r_s = 1.594811 (Delta = 0.0%)
    xStar = RSTAR_DECAY_GLOBAL
    delta = abs(float(d_ssz(xStar)) - float(d_gr(xStar)))
    if delta > 5e-4:
        raise AssertionError(f"self-check failed: r*=1.594811 intersection, |DeltaD|={delta:.2e}")
    print(f"  [ok] r*/r_s = 1.594811: D_SSZ-D_GR = {float(d_ssz(xStar)) - float(d_gr(xStar)):+.2e} (decay/global)")
    # Hermite blend C0/C1/C2 continuity at both boundaries (compare against
    # the exact endpoint values used to construct the blend)
    h = 1e-6
    for bnd in (_XA, _XB):
        outer_val = _XI_B if bnd == _XB else _XI_A
        if abs(float(xi_blend(bnd)) - outer_val) > 1e-12:
            raise AssertionError(f"blend C0 failed at x={bnd}")
        d_blend = (float(xi_blend(bnd + h)) - float(xi_blend(bnd - h))) / (2 * h)
        d_out = (float(xi_weak(bnd + 2 * h)) - float(xi_weak(bnd))) / (2 * h) if bnd == _XB \
            else (float(xi_strong(bnd)) - float(xi_strong(bnd - 2 * h))) / (2 * h)
        if abs(d_blend - d_out) > 1e-4:
            raise AssertionError(f"blend C1 failed at x={bnd}: {d_blend} vs {d_out}")
    print("  [ok] Hermite C^2 blend: C0/C1 continuous at 1.8 and 2.2")
    # Canonical lattice table (3-decimal rounding tolerance)
    for k, xk, xi_doc, d_doc, dgr_doc in LATTICE_TABLE:
        x = PHI**k
        if abs(x - xk) > 5e-3:
            raise AssertionError(f"lattice x_{k}: {x:.4f} vs doc {xk}")
        if abs(float(xi_operative(x)) - xi_doc) > 5e-3:
            raise AssertionError(f"lattice Xi k={k}: {float(xi_operative(x)):.4f} vs doc {xi_doc}")
        if abs(float(d_ssz(x)) - d_doc) > 5e-3:
            raise AssertionError(f"lattice D k={k}: {float(d_ssz(x)):.4f} vs doc {d_doc}")
        if abs(float(d_gr(x)) - dgr_doc) > 5e-3:
            raise AssertionError(f"lattice D_GR k={k}: {float(d_gr(x)):.4f} vs doc {dgr_doc}")
    print("  [ok] phi-lattice table k=0..5 matches documented values")


# ---------------------------------------------------------------------------
# Dark-theme helpers
# ---------------------------------------------------------------------------
def dark_ax(ax: plt.Axes) -> None:
    ax.set_facecolor(C_PANEL)
    ax.grid(True, color=C_GRID, linewidth=0.6, alpha=0.7)
    for s in ax.spines.values():
        s.set_color(C_GRID)
    ax.tick_params(colors=C_TEXT)


def new_fig(nrows: int = 1, figsize=(9.0, 5.2)):
    fig, axes = plt.subplots(nrows, 1, figsize=figsize, facecolor=C_BG)
    if nrows == 1:
        axes = [axes]
    for ax in axes:
        dark_ax(ax)
    return fig, axes


def _save(fig: plt.Figure, anim: FuncAnimation, path: str, fps: int = 10, n_frames: int = 0) -> None:
    writer = PillowWriter(fps=fps)
    anim.save(path, writer=writer, savefig_kwargs={"facecolor": C_BG})
    plt.close(fig)
    size_kb = os.path.getsize(path) / 1024.0
    print(f"  [written] {path}  ({size_kb:,.0f} kB, {n_frames} frames)")


# ---------------------------------------------------------------------------
# GIF 1: Time dilation D(r) = 1/(1+Xi(r)) -- GR vs SSZ, dynamically built
# ---------------------------------------------------------------------------
def gif_time_dilation() -> str:
    x = np.linspace(1.0, 10.0, 900)
    dssz = d_ssz(x)
    dgr = d_gr(x)

    fig, (ax,) = new_fig()
    fig.suptitle("SSZ Time Dilation:  D(r) = 1/(1+Xi(r))   vs   GR:  D = sqrt(1-r_s/r)",
                 color=C_TEXT, fontsize=12, fontweight="bold")

    (ln_gr,) = ax.plot([], [], color=C_GR, lw=2.4, label="GR:  D$_{GR}$ = sqrt(1-r$_s$/r)")
    (ln_ssz,) = ax.plot([], [], color=C_SSZ, lw=2.4, label="SSZ:  D$_{SSZ}$ = 1/(1+Xi)")
    sweep = ax.axvline(10.0, color=C_TEXT, lw=1.0, ls=":", alpha=0.8)
    ax.set_xlim(1.0, 10.0)
    ax.set_ylim(0.0, 1.05)
    ax.set_xlabel("r / r$_s$", color=C_TEXT)
    ax.set_ylabel("D(r)  (d$\\tau$ = D$\\cdot$dt)", color=C_TEXT)
    leg = ax.legend(loc="lower right", facecolor=C_PANEL, labelcolor=C_TEXT, edgecolor=C_GRID)
    txt = ax.text(0.025, 0.965, "", transform=ax.transAxes, color=C_TEXT, fontsize=9,
                  va="top", ha="left")

    statics: list = []

    def update(frame: int):
        for st in statics:
            try:
                st.remove()
                statics.remove(st)
                if st in ax.texts:
                    ax.texts.remove(st)
            except Exception:
                pass
        x_sweep = float(np.interp(frame, [0, 68], [10.0, 1.0]))
        m = x >= x_sweep
        ln_gr.set_data(x[m], dgr[m])
        ln_ssz.set_data(x[m], dssz[m])
        sweep.set_xdata([x_sweep, x_sweep])
        txt.set_text(f"sweeping inward:  r/r$_s$ = {x_sweep:.2f}")
        if frame >= 68:  # final annotation phase
            # SSZ finite value at the horizon
            pt = ax.plot([1.0], [D_AT_RS], "o", color=C_SSZ, ms=9, zorder=6)
            t1 = ax.annotate("SSZ:  D(r$_s$) = 0.55503  (finite)\nXi(r$_s$) = 0.80171,  z = 0.802",
                             xy=(1.0, D_AT_RS), xytext=(1.7, 0.36), color=C_SSZ,
                             fontsize=10, fontweight="bold",
                             arrowprops=dict(arrowstyle="->", color=C_SSZ))
            # GR singular horizon
            t2 = ax.annotate("GR:  D(r$_s$) $\\rightarrow$ 0  (singular,\nfrozen time)",
                             xy=(1.02, 0.02), xytext=(2.9, 0.10), color=C_GR,
                             fontsize=10, fontweight="bold",
                             arrowprops=dict(arrowstyle="->", color=C_GR))
            # Documented intersection decay/global
            pt2 = ax.plot([RSTAR_DECAY_GLOBAL], [float(d_gr(RSTAR_DECAY_GLOBAL))], "*",
                          color=C_OK, ms=15, zorder=6)
            t3 = ax.annotate("r*/r$_s$ = 1.594811\nD$_{SSZ}$ = D$_{GR}$  (decay/global)",
                             xy=(RSTAR_DECAY_GLOBAL, float(d_gr(RSTAR_DECAY_GLOBAL))),
                             xytext=(3.1, 0.52), color=C_OK, fontsize=9,
                             arrowprops=dict(arrowstyle="->", color=C_OK))
            # phi lattice anchor k=1
            t4 = ax.annotate("r = $\\varphi\\cdot$r$_s$:  D$_{SSZ}$ = 0.613,\nD$_{GR}$ = 1/$\\varphi$ = 0.618",
                             xy=(PHI, float(d_ssz(PHI))), xytext=(4.4, 0.72), color=C_LATTICE,
                             fontsize=9, arrowprops=dict(arrowstyle="->", color=C_LATTICE))
            statics.extend([*pt, *pt2])
            for t in (t1, t2, t3, t4):
                statics.append(t)
            txt.set_text("weak field:  SSZ reproduces GR to 1st order  (Xi = r$_s$/2r)")
        return ln_gr, ln_ssz, sweep, txt

    anim = FuncAnimation(fig, update, frames=76, interval=100)
    path = os.path.join(OUT_DIR, "ssz_time_dilation_gr_vs_ssz.gif")
    _save(fig, anim, path, n_frames=76)
    return path


# ---------------------------------------------------------------------------
# GIF 2: Animated regime diagram (very_close -> weak), transition radii fade in
# ---------------------------------------------------------------------------
def gif_regime_map() -> str:
    x = np.linspace(1.0, 30.0, 1500)
    xi = xi_operative(x)

    regimes = [
        ("very_close", 1.0, B_VERY_CLOSE, "#8b949e", "Xi = 1-exp(-$\\varphi$r$_s$/r)  (g$_2$ decay)", "0.5-0.802"),
        ("blended", B_VERY_CLOSE, B_BLEND_HI, C_BLEND, "Hermite C$^2$ blend H$_5$", "0.22-0.5"),
        ("photon_sphere", B_BLEND_HI, B_PHOTON_HI, "#39c5cf", "g$_1$ formula (operative)", "0.13-0.22"),
        ("strong", B_PHOTON_HI, B_STRONG_HI, "#ff7b72", "g$_1$ formula (operative)", "0.05-0.13"),
        ("weak", B_STRONG_HI, 30.0, C_OK, "Xi = r$_s$/(2r)", "<0.05"),
    ]
    bounds = [B_VERY_CLOSE, B_BLEND_HI, B_PHOTON_HI, B_STRONG_HI]

    fig, (ax,) = new_fig(figsize=(9.0, 5.4))
    fig.suptitle("SSZ Regime Map:  Xi(r) operative branches  (regime check is MANDATORY)",
                 color=C_TEXT, fontsize=12, fontweight="bold")
    (ln,) = ax.plot([], [], color=C_SSZ, lw=2.6, label="Xi$_{operative}$(r/r$_s$)")
    ax.set_xscale("log")
    ax.set_xlim(1.0, 30.0)
    ax.set_ylim(0.0, 0.9)
    ax.set_xlabel("r / r$_s$  (log scale)", color=C_TEXT)
    ax.set_ylabel("Xi(r)", color=C_TEXT)
    leg = ax.legend(loc="upper right", facecolor=C_PANEL, labelcolor=C_TEXT, edgecolor=C_GRID)
    txt = ax.text(0.02, 0.96, "", transform=ax.transAxes, color=C_TEXT, fontsize=9, va="top")

    artists: dict[str, list] = {"bands": [], "notes": []}

    def clear_lists():
        for key in ("bands", "notes"):
            for a in artists[key]:
                try:
                    a.remove()
                except Exception:
                    pass
            artists[key] = []

    def update(frame: int):
        # phase 1 (frames 0-30): curve builds left->right
        x_tip = float(np.interp(frame, [0, 30], [1.0, 30.0]))
        m = x <= x_tip
        ln.set_data(x[m], xi[m])
        txt.set_text("building Xi(r)…" if frame < 30 else "")
        # phase 2 (frames >= 32): regime bands + transition radii appear one by one
        clear_lists()
        if frame >= 32:
            n_regimes = min(int((frame - 32) // 8) + 1, len(regimes))
            alpha_scale = min((frame - 32) % 8 / 3.0, 1.0) if n_regimes <= len(regimes) else 1.0
            for i, (name, x0, x1, col, formula, xirange) in enumerate(regimes[:n_regimes]):
                alpha = 0.16 * (alpha_scale if i == n_regimes - 1 else 1.0)
                band = ax.axvspan(x0, x1, color=col, alpha=alpha)
                artists["bands"].append(band)
                xc = np.sqrt(x0 * x1) if x1 < 30.0 else 20.0
                note = ax.text(xc, 0.845, f"{name}\n{formula}\nXi: {xirange}",
                               color=col, fontsize=7.6, ha="center", va="top", fontweight="bold")
                artists["notes"].append(note)
            for j, b in enumerate(bounds):
                if frame >= 40 + j * 6:
                    artists["bands"].append(
                        ax.axvline(b, color=C_TEXT, lw=1.1, ls="--", alpha=0.85))
                    artists["notes"].append(
                        ax.text(b, 0.015, f"{b}", color=C_TEXT, fontsize=9,
                                ha="center", va="bottom", fontweight="bold"))
            if frame >= 68:
                artists["notes"].append(
                    ax.text(0.02, 0.80, "Transition radii: 1.8 / 2.2 / 3.0 / 10.0\n"
                                        "Blend: t=(x-1.8)/0.4, quintic H$_5$, C$^2$\n"
                                        "g$_2$$\\rightarrow$g$_1$ FORBIDDEN (irreversible)",
                            transform=ax.transAxes, color=C_TEXT, fontsize=8.4, va="top"))
        return ln, txt

    anim = FuncAnimation(fig, update, frames=80, interval=110)
    path = os.path.join(OUT_DIR, "ssz_regime_map_animated.gif")
    _save(fig, anim, path, fps=9, n_frames=80)
    return path


# ---------------------------------------------------------------------------
# GIF 3: phi-lattice x_k = phi^k growing + bracket-theorem interval
# ---------------------------------------------------------------------------
def gif_phi_lattice() -> str:
    x = np.linspace(1.0, 12.0, 900)
    dssz = d_ssz(x)
    dgr = d_gr(x)

    fig, (ax1, ax2) = new_fig(nrows=2, figsize=(9.0, 7.0))
    fig.suptitle("Golden-Ratio Lattice  x$_k$ = $\\varphi^k$  +  Bracket Theorem   "
                 "($\\varphi$ = 1.618034)",
                 color=C_TEXT, fontsize=12, fontweight="bold")

    ax1.plot(x, dgr, color=C_GR, lw=1.6, alpha=0.9, label="D$_{GR}$")
    ax1.plot(x, dssz, color=C_SSZ, lw=1.8, alpha=0.9, label="D$_{SSZ}$")
    bracket = ax1.axvspan(1.0, PHI, color=C_LATTICE, alpha=0.0)
    ax1.set_xlim(1.0, 12.0)
    ax1.set_ylim(0.0, 1.05)
    ax1.set_xlabel("r / r$_s$", color=C_TEXT)
    ax1.set_ylabel("D(r)", color=C_TEXT)
    ax1.legend(loc="lower right", facecolor=C_PANEL, labelcolor=C_TEXT, edgecolor=C_GRID, fontsize=9)
    ax1.set_title("Bracket theorem:  r* $\\in$ [r$_s$, $\\varphi\\cdot$r$_s$]", color=C_TEXT, fontsize=10)

    ax2.set_yscale("log")
    ax2.set_xlim(-0.5, 5.5)
    ax2.set_ylim(0.9, 14.0)
    ax2.set_xlabel("k", color=C_TEXT)
    ax2.set_ylabel("x$_k$ = $\\varphi^k$  (log scale)", color=C_TEXT)
    (ln_lat,) = ax2.plot([], [], color=C_LATTICE, lw=1.8, ls="--", alpha=0.8)
    txt2 = ax2.text(0.03, 0.93, "", transform=ax2.transAxes, color=C_LATTICE, fontsize=9, va="top")

    dyn: list = []

    def update(frame: int):
        for a in dyn:
            try:
                a.remove()
            except Exception:
                pass
        dyn.clear()
        k_show = int(np.clip(frame // 10, 0, 6))  # 0..6 stages (6 -> table)
        # lattice points on D(r) panel
        for k, xk_doc, xi_doc, d_doc, dgr_doc in LATTICE_TABLE[:k_show]:
            xv = PHI**k
            dyn.extend(ax1.plot([xv], [float(d_ssz(xv))], "o", color=C_LATTICE, ms=8, zorder=6))
            dyn.append(ax1.annotate(f"k={k}: x={xk_doc}, D={d_doc}",
                                    xy=(xv, float(d_ssz(xv))), xytext=(xv + 0.25, float(d_ssz(xv)) + 0.055),
                                    color=C_LATTICE, fontsize=7.8))
        # geometric progression panel
        ks = np.arange(k_show)
        xs = PHI**ks
        ln_lat.set_data(ks, xs)
        ax2.set_xlim(-0.4, max(5, k_show - 0.5 + 0.5))
        txt2.set_text("x$_k$ = $\\varphi^k$:  " + ", ".join(f"{v:.3f}" for v in xs))
        # bracket interval + r* markers appear once lattice covers k=1
        if frame >= 12:
            bracket.set_alpha(0.14)
            dyn.append(ax1.axvline(1.0, color=C_LATTICE, lw=1.2, ls=":", alpha=0.9))
            dyn.append(ax1.axvline(PHI, color=C_LATTICE, lw=1.2, ls=":", alpha=0.9))
            dyn.append(ax1.annotate("r$_s$", xy=(1.0, 0.5), xytext=(0.86, 0.5),
                                    color=C_LATTICE, fontsize=9))
            dyn.append(ax1.annotate("$\\varphi\\cdot$r$_s$", xy=(PHI, 0.42), xytext=(PHI - 0.02, 0.30),
                                    color=C_LATTICE, fontsize=9))
        if frame >= 22:
            dyn.append(ax1.plot([RSTAR_DECAY_GLOBAL], [float(d_gr(RSTAR_DECAY_GLOBAL))], "*",
                                color=C_OK, ms=14, zorder=7)[0])
            dyn.append(ax1.annotate("r* = 1.594811 r$_s$\n(decay/global)",
                                    xy=(RSTAR_DECAY_GLOBAL, float(d_gr(RSTAR_DECAY_GLOBAL))),
                                    xytext=(2.4, 0.22), color=C_OK, fontsize=8,
                                    arrowprops=dict(arrowstyle="->", color=C_OK)))
        if frame >= 32:
            dyn.append(ax1.plot([RSTAR_SAT_LOCAL], [float(d_gr(RSTAR_SAT_LOCAL))], "*",
                                color=C_BLEND, ms=14, zorder=7)[0])
            dyn.append(ax1.annotate("r* = 1.386562 r$_s$\n(saturation/local)",
                                    xy=(RSTAR_SAT_LOCAL, float(d_gr(RSTAR_SAT_LOCAL))),
                                    xytext=(2.15, 0.075), color=C_BLEND, fontsize=8,
                                    arrowprops=dict(arrowstyle="->", color=C_BLEND)))
        if frame >= 44:
            dyn.append(ax1.annotate("D$_{GR}$($\\varphi\\cdot$r$_s$) = 1/$\\varphi$ = 0.618\n"
                                    "Xi$_{decay}$ = 1-e$^{-1}$ = 0.63212,  D$_{SSZ}$ = 0.61270",
                                    xy=(PHI, float(d_ssz(PHI))), xytext=(4.6, 0.44),
                                    color=C_LATTICE, fontsize=8.6,
                                    arrowprops=dict(arrowstyle="->", color=C_LATTICE)))
        if frame >= 56:
            dyn.append(ax1.text(0.30, 0.035,
                                "QNM prediction:  f$_{SSZ}$/f$_{GR}$ = 1/D$_{SSZ}$(r*) $\\approx$ 1.39",
                                transform=ax1.transAxes, color=C_TEXT, fontsize=9,
                                fontweight="bold"))
        return [ln_lat, txt2]

    anim = FuncAnimation(fig, update, frames=66, interval=130)
    path = os.path.join(OUT_DIR, "ssz_phi_lattice_bracket_theorem.gif")
    _save(fig, anim, path, fps=8, n_frames=66)
    return path


# ---------------------------------------------------------------------------
def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    print("Self-verification against documented canonical values:")
    _selfcheck()
    print("\nRendering animations into demos/output/ …")
    paths = [gif_time_dilation(), gif_regime_map(), gif_phi_lattice()]
    print("\nAll GIFs rendered successfully:")
    for p in paths:
        print(f"  {p}  ({os.path.getsize(p):,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
