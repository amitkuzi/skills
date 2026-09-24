# Research Scope and Evidence Rules

Cutoff date: 2026-09-24

## Corpus

- Inventory every public long-form upload visible through the Slant 3D channel's Videos catalog.
- Deeply analyze only videos that contain actionable information about CAD geometry, design for
  FDM, model repair, orientation, supports, strength, tolerances, slicing-relevant geometry, or
  repeatable production.
- Record non-relevant videos in the catalog, but do not spend transcript-analysis effort on them.

## Evidence labels

- **Channel claim:** advice stated or demonstrated by Slant 3D.
- **Corroborated practice:** a channel claim consistent with an independent primary technical
  source or repeatable tool check.
- **Conditional practice:** useful only for named machines, materials, slicers, orientations, or
  production constraints.
- **Conflict:** two sources recommend incompatible defaults; preserve both contexts rather than
  silently choosing one.
- **Inference:** a conclusion synthesized from sources but not stated directly by them.
- **Unverified:** plausible guidance that has not been independently checked.

The final documents must link every material rule to its source video and must not present channel
advice, slicer simulation, or geometry inspection as proof of a successful physical production run.

## Corroboration policy

- Slant 3D is the core corpus, not the sole authority.
- Cross-check material rules against primary sources such as manufacturer design guides, official
  software documentation, published standards, or peer-reviewed research when the claim warrants it.
- Do not use a repeated channel claim as independent corroboration.
- Preserve useful disagreements and state the differing machines, materials, geometry, or production
  goals that may explain them.
- Prefer dimensionless relationships, named parameters, and conditional ranges over defaults tied to
  a particular printer, nozzle, material, layer height, or slicer.
