# Vertical Ricci curvature of totally geodesic submersions

Deep Bhattacharjee

This repository holds the LaTeX source of the paper *Vertical Ricci curvature of totally geodesic submersions* and the script that draws its figure.

**Theorem.** Let π: (M, g) → (B, h) be a Riemannian submersion whose fibres are compact, connected and totally geodesic, and suppose that the Ricci curvature of g is nonpositive on every vertical vector. Then O'Neill's tensor A vanishes, so M is locally the Riemannian product of a fibre and the base; if M is complete, its universal cover is the product of the universal covers of a fibre and of B.

The proof rests on the fact that, when the fibres are totally geodesic, the vertical part of the bracket of two basic fields restricts to a Killing field of every fibre, and on Bochner's formula for Killing fields on the compact fibre. Consequences: a compact Ricci-flat manifold admits no Riemannian submersion with totally geodesic fibres other than a local product, so compact Calabi–Yau, hyperkähler, G2 and Spin(7) manifolds with irreducible holonomy carry no such submersion onto a lower-dimensional base; the same holds for compact Einstein manifolds with nonpositive Einstein constant; and in general the fibre average of |A_X Y|^2 is bounded by the largest vertical Ricci curvature. Every formula used from the theory of submersions and of Killing fields is derived from the definitions in the appendices, and the curvatures of the Hopf fibration and of the Heisenberg nilmanifold are computed there.

## Layout

- `main.tex` — the paper (amsart, single column; MSC 2020: 53C12, 53C20, 53C25, 53C29).
- `anc/fig_dichotomy.py` — draws `fig_dichotomy.png` (matplotlib, 200 dpi); run it in the repository root before compiling.
- `.github/workflows/build.yml` — draws the figure and compiles `main.pdf` with `latexmk -pdf`.
- `.github/workflows/release.yml` — publishes a release from a tag and title.

## Build

```
python3 anc/fig_dichotomy.py
latexmk -pdf main.tex
```

## Releases

| Release | Zenodo DOI |
| --- | --- |
| v2.1.0 (the paper, corrected averaged bound) | [10.5281/zenodo.23875735](https://doi.org/10.5281/zenodo.23875735) |
| v2.0.0 (first release of the paper) | [10.5281/zenodo.23875228](https://doi.org/10.5281/zenodo.23875228) |
| all versions (concept DOI) | [10.5281/zenodo.23875227](https://doi.org/10.5281/zenodo.23875227) |

Release v1.0.0 (February 2026) predates the paper and has no Zenodo record.

## Citation

See `CITATION.cff`. The DOI of the release is also recorded in the paper's data availability section.

## Contact

d.bhattacharjee@erl-forschung.de (corresponding), itsdeep@live.com; GitHub-related contact egspl@proton.me (https://github.com/creelie).

## License

MIT, see `LICENSE`.
