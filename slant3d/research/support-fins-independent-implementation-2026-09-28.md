# Third-party implementation and print validation of designed-in support fins

- **Research date:** 2026-09-28
- **Source:** [gittrahan/support-fins](https://github.com/gittrahan/support-fins) (MIT license), live at
  printfins.com. A browser-based tool that reads an STL/3MF/STEP, lets a human pick the print
  orientation and load direction, then bakes breakaway support fins, tines, sway braces, and a bed
  pad into the exported mesh.
- **Relationship to the existing corpus:** this is **not an independent primary source on the
  underlying claim**. Its own spec file (`docs/FIN-SPEC.md`) states plainly that "every number here
  is stated on camera by Slant 3D" in
  [How to Design Better Support Fins for 3D Printing](https://www.youtube.com/watch?v=vnn4XeKQobs),
  the same video already logged in
  [`claims/core-design-orientation-batch-01.md`](claims/core-design-orientation-batch-01.md#video-3)
  with **Medium confidence** on exact dimensions "because the exact dimensions are process specific."
- **What is new here:** a third party independently built a mesh-generation engine against that
  claim, pinned its geometry with an offline regression suite (`deno test tests/`), stress-tested it
  against an 11-model third-party STL set, and physically printed specific configurations with dated
  results. That is evidence about **feasibility and edge cases of the technique**, not a second
  independent statement of the original claim. Treat it as promoting selected sub-claims from
  **Source hypothesis** toward **Conditional practice**, never to **Verified result** for the general
  case.

## What the implementation confirms

1. **Horizontal tines vs. vertical tines is corroborated, not just asserted.** The repo's own
   engineering rationale (`docs/FIN-SPEC.md`, "Why the tines must be horizontal") independently
   derives the same conclusion the video states: a horizontal tine prints as one continuous bead with
   no retraction; a vertical tine is a frail one-dot-per-layer tower that may not fuse to the part at
   all. Two unrelated reasoning paths (a channel demo of a part falling off mid-print, and a
   toolpath-mechanics argument) converge. This raises "tines must be horizontal, not vertical posts"
   to **Corroborated practice**.
2. **A fin needs both a standoff wall and tines; a wall alone is directional only.** Consistent with
   the existing claim record; the implementation could not build a working "combined" fin any other
   way (see "Where we deviate" below).
3. **Print-tested configurations exist**, each a single data point, not a study:
   - A cube on its edge in PETG, printed 2026-09-24, using the "Light" bed-pad style (one layer,
     0.12 mm sideways gap off the first-layer outline) — the pad released cleanly.
   - A 249 mm fence-post cap in ASA, printed 2026-09-22 (twice, with 3 and 5 hand-placed sway braces),
     using PLA-profile default brace settings (0.2 mm gap, 0.3 mm bite, 6 mm tine spacing, 15% base
     depth, 0.2 mm layer height) — both prints came out clean, braces snapped off by hand, and the
     drift the braces exist to correct was gone.
   These are **Verified result** only for those exact geometries/materials/settings; the author
   explicitly declines to generalize the ASA numbers beyond "a safe starting point."

## Geometry parameters (Source hypothesis / Conditional practice — process-dependent)

All values below are the on-camera Slant 3D numbers as re-stated and used by the independent
implementation. They are dimensionless relationships or small-in-context values, not calibrated for
every printer/material; treat them as a starting proposal to size from the intended layer height and
nozzle diameter, per this skill's process-agnostic policy.

| Feature | Value | Notes |
|---|---|---|
| Fin body standoff from part face | 0.2 mm | same clearance logic as any slicer support |
| Tine height (vertical) | one layer line | must equal the *target* layer height or it slices into partial layers and stops being one continuous bead |
| Tine width | 0.4–0.8 mm | 0.4 mm ≈ one nozzle pass; prefer the smallest width that prints reliably |
| Tine count | ~7–8 near the base, tapering to fewer with height | most needed low, where the part is least stable |
| Base/pad | wide ellipse, ~1 mm thick disc, OR a dedicated bed pad sized to the part's first-layer outline | bed adhesion without a large witness scar |
| Bottom edge overhang threshold | faces steeper than ~45° from vertical need support | 45° is the conventional self-supporting default, not a universal material constant; verify against the intended process |
| Minimum supportable feature height | roughly 4 mm of standoff-wall height | shorter features cannot carry a real fin; use orientation change or slicer support instead |
| Fin top | rounded, never pointed | a sharp tip is a retraction/defect point |
| Placement | on an edge or corner | hides tine witness marks; avoid the middle of a visible face |
| Long/tall parts | two fins on opposite sides, or sway braces (below) | a single fin lets the part twist or sway free in the other direction |

## The practical ceiling the implementation surfaces

Measured across the repo's 11-model third-party STL test set: only **66% of contact-line stations
had a vertical face within 1.5 mm that could actually take a tine**, and only 13 of 20 overhang
regions had a standoff-capable face at all. The authors call this "why manual fin placement is a
core feature, not a fallback" — an automatic solver that is turned fully loose can produce a
geometrically "optimal" but unprintable result (their own stated failure case: a 155 mm part balanced
on a needle with two sail-sized fins).

**Skill consequence:** never auto-generate or auto-place support fins without human review of each
placement, exactly as this skill already requires separate approval for orientation and bed-contact
changes. Present candidate fin locations, the face they attach to, and the overhang/height math that
justifies each one; do not claim a part is support-fin-ready from geometry inspection alone.

## Sway braces — a related but distinct technique for tall/slender parts

Not from the Slant 3D video; the implementation's own extension for a different failure mode: a tall,
slender part with **no overhangs** can still drift, sag, or wobble under nozzle drag and layer
shrinkage, leaving visible drift marks. A sway brace is a vertical rib standing edge-on (its stiff
bending direction) against an upright face, tied to the part by evenly spaced one-layer horizontal
tines running the brace's full height, tapering from ~15% of height at the base to a 4 mm flat top.
This is print-validated only for the two 2026-09-22 ASA prints cited above; treat it as a **Source
hypothesis** for any other material or geometry.

**Skill consequence:** distinguish "part needs support because a face overhangs" from "part needs
lateral stabilization because it is tall and slender relative to its base" — the second calls for a
brace/stabilizer answer, not a fin, and is a materially newer, less-validated technique than the fin
geometry above.

## Where the implementation still deviates from the channel claim (its own admission)

- A gap-only standoff wall cannot carry horizontal tines across the true contact line — a wall can
  pass either below or above the contact line, never both, so the tines-carry-the-load design is not
  optional; it is required by the geometry, which is why edge/corner placement matters.
- The channel's ~2 mm bottom chamfer (to avoid the part starting on a single line) was deliberately
  **not implemented** in favor of a separate breakaway bed pad, specifically because a chamfer
  modifies the user's part geometry rather than only adding a support feature — the same
  never-touch-the-source-without-approval principle this skill already applies.
- Fin/tine profiles are not yet scale-aware in the implementation; a fixed profile can degenerate into
  an oversized splayed sheet on a low, short overhang. Treat any fixed absolute dimension as a
  starting point to be checked against the actual feature scale, never copied verbatim.

## Update to the "themes not independently established" list

In [`independent-validation-2026-09-24.md`](independent-validation-2026-09-24.md#themes-not-independently-established-by-the-sources-above),
"designed support fins/tines as superior for every production workflow" and "exact chamfer/overhang
angles, minimum walls, tine sizes, or clearances" remain correctly listed — this implementation does
not establish superiority over slicer supports for every workflow, and its own test set shows the
geometry cannot always be applied. What has changed is narrower: the horizontal-tine requirement is
now corroborated by independent engineering reasoning (not just restated), and specific
printer/material/geometry combinations now have a dated, named physical print result instead of only
a channel demonstration. Both distinctions must be preserved when citing this material.
