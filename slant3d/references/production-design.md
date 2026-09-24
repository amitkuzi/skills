# Production Design Reference

This is the compact reference used by the skill. The complete 635-video long-form catalog was
screened; all 185 definite and 49 probable candidates received full-caption review. Of those, 219
videos contributed 970 timestamped claim records. These rules are a conservative synthesis, not an
endorsement of every channel claim or proof that a specific part is production-ready.

Detailed evidence:

- `../research/coverage-summary-2026-09-24.md`
- `../research/claims/core-design-orientation-batch-01.md` through batch 08
- `../research/claims/probable-video-deep-review.md`
- `../research/claims/thematic-synthesis-full-corpus.md`
- `../research/claims/best-practice-traceability-matrix.md`
- `../research/independent-validation-2026-09-24.md`

The traceability matrix maps every substantive section below to exact official-video timestamps,
independent evidence where available, conflicts, and the evidence needed to move from proposal to
verified result.

## Evidence labels

- **Invariant check:** safe to inspect without a printer profile, such as invalid solids, non-manifold
  edges, open shells, duplicate bodies, assembly references, or scale ambiguity.
- **Conditional practice:** generally useful but depends on loads, feature size, material, nozzle,
  layer height, machine behavior, surface requirements, or production handling.
- **Source hypothesis:** recurring Slant 3D advice that has not been independently established for
  the model and must be tested before becoming an approved change.
- **Verified result:** supported by a stated parser check, slicer preview, measured prototype, or
  production sample. Name the evidence; never use the label without it.

## Review sequence

1. Establish source fidelity, units, coordinate system, part/instance identity, and geometry health.
2. State the product's function, load cases, critical interfaces, cosmetic surfaces, environment,
   expected life, production quantity, and required evidence. Unknowns remain explicit.
3. Analyze every part in at least several feasible orientations. Compare load paths, interfaces,
   support/bridging, bed contact, surface finish, accuracy, stability, removal, and packing.
4. Redesign unsupported or weak features only after choosing candidate orientations; orientation and
   geometry are coupled decisions.
5. Review interfaces, hardware, assembly order, tooling access, inspection, service, and packaging.
6. Propose changes with tradeoffs and validation tests. Obtain approval before editing.
7. Validate the new artifact against the original: units, bounds, part count, transforms, topology,
   interfaces, and every intentional change.

## Requirements, parameters, and product families

- Capture the interfaces imposed by the surrounding product before remodeling: envelope, datums,
  mounting pattern, motion space, purchased hardware, cable/tool access, and the surfaces that may
  vary between host products.
- Expose functional dimensions as named parameters instead of burying them in unrelated sketches or
  repeating manual edits. Parameterization improves control; it does not validate an incorrect
  requirement or generated result.
- For product families, separate the genuinely custom interface from a stable base and standardized
  hardware. Reuse an already verified feature only when its loads, orientation, mating geometry, and
  process assumptions remain valid.
- Keep variants within intentional manufacturing, inspection, labeling, and packaging envelopes when
  that reduces production complexity. Do not force a common envelope when function or safety needs a
  different design.
- Keep the internal parametric family broader than the released catalog when useful, but curate
  customer-facing variants from demand, usability, QA, packaging, documentation, and support evidence.
  Manufacturable combinations are not automatically valuable or supportable products.

## Orientation

- **Conditional practice:** align continuous roads/layers with primary tensile and bending load paths
  where practical, while avoiding a single weak layer plane across a critical root, boss, loop, pin,
  handle, snap, or enclosure wall.
- Do not optimize strength alone. Include dimensional accuracy, support, first-layer stability,
  trapped support, critical finish, seams, throughput, removal, and assembly orientation.
- A diagonal/edge orientation can distribute layer directions and equalize visible faces, but often
  reduces bed contact and needs a designed stabilizer. It is a candidate, never a default.
- Choose orientation per component. An enclosure, lid, pin, spring, and insert may need different
  build directions even when they belong to one assembly.
- Orientation optimization remains a detailed proposal. Obtain separate explicit approval before
  applying a transform or creating an orientation-specific derivative, even if other edits are approved.
- Record the transform for each approved orientation variant. Do not rotate the source silently.

## First layer and bed contact

- **Conditional practice:** keep the first layer geometrically simple and move text, tiny islands,
  sharp cosmetic detail, and precision mating edges away from it when possible.
- Add a small bottom chamfer or relief where elephant-foot growth would interfere with fit. Size it
  from the intended layer height/process, not a fixed channel number.
- A mathematically sharp edge or round rod is not stable bed contact. Provide a deliberate flat,
  polygonal section, pad, or approved stabilizer.
- Wide contact improves adhesion but can increase removal force and automation difficulty. Small
  contact improves release but can detach or wobble. Treat this as an explicit tradeoff.
- Local ears, tabs, rafts, combs, and fins are source hypotheses until their breakaway behavior,
  witness marks, and removal labor are tested.
- Treat every bed-contact geometry change as an explicit change-plan item. Do not apply it merely
  because an orientation candidate appears promising.

## Overhangs, bridges, and support

- Prefer this order: change orientation; reshape the feature; shorten/split the unsupported span;
  then add only the support still required.
- **Conditional practice:** replace a bed-facing/horizontal fillet start or shelf with a chamfer or a
  custom blend that begins with supported layer increments. Preserve the required functional volume.
- Long roofs, circular side holes, recessed handles, domes, and captive features need separate bridge
  and sag analysis. A generic angle threshold is not enough.
- Designed support can improve repeatability, but it is still support. Specify contact geometry,
  separation, stability, removal direction/tool access, acceptable witness surface, and verification
  prints. Never call it "support-free."
- Experimental wave, arc, or other alternative overhang paths are process-specific manufacturing
  trials, not portable CAD rules. Require stability, time, quality, and repeatability evidence before
  relying on them to replace support or geometric redesign.
- Slicer support inspection is optional evidence; the design remains slicer-agnostic.

## Holes, pins, threads, and hardware

- Classify each opening by axis relative to build direction, load direction, fit function, sealing or
  bearing need, and access. Top holes, side holes, and bed-facing holes fail differently.
- Provide lead-ins for assembly. Chamfers are usually more predictable than a tangent underside
  fillet, but the final profile must preserve contact and strength.
- A side circular roof may sag. Candidate geometries include a relieved/pointed roof, polygonal
  contact faces, a keyhole profile, local support, or a different orientation. Do not change a
  precision circle without approval.
- Threads and inserts require sufficient surrounding section, torque/load direction, insertion tool
  access, heat/temperature review, and split-plane analysis.
- Captive nuts and magnets must have a positive retention path and assembly access. Absolute claims
  such as "never escapes" require pullout, impact, temperature, and lifecycle evidence.

## Fits and compliant interfaces

- No universal clearance is valid across machines, materials, colors, layer heights, or orientations.
  Use a named parameter and a representative calibration/interface coupon.
- Reduce uncontrolled full-perimeter contact. Candidate strategies include limited contact pads,
  tapered lead-ins, relieved corners, split fingers, leaf springs, and grip fins.
- Compliance absorbs dimensional variation but introduces strain, creep, fatigue, and wear. Review
  root stress, over-travel protection, layer-plane opening, duty cycle, and service environment.
- Validate initial assembly force, retention, repeatability, cycle life, and aged behavior as the
  product requires. "Perfect tolerance" and "lasts forever" are not acceptable conclusions.

## Walls, ribs, cavities, and local reinforcement

- Wall/section thickness must be related to road width/nozzle, feature scale, loading, deformation,
  material, and required life. Do not adopt a single minimum or strength threshold.
- Follow actual load paths with smooth section transitions and adequate material around holes,
  handles, loops, bosses, snaps, and fasteners.
- Do not copy injection-molding ribs or cavities automatically. A filled or backed region can print
  more simply and resist shear/warping; a cavity can still be required for flow, drainage, thermal,
  acoustic, weight, cleaning, access, or compliance reasons.
- Hidden cuts intended to provoke extra perimeters are **source hypotheses**: they depend on mesh
  export and slicer healing/toolpath behavior. Require preview or toolpath evidence and mechanical
  testing before treating them as reinforcement.
- Flag all geometry whose effect exists mainly through generated paths—thin walls, modeled gaps,
  textures, sacrificial interfaces, and hidden cuts. Slicer-agnostic does not mean toolpath-independent;
  keep the physical intent portable and verify the selected process when it becomes known.

## Text, texture, and cosmetic surfaces

- Keep critical text off the first layer and unsupported undersides. Check stroke width, island size,
  depth/height, font features, orientation, and contrast against the intended process.
- Texture can mask layer/seam/shrink artifacts but can change envelope, fit, friction, cleanability,
  optical behavior, and print time. Exclude mating, sealing, bearing, and controlled cosmetic datum
  surfaces unless approved.
- Model-based texture is more portable than a slicer-only effect, but its feature size still must be
  resolvable by the selected process.

## Scans and generated geometry

- Treat scan-, image-, mesh-, and AI-generated geometry as input evidence, not as a production-ready
  solid. Inspect artifacts, scale, topology, hidden cavities, surface noise, thin features, and
  imprecise spatial relationships.
- Add deliberate manufacturing geometry: stable datums, a controlled base, functional interfaces,
  clearances, access, and editable parameters. Do not infer these from an attractive organic surface.
- A scripted or parametric generator can encode exact dimensions only when the specification is
  exact. Verify its output with the same geometry, interface, and physical gates as human-made CAD.

## Assemblies and part consolidation

- Treat every component and instance separately, then check the system: mating interfaces,
  tolerances, degrees of freedom, alignment, fastener/tool access, collision, assembly order,
  serviceability, and load transfer.
- Part consolidation can reduce labor and hardware, but may increase print duration, reject cost,
  material coupling, replacement cost, support complexity, and service difficulty. Do not assume
  fewer parts is always better.
- Splitting is a separately approved intervention. Define cut planes, registration, joint type,
  load path, tolerance, seams, assembly access, and per-part orientation before editing.

## Print-in-place and moving mechanisms

- A print-in-place joint exchanges assembly labor for tighter dependence on orientation, clearance,
  bridge behavior, first-layer control, debris removal, and release access. It is not automatically
  the lower-risk production choice.
- Give hinges, latches, sliders, and captive parts a defined motion envelope, hard stops where needed,
  accessible release gaps, and a load path that does not pry apart a critical layer interface.
- Separate freedom-of-motion clearance from structural retention. Validate breakaway force, starting
  torque, travel, backlash, wear, creep, cycle life, and recovery after storage when they matter.
- Do not infer a working mechanism from a successful mesh load or free movement in CAD. Use a
  representative physical mechanism test under the intended orientation and process.

## Adhesive and sealed joints

- Adhesive joints need controlled bond area, surface preparation, a path for displaced adhesive,
  venting, fill confirmation, cure access, and an acceptance method. A larger hidden cavity alone
  does not prove a stronger joint.
- Grooves, injection ports, radial channels, and witness vents are candidate delivery features. Check
  viscosity, pressure, void trapping, chemical compatibility, cure shrink, cleanup, and the section
  lost to the channel before approving them.
- Water resistance depends on the complete leak path: seam geometry, overlap, capillary breaks,
  drainage, fastener compression, print porosity, orientation, material, and process. Do not equate a
  labyrinth or overlapping lid with a certified seal.
- Distinguish water shedding in a stated orientation, watertightness under a defined immersion or
  leak test, and pressure containment with a specified fluid, pressure, duration, and safety method.
  Passing one category does not establish either of the others.
- Vents and fluid paths require purpose-specific testing for flow, pressure drop, droplet entry,
  contamination, cleaning, and the actual direction of gravity and exposure.

## Rotating, aerodynamic, and balance-critical parts

- Blades, impellers, fans, and other rotating parts require symmetry, balance, hub retention,
  adequate root section, smooth transitions, and an orientation that does not place the dominant
  centrifugal or bending load across one weak layer plane.
- Support scars and uneven cleanup can unbalance a rotor. Prefer self-supporting geometry or symmetric
  post-processing, then measure runout and balance rather than relying on visual inspection.
- A geometry review is not approval for high-speed operation. Define speed, overspeed margin,
  enclosure/containment, material behavior, fatigue life, and a safe physical test plan separately.

## Production packing, cycle risk, and removal

- A full build plate maximizes parts per job but also couples more inventory to one failure, extends
  time before feedback, can amplify thermal interactions, and may complicate automated removal.
- Compare batch size using throughput, yield, recovery time, changeover, inspection, traceability,
  removal labor, and consequence of a stopped or rejected job—not part density alone.
- Rafts, brims, ears, combs, fins, and breakaway stabilizers must be treated as designed process
  features. Specify why each exists, how it separates, acceptable witness marks, and removal effort.
- Do not encode a universal packing density or batch size in CAD. Keep production assumptions
  parameterized and verify them with the selected process when known.

## Inspection and production feedback

- Define observable acceptance criteria before scale-up: critical dimensions and fits, warp/flatness,
  surface limits, contamination, layer or extrusion defects, mechanism force, hardware retention,
  and cosmetic boundaries as applicable.
- Distinguish an isolated process event from a repeated design/process interaction. Reprint only when
  evidence supports an isolated event; otherwise revisit preparation, orientation, and geometry.
- Feed measured rejects, removal problems, assembly difficulty, and field failures back into the CAD
  requirements and validation coupons. A model is not frozen merely because it printed once.
- Preserve traceability between source revision, approved change plan, generated artifact, process
  assumptions, sample results, and acceptance decision.

## Warpage and dimensional stability

- Flag large flat extents, sharp plan-view corners, abrupt mass/section changes, long continuous
  roads, asymmetric cooling geometry, and weak bed contact as risks.
- Geometry changes can reduce sensitivity, but warpage also depends on material, temperatures,
  chamber, cooling, layer strategy, and machine. Never claim that CAD alone eliminated it.
- Compare variants with measured flatness, corner lift, dimensional drift, and production yield.

## Validation gates

- **Geometry gate:** parser load succeeds; units/bounds/part count/transforms match intent; solids or
  meshes are valid enough for the next stage; no unexplained loss.
- **Interface gate:** mating/contact geometry and assembly sequence are checked for every part.
- **Orientation gate:** ranked alternatives and their tradeoffs are documented per part.
- **Process gate:** conditional features are evaluated with the chosen process when available.
- **Physical gate:** critical fits, compliant mechanisms, loads, hardware retention, warpage,
  cosmetics, and removal are validated with representative parts and acceptance criteria.
- A clean parser report or attractive render is not proof of manufacturability or production success.

### Strength and FEA boundary

- A qualitative load-path review is not finite-element analysis and does not establish a load rating.
- Offer FEA only when the user can supply or approve the load cases, constraints, contacts, material
  model, process-dependent assumptions, failure criteria, and acceptance threshold. Missing inputs
  must be reported, not invented.
- Treat simulated results as conditional evidence. Printed anisotropy, defects, creep, fatigue,
  environment, hardware interfaces, and process variation still require representative physical
  validation for the intended use.

## Regulated and safety-critical uses

- Food/drinking-water contact, medical or skin contact, children's products, electrical enclosures,
  fire/heat exposure, pressure, lifting, impact protection, and high-speed rotating or structural use
  require application-specific standards, material/process traceability, risk analysis, and qualified
  testing outside a general CAD review.
- Do not promote a channel anecdote, polymer label, successful prototype, or qualitative load-path
  review into a safety, biocompatibility, ingress, flame, electrical, food-contact, or load rating.
- When required inputs or competent validation are unavailable, identify the issue and stop at a
  non-authoritative design proposal.
