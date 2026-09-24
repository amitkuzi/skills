# Input Format Policy

Use this reference when selecting an analyzer, importing a model, or converting between formats.
Never claim support from a filename extension alone: identify the container or content and require a
successful parser load before geometry-dependent conclusions.

## Fidelity tiers

| Tier | Meaning | Typical inputs |
|---|---|---|
| `native-parametric` | Native feature/property graph and exact shape data | FCStd |
| `exact-brep` | Exact surfaces and topology without original feature history | STEP, IGES, BREP |
| `polygon-mesh` | Tessellated surface, not editable design intent | STL, 3MF, OBJ |
| `2d-reference` | Profiles/reference geometry only; no 3D conversion in this skill | DXF, SVG |
| `detected-only` | Candidate format awaiting an installed authorized parser | Proprietary CAD, AMF |
| `unsupported` | Unknown, malformed, or unavailable parsing path | Unknown or invalid input |

## Core matrix

| Input | Route | Required cautions |
|---|---|---|
| FCStd | Inspect the ZIP package, then use FreeCAD/FreeCADCmd | Add-on objects may require their original workbenches; inspect recompute errors and external references. |
| STEP/STP/STPZ | FreeCAD/Open CASCADE | Preferred neutral exact-CAD input, but it does not reconstruct the source feature history. STPZ is validated and its single bounded STEP member is extracted to an isolated temporary directory before import. Check units, hierarchy, placements, names, colors, solids, and shells. |
| IGES/IGS | FreeCAD/Open CASCADE | Legacy exchange. Validate sewing and solidness; prefer STEP when the source can export it. |
| BREP/BRP | FreeCAD/Open CASCADE | Exact topology/geometry but not a parametric model; do not promise assemblies, colors, PMI, or feature history. |
| STL | Blender or another approved mesh backend | Unitless and tessellated. Require units before dimensional edits; inspect topology, normals, components, and facet resolution. |
| 3MF | Inspect the OPC/ZIP package before mesh import | Can carry units, objects, transforms, color, and extensions. FreeCAD may flatten object hierarchy; record losses. |
| OBJ/MTL | Blender | Unitless polygon mesh. Preserve groups and materials where possible; treat hierarchy as advisory. |
| AMF | Detect only | Current FreeCAD documentation lists export but not import; request 3MF, STL, or STEP. |
| DXF/SVG | Static 2D analysis only | Never extrude, reconstruct, or describe the file as a printable 3D model. |
| SLDPRT/SLDASM | Installed licensed source application or approved importer | Prefer a source-generated STEP plus the untouched native files. |
| F3D/F3Z | Installed licensed Fusion on a supported platform | Prefer STEP for exchange; preserve the native file because STEP loses timeline and other design data. |
| IPT/IAM | Installed licensed source application or approved importer | Prefer authoring-system STEP; keep referenced assembly files together. |
| CATPart/CATProduct | Installed licensed source application or approved importer | Prefer CATIA-generated STEP; preserve product dependencies. |
| X_T/X_B | Installed licensed Parasolid-capable importer | Prefer STEP when no licensed converter is already available. |

## Analyzer routing

1. Run `scripts/cad_input_report.py <input>` to create the read-only preflight report.
2. For FCStd, STEP, IGES, and BREP, use FreeCADCmd for topology and shape-validity analysis when it
   is installed. Run `python scripts/run_freecad_geometry_report.py <input> --output <report.json>`.
   The launcher uses FreeCAD safe mode and passes user paths through a private environment handoff,
   not through FreeCAD's own argument parser. It checks `PATH` and standard Windows/macOS installation
   locations; use `--freecad-cmd <path>` for portable or nonstandard installs. Treat unresolved add-on
   objects as incomplete evidence.
   Neutral STEP/IGES currently uses FreeCAD's `Part.insert` in headless safe mode; FreeCAD 1.1 warns
   that this route is deprecated. The launcher preserves bounded, path-redacted stderr diagnostics,
   so treat that warning as a future-compatibility limitation until a verified headless replacement
   is available.
3. For STL and OBJ, use Blender headless for mesh diagnostics when it is installed.
   Run `python scripts/run_blender_mesh_report.py <input> --output <report.json>`. The launcher
   discovers standard Windows/macOS installs, runs Blender in background factory-startup mode, and
   passes private paths through an environment handoff. STL and OBJ remain unitless until the user
   confirms physical units.
   The launcher preserves raw OBJ coordinate values using Y-forward/Z-up import axes, but OBJ itself
   defines no universal physical up direction; confirm orientation intent before recommending a build
   direction.
4. Inspect 3MF as a package before opening it in an application; record unsupported extensions and
   hierarchy flattening.
5. Treat proprietary extensions as routing hints only. Require a successful licensed parser load or
   ask for a neutral STEP export.
6. Never turn mesh triangles into a face-per-triangle B-rep and call it an editable CAD reconstruction.

## Primary sources

- [FreeCAD FCStd format](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/File_Format_FCStd.md)
- [FreeCAD import/export support](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export.md)
- [FreeCAD import/export preferences](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Import_Export_Preferences.md)
- [FreeCAD console mode](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Start_up_and_Configuration.md)
- [FreeCAD scripted objects and embedded-code boundary](https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/Scripted_objects.md)
- [3MF Core specification](https://github.com/3MFConsortium/spec_core/blob/master/3MF%20Core%20Specification.md)
- [Blender STL importer](https://docs.blender.org/manual/en/5.3/files/import_export/stl.html)
- [Blender OBJ importer](https://docs.blender.org/manual/en/5.0/files/import_export/obj.html)
- [Autodesk Fusion export formats](https://help.autodesk.com/view/fusion360/ENU/?caas=caas%2Fsfdcarticles%2Fsfdcarticles%2FExport-format-options-for-Fusion-360.html)
- [CAD Exchanger format matrix](https://cadexchanger.com/formats/)
