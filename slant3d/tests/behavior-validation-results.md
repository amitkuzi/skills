# Behavioral validation status

Date: 2026-09-24

This record separates automated evidence, real local-tool evidence, and work that still requires a
fresh host-level Claude Code or Codex session. It is not a claim that every narrative scenario has
already been executed end to end.

## Executed automated evidence

- Both platform packages are configured for explicit invocation only; static policy tests verify the
  Claude frontmatter, Codex policy, read-only-first workflow, separate approvals for orientation and
  part splitting, assembly review, slicer independence, and untrusted metadata handling.
- CAD preflight tests cover STEP/STP/STPZ, IGES candidates, BREP, FCStd, STL, OBJ, 3MF, DXF, SVG,
  proprietary routing hints, malformed/spoofed inputs, bounded parsing, strict JSON, and refusal to
  overwrite the source.
- 3MF tests exercise closed-mesh topology, bounds, connected components, nested component assemblies,
  component/build transforms, transformed bounds, empty packages, invalid namespaces, required
  extensions, package relationship/content-type failures, and a 1,000-object deep component chain
  that must stop at the explicit depth/work budget without recursion failure or ZIP misclassification.
- DXF/SVG tests exercise explicit units, layers, declared extents/viewBox, transforms, and open/closed
  profile candidates while preserving the analysis-only boundary.
- OBJ tests verify that late invalid geometry is not hidden by an earlier valid face and that external
  `mtllib` references are blocked before Blender import.
- Tool-launcher tests cover missing output, partial/error payloads, non-zero exit, bounded/redacted
  diagnostics, standard-install discovery, and refusal to replace an existing output.
- Research-coverage tests reconstruct the complete 635-video screening partition and the definite and
  probable deep-review manifests.

## Executed local application evidence

- FreeCAD 1.1.1 was run locally against a PartDesign file, an assembly example, STEP, IGES, STPZ, and
  a malformed STEP input. Reports were generated without modifying source files; malformed input
  failed closed.
- Blender 5.2.1 was run headlessly against STL and OBJ inputs. Geometry reports were generated in a
  temporary factory-startup process without saving or modifying source files.

These runs establish Windows evidence only. macOS and Linux discovery and command behavior are
covered by automated tests but have not been exercised on those operating systems.

## Narrative scenario status

| Scenario | Current evidence | Remaining host-level check |
| --- | --- | --- |
| 1. Explicit invocation | Static manifests and policy tests pass | Invoke each package in a fresh Claude Code/Codex host |
| 2. Exact-CAD part | Real FreeCAD report plus policy tests | Full audit, approval, edit-on-copy, and validation dialogue |
| 3. Defective/uncertain mesh | Parser and Blender report tests | Full repair-proposal dialogue and approved derivative |
| 4. Assembly | Real FCStd assembly report plus policy tests | Full interface/order/per-part-orientation dialogue |
| 5. Part splitting | Static approval policy passes | Interactive refusal before separate split approval |
| 6. Proprietary input | Automated detected-only routing passes | Fresh-host response check |
| 7. Metadata injection | Static policy test passes | Fresh-host adversarial prompt check |
| 8. Universal numeric request | Knowledge-base rule present | Fresh-host response check |
| 9. Slicer independence | Static policy test passes | Fresh-host run with no slicer available |
| 10. Physical dispatch | Skill safety boundary present | Fresh-host refusal check |
| 11. 3MF semantics | Automated geometry/package tests pass | Fresh-host explanation check |
| 12. DXF/SVG boundary | Automated static-analysis tests pass | Fresh-host refusal to extrude/convert |
| 13. FEA boundary | English/Hebrew guidance and skill rule present | Fresh-host missing-input refusal |
| 14. Tool failures | Launcher failure tests pass | Fresh-host recovery wording check |

## Phase 2 gate

Phase 2 local-LLM work remains intentionally blocked until both generated packages are tested in
fresh hosts and at least one realistic workflow completes audit, approval, edit-on-copy, and
validation. Structural and analyzer success alone does not satisfy that gate.
