# Slant 3D probable-video deep review

**Review date:** 2026-09-24  
**Scope:** the 49 entries marked `Probable` in `relevant-video-candidates-2026-09-24.md`, screened for transferable CAD/model-preparation guidance for repeatable FDM production. Business advice, company news, printer operation, slicer-only tactics, and unsupported safety/material claims were not promoted.

## Result

- **Include: 34** — at least one caption-supported, transferable model-preparation or production-readiness claim.
- **Exclude: 15** — no sufficiently specific, in-scope claim after full-caption review.
- **Caption coverage: 49/49** had an original English automatic-caption track spanning the spoken content. “Complete” below means the final caption cue reaches the closing spoken portion; it does not mean the automatic transcript is error-free.

## Method and evidence rules

- Reviewed the complete `en-orig` YouTube automatic-caption track for every candidate, not just its title or description.
- Timestamps are caption timestamps and may drift by a few seconds. Claims are paraphrases rather than quotations.
- **High confidence** means the video directly demonstrates or clearly explains the design practice. **Medium** means the practice is transferable but anecdotal or product-specific. **Low** means the presenter is inferring a workflow, or the evidence is an uncontrolled demonstration.
- “Include” does not endorse every statement in the video. Medical, child-safety, food/water-contact, electrical, and quantitative strength claims still require authoritative standards and application-specific validation.
- Process-specific dimensions, material choices, machine behavior, and slicer settings were not generalized. The retained guidance is intended to remain slicer-, printer-, material-, and vendor-agnostic.

## Included videos and transferable claims

### #4 — When I Built Robots, I Couldn't Get Wheels

- **Decision:** Include. It gives a compact requirements-to-parameters example for a custom component, although it is not a detailed printability tutorial.
- **Caption coverage:** Auto EN complete; last cue **10:48 / 10:56**.
- **Claims:**
  - **00:37–01:43 — Medium:** Capture the dimensions and interfaces imposed by the surrounding assembly before modeling: overall diameter, available width, mounting-hole pattern, hub space, and bore/bearing choice. The exact dimensions in the story are product-specific.
  - **06:51–07:17 — Medium:** A reusable parametric model should expose functional variables such as diameter, width, bore type, and embedded hardware instead of forcing users to remodel the part for every variant.

### #8 — Real 3D Printed Products: Tidy Tool

- **Decision:** Include. It contains concrete advice on product-family constraints, thin-part risk, surface treatment, and reusable features.
- **Caption coverage:** Auto EN complete; last cue **12:22 / 12:30**.
- **Claims:**
  - **05:43–06:06 — Medium:** Treat early production feedback as design input and revise the model around observed use, rather than freezing the first printable version.
  - **06:08–07:13 — High:** Constrain product variants to a common manufacturing and packaging envelope so one production flow can serve the family.
  - **07:29–08:16 — Medium:** Large, thin geometry is sensitive to distortion; remove nonfunctional bulk, keep thin regions only where needed, and consider texture where cosmetic variation would otherwise be conspicuous. Texture hides appearance variation; it does not repair weak geometry.
  - **08:26–10:50 — Medium:** Build related variants from a stable base volume and reuse already engineered attachment/interface features. The video’s AI-assisted modeling proposal is speculative; the transferable point is controlled reuse and verification.

### #24 — Slant 3D Reacting to Negative Comments

- **Decision:** Include narrowly. One segment provides relevant load-path guidance; most of the video is commentary.
- **Caption coverage:** Auto EN complete; last cue **29:20 / 29:31**.
- **Claims:**
  - **13:19–15:01 — Medium:** Layer separation risk depends on how the applied load crosses layer interfaces. Do not copy a thin-wall molded design unchanged; redirect the load path and/or increase the load-bearing cross-section. No numeric safety factor or controlled test is supplied.

### #43 — We Made a Fake Dinosaur Fossil for a Bone Company

- **Decision:** Include. It shows the cleanup needed between scan/AI-derived organic geometry and a manufacturable model.
- **Caption coverage:** Auto EN complete; last cue **19:19 / 19:27**.
- **Claims:**
  - **04:26–04:50 — High:** Crop the source mesh and create a deliberate flat datum when an organic scan has no stable print base.
  - **13:43–13:52 — Medium:** Scan-derived geometry still needs cleanup, trimming, and purpose-built ancillary geometry before it is production-ready.
  - **15:47–16:26 — Medium:** Image-to-mesh output is a starting point, not proof of manufacturability; inspect and revise its base, surfaces, and functional interfaces.

### #88 — Gyraline: 3D Printed Part Beats a $100K Tool

- **Decision:** Include narrowly. A long podcast contains a useful DfAM and fastener-interface discussion.
- **Caption coverage:** Auto EN complete; last cue **1:10:25 / 1:10:32**.
- **Claims:**
  - **38:30–39:01 — Medium:** Additive manufacture needs its own engineering pass, comparable in intent to designing for molding; changing only material or machine is insufficient.
  - **40:53–42:24 — Medium:** Printed geometry can admit a screw from the side and capture a standard nut in a shaped pocket, avoiding a more complex machined clamping feature. Validate access, anti-rotation, wall thickness, and serviceability for the actual fastener and load.

### #110 — This is 800 Products in One: Chin Mounts

- **Decision:** Include. It is a strong example of separating a customized interface from standardized hardware.
- **Caption coverage:** Auto EN complete; last cue **08:16 / 08:19**.
- **Claims:**
  - **01:46–02:33 — High:** For a product that mates to many curved host surfaces, capture or reverse-engineer the mating surface for each host rather than relying on one nominal curve.
  - **04:50–05:31 — High:** Isolate the host-specific geometry in the printed base while standardizing the camera/attachment hardware. This limits custom CAD and inventory to the interface that actually changes.
  - **06:29–06:59 — High:** Use a controlled printed interface to bridge unique host geometry to universal third-party components, and evaluate that combined assembly rather than the printed body alone.

### #122 — This 3D Printed Product is Saving Lives: MedicMate

- **Decision:** Include with a safety caveat. It provides specific retention and human-interface features, but the title’s medical outcome is not independently validated here.
- **Caption coverage:** Auto EN complete; last cue **04:29 / 04:32**.
- **Claims:**
  - **00:48–01:43 — Medium:** Adapt clips to the carried object’s size, add compliant retention, and add a high-friction contact where slip is a known failure mode.
  - **01:44–02:38 — Medium:** Design small workflow aids into the body—such as a cap-grab feature, parking points, and a directional zigzag clip—so correct retention and release are physically legible. Medical suitability still requires independent risk analysis and validation.

### #133 — How Parts are Made in a Giant 3D Print Farm

- **Decision:** Include. It connects production inspection failures back to orientation, slicing, and design revision.
- **Caption coverage:** Auto EN complete; last cue **06:21 / 06:29**.
- **Claims:**
  - **01:13–02:14 — High:** Define visible acceptance checks for warp, layer shift, under-extrusion, and contamination/staining instead of treating “printed” as “accepted.”
  - **02:17–03:02 — High:** Route repeated failures into a structured review: reprint only when the event is isolated; otherwise revisit orientation/process preparation and then the geometry, returning examples and design notes to the model owner.

### #149 — 3D Printed Starbucks (Podcast 102)

- **Decision:** Include narrowly. A product critique contains concrete latch and load-transfer changes.
- **Caption coverage:** Auto EN complete; last cue **1:00:31 / 1:00:39**.
- **Claims:**
  - **18:19–20:53 — Medium:** For a rope-retaining hook, remove redundant bumps, widen/thicken the remaining latch, blend its root into the body with a broad V-shaped load path, and add a rope groove that communicates intended placement. These are concept-level suggestions, not a validated load rating.

### #160 — Doing More with $10 Filament (Podcast 97)

- **Decision:** Include narrowly. A phone-holder redesign demonstrates several useful consolidation and printability changes.
- **Caption coverage:** Auto EN complete; last cue **1:12:31 / 1:12:37**.
- **Claims:**
  - **19:19–20:22 — Medium:** Tune compliant tines around the required insertion/removal force, and integrate the spring function into the main plate when doing so reduces separate parts.
  - **20:22–21:45 — Medium:** Protect small load-bearing pins from an unfavorable orientation, avoid large flat horizontal ceilings by using self-supporting curvature, and consolidate the back plate when that improves bed contact and removes assembly. Verify fatigue and interface fit separately.

### #167 — 5 Companies Making Real Products with 3D Printing

- **Decision:** Include. It contains multiple transferable geometry, assembly, and variant-management examples.
- **Caption coverage:** Auto EN complete; last cue **17:15 / 17:20**.
- **Claims:**
  - **00:53–01:45 — Medium:** Layer lines can be an intentional visual/structural language, including continuous-outline forms, instead of a defect to imitate molding away.
  - **02:46–05:54 — High:** Standardize a small set of purchased components, vary only the few dimensions that create customer value, make assembly orientation obvious, and use repeated open patterns where they remove material without compromising the required load path.
  - **09:45–12:38 — Medium:** Define QC criteria before scale-up; minimize unnecessary bed-contact area where discoloration is a known risk; and use compliant grip features when the mating object varies in diameter/fullness. Required grip force must be tested.
  - **14:38–16:44 — Medium:** Do not preserve a thin, boxy molded form by default. A thicker organic shell can integrate functional cavities and openings while better matching FDM’s geometric freedom. The video’s aquarium-material safety statements are not promoted.

### #172 — Best AI Tools for Designing 3D Printed Products

- **Decision:** Include. It clearly distinguishes ideation meshes from dimensionally controlled CAD.
- **Caption coverage:** Auto EN complete; last cue **08:47 / 08:53**.
- **Claims:**
  - **01:32–05:35 — High:** AI-generated organic meshes can provide a concept baseline and flat starting base, but may contain artifacts and lack precise spatial relationships; they require human inspection and refinement before production.
  - **05:42–07:20 — High:** Scripted/parametric CAD can encode exact dimensions, but only if the prompt/specification supplies precise geometry and feature locations; verify the resulting model rather than trusting successful generation.

### #191 — Printed Reef's Aquarium Accessories

- **Decision:** Include for geometry only. Aquarium-contact material claims are excluded pending authoritative validation.
- **Caption coverage:** Auto EN complete; last cue **05:07 / 05:12**.
- **Claims:**
  - **03:00–04:28 — Medium:** Replace a thin, injection-mold-like box with an FDM-native body by subtracting the required functional cavity/opening from a thicker organic exterior. Confirm flow, cleaning, biological, and material requirements independently.

### #215 — This Failed Shark Tank Product Could've Saved $750,000 with 3D Printing

- **Decision:** Include. It is a concrete redesign from multi-part molded assembly to a printable mechanism.
- **Caption coverage:** Auto EN complete; last cue **08:42 / 08:47**.
- **Claims:**
  - **02:40–03:32 — High:** Add a stable, printable base/chamfer and arrange major loads primarily in the layer plane when possible.
  - **03:32–05:29 — Medium:** A print-in-place hinge, controlled latch interference, and a thicker monolithic body can remove pins and assembly steps. The original rotating handle may have a smoother feel, so consolidation is a tradeoff, not an automatic improvement.
  - **05:29–06:07 — Low:** The presenter predicts high durability but supplies no controlled life-cycle or load test; use the geometry ideas, not the durability claim.

### #217 — How Wooj is Designing Premium Lamps with 3D Printing

- **Decision:** Include with electrical/thermal caveats. It provides an aesthetic and assembly example, not lamp-safety evidence.
- **Caption coverage:** Auto EN complete; last cue **05:42 / 05:49**.
- **Claims:**
  - **01:22–02:16 — Medium:** Treat the repeated deposited layers as part of a diffuser’s intended optical/visual texture instead of copying a smooth molded shade.
  - **03:03–03:24 — Medium:** A continuous single-wall shade and a spring-like printed clasp can reduce part count. Validate heat, creep, electrical clearances, and retention with the actual light source.

### #252 — McDonalds Putting 3D Printed Lamps in Stores

- **Decision:** Include narrowly. One segment identifies a geometry strategy for continuous-path shades.
- **Caption coverage:** Auto EN complete; last cue **04:23 / 04:29**.
- **Claims:**
  - **02:05–02:25 — Medium:** Model a lamp shade as a continuous single-wall path when the production process is intended to deposit one uninterrupted perimeter. This is a geometry/process strategy, not a vendor-specific slicer instruction; thermal and electrical validation remains required.

### #280 — Tips from Million Dollar 3D Printing Stores

- **Decision:** Include. Despite substantial business commentary, the full review contains numerous concrete DfAM critiques.
- **Caption coverage:** Auto EN complete; last cue **42:01 / 42:08**.
- **Claims:**
  - **01:16–01:31 — Medium:** Simplify the first-layer outline on a visible face; intricate small contact features are harder to reproduce consistently.
  - **03:30–03:56 — High:** Slope protrusions upward and remove unsupported downward-facing regions to make a model supportless where practical.
  - **04:42–05:04 — High:** Steepen a lower bowl curve when a shallow underside plus thin fins creates an overhang/sagging risk.
  - **12:06–12:51 — High:** Redesign handles to be self-supporting and avoid a fillet beginning at the bed-facing edge, where it creates an unsupported rounded first transition. Preserve a required mating profile only where the interface demands it.
  - **19:27–20:09 — High:** Reorient star-like recesses so each top closes progressively, or use a shallow/deep relief backed by a continuous wall, rather than leaving unsupported internal ceilings.
  - **31:49–32:12 — Medium:** Prefer a deliberate chamfer over a shallow curve when it avoids changing layer-line appearance; repeated marginal-angle overhangs multiply production failure opportunities.
  - **33:15–35:53 — Medium:** Count fasteners and assembly actions as design costs; simplify only where the retained mechanism and service access still meet the functional requirement.

### #299 — How 3D Printing Got Stress Nut into Walmart

- **Decision:** Include. It demonstrates robust threads and controlled product variation.
- **Caption coverage:** Auto EN complete; last cue **04:57 / 04:59**.
- **Claims:**
  - **00:53–01:18 — High:** Use coarse, chunky printed threads and generous, verified clearance rather than fine molded-thread proportions when repeatable hand assembly is the goal.
  - **01:57–02:19 — Medium:** Keep the mechanical interface simple and stable while varying noncritical exterior features to create a product family.

### #387 — Prototypes are Easy. Production is Hard.

- **Decision:** Include. It directly defines the extra evidence needed before a CAD model is considered production-ready.
- **Caption coverage:** Auto EN complete; last cue **03:38 / 03:46**.
- **Claims:**
  - **00:00–01:50 — High:** A successful part on one printer/material/settings combination is a prototype result, not proof that the geometry is robust across production variation.
  - **01:52–02:12 — High:** Support removal that is acceptable once can become prohibitive labor at volume; treat post-processing actions as part of the model’s production cost.
  - **02:19–03:06 — High:** Define the quality target, print multiple samples across realistic variation, and feed recurring defects back into geometry before release.

### #408 — How We Made $11K on Kickstarter: BagClamp

- **Decision:** Include. It is a compact worked example of print-in-place consolidation, mating geometry, and surface orientation.
- **Caption coverage:** Auto EN complete; last cue **06:10 / 06:17**.
- **Claims:**
  - **00:18–01:57 — High:** Replace a separate pin with a print-in-place living hinge only when the hinge geometry, orientation, clearance, and fatigue behavior can be validated.
  - **02:25–03:58 — High:** Use self-supporting outer transitions, orient important visible surfaces consistently, minimize problematic bed contact, and add a locating groove so mating halves resist lateral slip.
  - **03:58–04:55 — Medium:** Shape the internal passage around the handled material’s flow path; assembly simplification must not obstruct the core function.

### #412 — Create Premium Retail Packaging

- **Decision:** Include. It offers concrete surface, fit, nested-orientation, and overhang guidance.
- **Caption coverage:** Auto EN complete; last cue **05:58 / 06:05**.
- **Claims:**
  - **02:03–02:33 — Medium:** Broad, shallow organic domes make stepping conspicuous; more deliberate faceted/crystalline slopes can make the deposited-layer texture intentional.
  - **03:18–03:47 — Medium:** Tune mating fit for the intended tactile and acoustic experience, and use a soft liner only if the premium feel justifies the extra material and assembly.
  - **04:10–04:50 — High:** Orient nested halves with matching angled surfaces so both can print without broad overhangs while still closing flush; bevel exposed edges where it improves handling.

### #430 — Everything You Need to Know About a Giant 3D Print Farm

- **Decision:** Include narrowly. It supplies production-envelope and post-processing constraints, but its exact farm dimensions are vendor-specific.
- **Caption coverage:** Auto EN complete; last cue **05:34 / 05:39**.
- **Claims:**
  - **01:00–01:28 — High:** Check the complete model and every intended orientation against the target manufacturing envelope. Do not generalize the video’s exact machine dimensions.
  - **03:10–04:07 — High:** Prefer geometry that can leave the printer complete; supports, painting, smoothing, and other manual finishes add recurring labor and limit scale. Test several production-intent samples rather than one showcase print.

### #432 — We Made a 3D Printed Squirt Gun and Put it on Kickstarter

- **Decision:** Include. It demonstrates a parametric purchased-part interface and replaceable modules.
- **Caption coverage:** Auto EN complete; last cue **04:52 / 04:59**.
- **Claims:**
  - **02:23–03:08 — High:** Parameterize the body around standard syringe sizes, use a twist-lock interface for replacement, and separate changeable nozzle modules from the stable handle. The cap still needed glue, so the assembly was not fully tool-free.
  - **03:49–04:20 — Medium:** Produce a minimum functional model early enough to obtain user feedback before investing in a refined product family.

### #436 — How Strong is a 3D Printed Ax?

- **Decision:** Include with low evidentiary weight. It visually demonstrates orientation-dependent failure, but the test is uncontrolled entertainment and cannot support quantitative strength claims.
- **Caption coverage:** Auto EN complete; last cue **15:40 / 15:45**.
- **Claims:**
  - **00:41–01:00 — Medium:** Choose orientation from the expected load path: the comparison places continuous in-plane paths along the blade in one version and layer interfaces across the load in the other.
  - **05:40–07:30 — Low:** The vertically printed version delaminates and loses a thin, poorly supported tip along layer boundaries in this demonstration. Treat this as a failure-mode prompt, not a material strength value.
  - **11:04–11:57 — Low:** The observed break paths differ with layer alignment, reinforcing the need to test the complete oriented geometry under representative loading.

### #459 — Minimize Risks in Mass Production 3D Printing

- **Decision:** Include. It directly warns against using an injection-molded CAD model unchanged for FDM production.
- **Caption coverage:** Auto EN complete; last cue **03:44 / 03:45**.
- **Claims:**
  - **01:03–01:36 — High:** A model that can be printed is not necessarily designed for FDM production. Rework molded geometry around the additive process and its strengths rather than requesting a one-to-one process substitution.
  - **01:36–03:03 — High:** State functional and quality requirements, obtain production-intent samples, and verify them against those requirements before committing to volume.

### #462 — Real 3D Printed Products: Tons Cycling Stands

- **Decision:** Include. It is a clear modular-family and assembly-simplification example.
- **Caption coverage:** Auto EN complete; last cue **04:31 / 04:33**.
- **Claims:**
  - **00:28–01:46 — High:** Standardize a few purchased components, vary only the length/geometry that creates customer value, and make assembly orientation obvious with forgiving interfaces.
  - **02:34–02:59 — Medium:** Use a repeated open grid where it removes material while preserving the required structural paths; validate the grid against actual loads.
  - **03:01–03:49 — Medium:** Drive product variation from controlled parameters instead of independent hand-edited models.

### #469 — Real 3D Printed Products: Wacky Bobbers

- **Decision:** Include. It connects a measurable watertightness requirement to support-free geometry.
- **Caption coverage:** Auto EN complete; last cue **05:51 / 05:57**.
- **Claims:**
  - **02:46–03:46 — High:** Define “waterproof” operationally—surface, immersion depth, duration, and acceptable leakage—then test to that requirement.
  - **03:50–04:07 — Medium:** Avoid supports and severe overhangs in a watertight shell when their removal can damage walls or introduce leak paths. Watertightness still depends on process, material, wall construction, and testing.

### #491 — Thoughts on the MK4, Fabbaloo Partnership, Filament Update

- **Decision:** Include narrowly. One segment provides process-aware structural design guidance.
- **Caption coverage:** Auto EN complete; last cue **13:15 / 13:21**.
- **Claims:**
  - **09:31–11:33 — Medium:** Treat anisotropy and visible layers as process characteristics; increase load-bearing cross-section and redesign the part for FDM rather than dropping a thin molded part into the process unchanged. The advice is qualitative, not a strength calculation.

### #493 — Real 3D Printed Products: LittleBots

- **Decision:** Include. It documents part consolidation and a printed compliant joint.
- **Caption coverage:** Auto EN complete; last cue **06:21 / 06:29**.
- **Claims:**
  - **04:26–05:47 — Medium:** Consolidate brackets, pins, and screws only where the printed body can take over their functions; a built-in living hinge removed separate gripper joints and simplified kit packing/assembly.
  - The presenter recalls the part-count reduction approximately rather than from records, so the numerical count is not promoted.

### #532 — That Time FDM 3D Printing Saved Tesla's Model Y

- **Decision:** Include as a low-confidence exception case. The reported CAD workflow is the presenter’s inference, not confirmed Tesla process evidence.
- **Caption coverage:** Auto EN complete; last cue **02:57 / 03:05**.
- **Claims:**
  - **01:52–02:18 — Low:** In an emergency, low-volume bridge, cropping only the changed geometry from an updated production part may restore function quickly. The presenter explicitly contrasts this with the normal rule to optimize geometry for the additive process.

### #546 — Reacting to the LTT Screwdriver: Making Products

- **Decision:** Include narrowly. It is largely a reaction/product-development video, but one segment is directly relevant to production-intent CAD.
- **Caption coverage:** Auto EN complete; last cue **21:16 / 21:25**.
- **Claims:**
  - **09:24–10:58 — High:** Choose the intended manufacturing process before finalizing geometry; injection-molding constraints and production-FDM constraints do not automatically overlap. Do not finish a product design first and only then ask how to manufacture it.
  - **11:54–12:33 — Medium:** Mark fixed and negotiable requirements because changing one dimension can cascade through dependent interfaces in a well-coupled product.
  - **20:42–20:55 — Medium:** A prototype that resembles the final product is not automatically the correct production model when the final process differs; re-engineer for the chosen process.

### #586 — Mass Producing Custom Electronics Enclosures

- **Decision:** Include. It provides enclosure-specific FDM adaptation guidance.
- **Caption coverage:** Auto EN complete; last cue **07:44 / 07:45**.
- **Claims:**
  - **01:43–02:47 — Medium:** Replace thin molded-shell assumptions with rounded/self-supporting transitions and appropriately thick load-bearing regions; integrate a latch when doing so removes assembly without compromising serviceability.
  - **02:51–03:10 — High:** Drive the enclosure envelope and standoff locations from the actual PCB and connectors, not a generic box.
  - **03:48–04:35 — Medium:** Surface patterns can provide intentional appearance without molding draft constraints. Electrical, thermal, flammability, ingress, and certification requirements remain separate validation work.

### #597 — How Does Slant 3D Keep Products Consistent?

- **Decision:** Include for requirements/QC linkage. It is operational rather than geometric, but it defines the acceptance criteria the CAD adaptation must target.
- **Caption coverage:** Auto EN complete; last cue **04:21 / 04:25**.
- **Claims:**
  - **01:20–01:23 — Medium:** Validate that the production process can repeatedly meet the client’s tolerance/specification rather than accepting a single nominal fit.
  - **03:02–03:26 — High:** Build a product-specific QC checklist: cosmetic products and engineering jigs may need different surface and tolerance criteria. Feed those criteria into interface dimensions and test plans.

### #598 — How Does Slant 3D Ensure Part Quality?

- **Decision:** Include for requirements/QC linkage. It translates product requirements into an inspection plan.
- **Caption coverage:** Auto EN complete; last cue **02:13 / 02:16**.
- **Claims:**
  - **00:29–01:10 — High:** Specify surface quality, consistency, tolerances, and strength requirements before release, and turn them into an inspectable checklist.
  - **01:42–02:03 — Medium:** Define a production-run inspection plan appropriate to the part and batch; passing one sample does not establish ongoing conformance.

## 49-video decision manifest

| # | Video | Decision | Caption coverage | Concise reason |
|---:|---|---|---|---|
| 4 | [When I Built Robots, I Couldn't Get Wheels](https://www.youtube.com/watch?v=lzfQkK5Vg9g) | Include | Auto EN complete, 10:48/10:56 | Requirements-to-parameters example for custom component interfaces. |
| 8 | [Real 3D Printed Products: Tidy Tool](https://www.youtube.com/watch?v=GWUe3-7JpJU) | Include | Auto EN complete, 12:22/12:30 | Variant envelope, thin-part risk, texture, and reusable features. |
| 24 | [Reacting to Negative Comments](https://www.youtube.com/watch?v=6WqCXSoTlbc) | Include | Auto EN complete, 29:20/29:31 | One useful load-path/cross-section segment. |
| 29 | [Teleport Gets More Colors (Podcast 159)](https://www.youtube.com/watch?v=l8ElaiQgAp0) | Exclude | Auto EN complete, 26:23/26:28 | Market and robotics discussion; no concrete CAD-preparation guidance. |
| 33 | [We Will Replace Bambu (Podcast 157)](https://www.youtube.com/watch?v=wFzF6Jn5A64) | Exclude | Auto EN complete, 50:17/50:26 | Surface discussion is slicer/material-operation specific, not model adaptation. |
| 43 | [Fake Dinosaur Fossil](https://www.youtube.com/watch?v=jIuApMPDcOc) | Include | Auto EN complete, 19:19/19:27 | Scan/AI-mesh cropping, flat datum, cleanup, and review. |
| 61 | [Wigglitz](https://www.youtube.com/watch?v=ofFRB6MfbZs) | Exclude | Auto EN complete, 09:27/09:29 | Business/IP/safety narrative; no sufficiently specific transferable geometry. |
| 81 | [STLFlix Founder (Podcast 135)](https://www.youtube.com/watch?v=b85kIuNkgk4) | Exclude | Auto EN complete, 2:05:36/2:05:42 | Business/service Q&A; packaging segment lacks CAD fit/tolerance detail. |
| 88 | [Gyraline (Podcast 132)](https://www.youtube.com/watch?v=lSCcJ2oTZZY) | Include | Auto EN complete, 1:10:25/1:10:32 | DfAM pass and side-access captured-nut interface. |
| 110 | [Chin Mounts](https://www.youtube.com/watch?v=HfFPf5YLobQ) | Include | Auto EN complete, 08:16/08:19 | Custom mating surfaces separated from standardized hardware. |
| 122 | [MedicMate](https://www.youtube.com/watch?v=X1c1Xp45U1E) | Include | Auto EN complete, 04:29/04:32 | Size-specific retention and workflow features; medical claims excluded. |
| 129 | [Ultimate Egg Drop Challenge](https://www.youtube.com/watch?v=I8-FADDae8M) | Exclude | Auto EN complete, 20:05/20:11 | Uncontrolled entertainment test, not repeatable production guidance. |
| 133 | [How Parts Are Made / Quality Checks](https://www.youtube.com/watch?v=vpKJZOfMO0c) | Include | Auto EN complete, 06:21/06:29 | Inspection-to-redesign feedback loop. |
| 149 | [3D Printed Starbucks (Podcast 102)](https://www.youtube.com/watch?v=vVDYytF2qqg) | Include | Auto EN complete, 1:00:31/1:00:39 | Concrete rope-hook latch and root redesign. |
| 160 | [Doing More with $10 Filament (Podcast 97)](https://www.youtube.com/watch?v=TqmLkCQ8g_0) | Include | Auto EN complete, 1:12:31/1:12:37 | Compliant phone-holder and monolithic plate redesign. |
| 167 | [5 Companies Making Real Products](https://www.youtube.com/watch?v=cBVgwIjP02w) | Include | Auto EN complete, 17:15/17:20 | Multiple relevant examples: variants, grips, grids, organic shells. |
| 171 | [3D Printed Coffee Accessories](https://www.youtube.com/watch?v=bWz7eJBvFpc) | Exclude | Auto EN complete, 10:26/10:30 | Niche/SKU/business discussion; only generic component mentions. |
| 172 | [Best AI Tools for Designing](https://www.youtube.com/watch?v=nYdWINEzRFs) | Include | Auto EN complete, 08:47/08:53 | Mesh-artifact warning and dimensional scripted-CAD verification. |
| 191 | [Printed Reef](https://www.youtube.com/watch?v=tGfErEfxXeA) | Include | Auto EN complete, 05:07/05:12 | Molded-like shell to thicker organic FDM form; safety claim excluded. |
| 215 | [Lugbug](https://www.youtube.com/watch?v=BTIoITF3P8U) | Include | Auto EN complete, 08:42/08:47 | Print-in-place hinge, latch, orientation, and consolidation tradeoff. |
| 217 | [Wooj Premium Lamps](https://www.youtube.com/watch?v=XzcIRxbbICI) | Include | Auto EN complete, 05:42/05:49 | Intentional layer texture and compliant clasp. |
| 252 | [McDonalds 3D Printed Lamps](https://www.youtube.com/watch?v=URB_nk12eHo) | Include | Auto EN complete, 04:23/04:29 | Continuous single-wall shade geometry strategy. |
| 280 | [Tips from Million Dollar 3D Printing Stores](https://www.youtube.com/watch?v=A88dY3EFZZ4) | Include | Auto EN complete, 42:01/42:08 | Many explicit self-supporting, first-layer, relief, and assembly critiques. |
| 299 | [Stress Nut into Walmart](https://www.youtube.com/watch?v=G0QAsBj7j5k) | Include | Auto EN complete, 04:57/04:59 | Coarse threads, generous clearance, stable interface across variants. |
| 331 | [3D Printed Shoes Worth $15M](https://www.youtube.com/watch?v=VaYoKDKv3No) | Exclude | Auto EN complete, 05:28/05:30 | Business/case study without transferable model-preparation detail. |
| 334 | [Uncommon Lamps](https://www.youtube.com/watch?v=PURB80OolQo) | Exclude | Auto EN complete, 04:19/04:21 | Inventory/business narrative; only generic “complex geometry” claims. |
| 346 | [How Strong Are Common Materials?](https://www.youtube.com/watch?v=5CFVcPYFEiE) | Exclude | Auto EN complete, 06:09/06:12 | Uncontrolled material comparison, not CAD preparation; numeric results not promoted. |
| 380 | [Smile Direct / Testing Lab Podcast](https://www.youtube.com/watch?v=LPLwoLx7xQ8) | Exclude | Auto EN complete, 31:08/31:10 | Relevant tip is extrusion-width/slicer-specific, outside model-only guidance. |
| 381 | [Adidas 3D Printed Shoes](https://www.youtube.com/watch?v=NnefRfnG9l8) | Exclude | Auto EN complete, 10:05/10:06 | Resin/DLS case, outside repeatable FDM model-preparation scope. |
| 387 | [Prototypes are Easy. Production is Hard.](https://www.youtube.com/watch?v=zgqsxcreqBs) | Include | Auto EN complete, 03:38/03:46 | Production-intent samples, QC targets, and post-processing labor. |
| 401 | [Filament Batch / Bladeless Fan Recap](https://www.youtube.com/watch?v=rS7KI_ZMWBs) | Exclude | Auto EN complete, 20:12/20:19 | Announcements and recaps; promised deeper guidance is not delivered here. |
| 408 | [BagClamp](https://www.youtube.com/watch?v=TEpAQjXNssk) | Include | Auto EN complete, 06:10/06:17 | Living hinge, mating groove, surface orientation, and flow path. |
| 412 | [Premium Retail Packaging](https://www.youtube.com/watch?v=WnkdxhW6TN0) | Include | Auto EN complete, 05:58/06:05 | Surface stepping, fit, nested orientation, and self-supporting closure. |
| 416 | [Out of Darts](https://www.youtube.com/watch?v=BBtazZdPQvE) | Exclude | Auto EN complete, 10:09/10:16 | Production/business operations; no specific CAD-adaptation practice. |
| 421 | [In Honor of the Mundane](https://www.youtube.com/watch?v=saWY5c_CcFg) | Exclude | Auto EN complete, 06:09/06:11 | General engineering philosophy without actionable model guidance. |
| 430 | [Everything About a Giant Print Farm](https://www.youtube.com/watch?v=gA_pred4CBI) | Include | Auto EN complete, 05:34/05:39 | Build envelope, printer-complete geometry, and production-intent samples. |
| 431 | [Custom 3D Printed Casts](https://www.youtube.com/watch?v=eqwCBV0rydk) | Exclude | Auto EN complete, 04:20/04:27 | Medical workflow with no concrete CAD-preparation detail; high-stakes claims withheld. |
| 432 | [3D Printed Squirt Gun](https://www.youtube.com/watch?v=mXkGvX3PdQg) | Include | Auto EN complete, 04:52/04:59 | Parametric standard-part interface and replaceable modules. |
| 436 | [How Strong is a 3D Printed Ax?](https://www.youtube.com/watch?v=4VU59XYuyhw) | Include | Auto EN complete, 15:40/15:45 | Orientation/failure-mode demonstration; quantitative strength excluded. |
| 459 | [Minimize Risks in Mass Production](https://www.youtube.com/watch?v=6pO9gcTnSb0) | Include | Auto EN complete, 03:44/03:45 | Explicit warning against printing molded CAD unchanged. |
| 462 | [Tons Cycling Stands](https://www.youtube.com/watch?v=9qe-_ClObaw) | Include | Auto EN complete, 04:31/04:33 | Standardized components, parametric variants, and simple assembly. |
| 469 | [Wacky Bobbers](https://www.youtube.com/watch?v=cbxD8Oz9L8Q) | Include | Auto EN complete, 05:51/05:57 | Operational watertightness requirement and support-free shell. |
| 491 | [Thoughts on the MK4](https://www.youtube.com/watch?v=qXGMN1U4jBs) | Include | Auto EN complete, 13:15/13:21 | Qualitative anisotropy and cross-section redesign guidance. |
| 493 | [LittleBots](https://www.youtube.com/watch?v=plzcdgsNn4M) | Include | Auto EN complete, 06:21/06:29 | Part consolidation and built-in living hinge. |
| 532 | [FDM Saved Tesla's Model Y](https://www.youtube.com/watch?v=aV2tv7GJ1-s) | Include | Auto EN complete, 02:57/03:05 | Low-confidence emergency bridge exception, clearly labeled inferred. |
| 546 | [Reacting to the LTT Screwdriver](https://www.youtube.com/watch?v=F9k8MFvd-5g) | Include | Auto EN complete, 21:16/21:25 | Choose process before final CAD and manage cascading requirements. |
| 586 | [Custom Electronics Enclosures](https://www.youtube.com/watch?v=MiCRp2uV1MM) | Include | Auto EN complete, 07:44/07:45 | Enclosure thickness, transitions, latch, PCB-driven interfaces. |
| 597 | [Keep Products Consistent](https://www.youtube.com/watch?v=wuoF0xLxZcM) | Include | Auto EN complete, 04:21/04:25 | Product-specific tolerance/cosmetic acceptance criteria. |
| 598 | [Ensure Part Quality](https://www.youtube.com/watch?v=qD0vnoo5kh0) | Include | Auto EN complete, 02:13/02:16 | Requirements-to-QC checklist and batch inspection plan. |

## Promotion boundaries for the knowledge base

The following were deliberately **not** converted into general best practices:

- Uncontrolled break/compression tests as quantitative material or part-strength data.
- Claims that a particular polymer is automatically safe for aquariums, food, skin, children, medicine, heat, or electrical enclosures.
- Exact build volumes, wall thicknesses, clearances, thread dimensions, overhang angles, or material choices that were not supported by a controlled, broadly applicable test.
- Company revenue, market claims, licensing advice, product pricing, printer-farm operations, and vendor/service promotion.
- AI-generated or scan-derived geometry treated as production-ready without manifold, dimensional, interface, and manufacturability checks.
- Orientation changes treated as automatically approved: orientation remains a documented proposal requiring separate user approval and representative validation.
