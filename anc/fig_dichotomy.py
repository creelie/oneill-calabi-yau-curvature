"""Figure 1 of the paper: Hopf twisting versus a local product (schematic)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

def hopf_circle(eta, phi, n=200):
    """A Hopf fibre on the torus |z1|=cos eta,|z2|=sin eta, stereographically projected."""
    t = np.linspace(0, 2*np.pi, n)
    z1 = np.cos(eta)*np.exp(1j*t)
    z2 = np.sin(eta)*np.exp(1j*(t+phi))
    x, y = z1.real, z1.imag
    u, v = z2.real, z2.imag
    d = 1.0 - v
    return x/d, y/d, u/d

fig = plt.figure(figsize=(11, 5.2), dpi=200)
# ---------------- left: Hopf fibration ----------------
ax = fig.add_subplot(1, 2, 1, projection="3d")
eta = 0.62
for phi in np.linspace(0, 2*np.pi, 9, endpoint=False):
    X, Y, Z = hopf_circle(eta, phi)
    ax.plot(X, Y, Z, color="0.72", lw=0.9)
X, Y, Z = hopf_circle(eta, 0.9)
ax.plot(X, Y, Z, color="#b3261e", lw=2.2, label=r"$F_b$")
# tangent (vertical) field xi along the fibre, and two horizontal arrows
for i in range(0, 200, 25):
    j = (i + 3) % 200
    ax.quiver(X[i], Y[i], Z[i], X[j]-X[i], Y[j]-Y[i], Z[j]-Z[i],
              color="#b3261e", arrow_length_ratio=0.45, lw=1.4)
i0 = 112
p = np.array([X[i0], Y[i0], Z[i0]])
tang = np.array([X[i0+3]-X[i0], Y[i0+3]-Y[i0], Z[i0+3]-Z[i0]]); tang /= np.linalg.norm(tang)
a = np.cross(tang, [0, 0, 1]); a /= np.linalg.norm(a)
b = np.cross(tang, a); b /= np.linalg.norm(b)
ax.quiver(*p, *(0.55*a), color="#1f4e9c", arrow_length_ratio=0.3, lw=1.8)
ax.quiver(*p, *(0.55*b), color="#1f4e9c", arrow_length_ratio=0.3, lw=1.8)
ax.text(*(p+0.70*a), r"$\widetilde X$", color="#1f4e9c", fontsize=12)
ax.text(*(p+0.70*b), r"$\widetilde Y$", color="#1f4e9c", fontsize=12)
ax.text(*(p-1.25*tang+np.array([0.15,0,-0.55])), r"$\xi=A_{\widetilde X}\widetilde Y$", color="#b3261e", fontsize=12)
ax.text(X[20], Y[20], Z[20]+0.3, r"$F_b$", color="#b3261e", fontsize=12)
ax.set_title(r"Hopf fibration: $A\neq0$, $\mathrm{Ric}(\xi,\xi)>0$", fontsize=11)
ax.set_axis_off(); ax.view_init(elev=28, azim=-55)
ax.set_box_aspect((1, 1, 0.8))
# ---------------- right: local product ----------------
ax = fig.add_subplot(1, 2, 2, projection="3d")
s = np.linspace(-1.6, 1.6, 60); t = np.linspace(0, 2*np.pi, 60)
S, T = np.meshgrid(s, t)
r = 0.55
ax.plot_surface(S, r*np.cos(T), r*np.sin(T), color="#d9e2f3", alpha=0.55, linewidth=0, antialiased=True)
for sv in np.linspace(-1.5, 1.5, 9):
    ax.plot(np.full_like(t, sv), r*np.cos(t), r*np.sin(t), color="0.55", lw=0.9)
ax.plot(np.zeros_like(t), r*np.cos(t), r*np.sin(t), color="#b3261e", lw=2.2)
ax.text(0.05, r*np.cos(1.2), r*np.sin(1.2)+0.2, r"$F_b$", color="#b3261e", fontsize=12)
# base line and horizontal leaf
ax.plot(s, np.full_like(s, -r), np.full_like(s, 0), color="#1f4e9c", lw=1.8)
ax.plot(s, np.full_like(s, -1.1), np.full_like(s, -0.9), color="k", lw=1.4)
ax.text(1.3, -1.1, -1.05, r"$B$", fontsize=12)
ax.quiver(0.0, -r, 0.0, 0.7, 0, 0, color="#1f4e9c", arrow_length_ratio=0.25, lw=1.8)
ax.text(0.75, -r-0.05, 0.08, r"$\widetilde X$", color="#1f4e9c", fontsize=12)
ax.text(-1.55, 0.2, 0.75, r"$M\cong F\times B$ locally, $A=0$", fontsize=11)
ax.set_title(r"nonpositive vertical Ricci curvature: product", fontsize=11)
ax.set_axis_off(); ax.view_init(elev=22, azim=-60)
ax.set_box_aspect((2.2, 1, 1))
plt.tight_layout()
plt.savefig("fig_dichotomy.png", dpi=200, bbox_inches="tight")
print("ok")
