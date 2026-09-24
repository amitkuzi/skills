# Slant 3D claim extraction: core design and orientation, batch 07

- **Research date:** 2026-09-24
- **Scope:** 25 additional definite-relevance videos from `relevant-video-candidates-2026-09-24.md`, excluding all sources in batches 01-04 and all IDs reserved for batches 05-06.
- **Selection priority:** direct design tutorials and case studies with transferable CAD, orientation, support, assembly, surface, fit, or production-readiness content; remaining broad podcasts and duplicate compilations were not selected.
- **Purpose:** record what Slant 3D actually says before any claim is independently corroborated or converted into a skill rule.
- **Not done here:** independent engineering validation, material/food/electrical/safety approval, or endorsement of sales and service claims.

## Method and evidence limits

For each video, the complete official YouTube original-English automatic-caption track (`en-orig`) was retrieved in JSON3 format and read from its first caption event through its closing spoken content. Official YouTube metadata supplied title, date, duration, and URL. No selected video had a manually authored `en-orig` track; all 25 had full-length automatic-caption coverage.

Claims below are paraphrases. Each claim links to the official video at the point where it is made. “Confidence” measures how clearly the captions support the paraphrase, **not** whether the engineering claim is true.

- **High:** clear spoken claim with an unambiguous timestamp.
- **Medium:** clear general claim whose scope depends on geometry, material, process, or an inferred design intent.
- **Low:** causal, numerical, safety, or performance claim is weakly demonstrated, commercially motivated, or based on an uncontrolled prototype.

Evidence limits:

- Fine on-screen dimensions, CAD sketches, texture settings, flow/thermal results, and physical test data not spoken in the captions were not inferred.
- Audio was not separately human-audited. Ambiguous decimals and units in automatic captions were not converted into rules.
- Descriptions, comments, linked downloads, vendor pages, sales figures, and external sources were not used as engineering evidence.
- Several videos promote Slant 3D/Teleport services. Commercial capacity, cost, sustainability, and fulfillment claims were excluded from CAD guidance.
- Reused footage is identified below and is not counted as independent corroboration.

## Batch manifest

| # | Catalog # | Video | Date | Duration | Primary topics |
|---:|---:|---|---:|---:|---|
| 1 | 86 | [Brims, Rafts & Supports — The RIGHT Way](https://www.youtube.com/watch?v=3AZWuVRUh2c) | 2025-12-08 | 30:10 | CAD brims/rafts/support, removability, portability |
| 2 | 95 | [Designing Everyday Products for 3D Printing](https://www.youtube.com/watch?v=rNTBjT49OqU) | 2025-11-07 | 29:55 | compilation: clocks, chargers, lamps, dispenser, coffee stand |
| 3 | 109 | [Redesigning YouTuber Products for 3D Print on Demand](https://www.youtube.com/watch?v=SiGoPAGXuKM) | 2025-09-20 | 22:48 | compliant hanger, ribs, support replacement, consolidation |
| 4 | 125 | [Perfect Snack Tray for Oreos & Milk](https://www.youtube.com/watch?v=O7uwXBGHN3g) | 2025-07-26 | 5:35 | orientation, customer-facing surfaces, handles, overhangs |
| 5 | 141 | [How We Would Make a Product for Mr. Beast](https://www.youtube.com/watch?v=9ItEMRg8cxg) | 2025-05-31 | 8:04 | print-in-place lunchbox, orientation, texture, cleanable liner |
| 6 | 159 | [Crystal Creek GoReel](https://www.youtube.com/watch?v=eDgY9_JC7sM) | 2025-03-27 | 5:57 | reel geometry, ergonomics, wet grip, color/branding |
| 7 | 182 | [Belt Holster for a ZYN Can](https://www.youtube.com/watch?v=0mti_RY2WnA) | 2025-01-10 | 4:32 | compliant clip orientation, text, bed-edge treatment |
| 8 | 184 | [Turn Your 3D Printed Design into a REAL PRODUCT](https://www.youtube.com/watch?v=AQKGvPmz0eQ) | 2025-01-04 | 22:33 | production preflight, hidden assembly, cost-oriented geometry |
| 9 | 229 | [Scott Yu-Jan's 3D Printed iPhone Dock](https://www.youtube.com/watch?v=b1RBo7f0Zb0) | 2024-09-05 | 8:17 | part consolidation, print-in-place trade-off, modeled texture |
| 10 | 251 | [How to Make a Good Product...with Calculators](https://www.youtube.com/watch?v=MK90srPx8wI) | 2024-07-27 | 29:28 | functional hierarchy, affordance, assembly/manufacturing trade-offs |
| 11 | 255 | [MagSafe Charger Stands](https://www.youtube.com/watch?v=kIFGtNMmxuM) | 2024-07-20 | 5:02 | underside geometry, overhangs, stable ring, texture |
| 12 | 284 | [Minimalist Coffee Stand](https://www.youtube.com/watch?v=Jps5YPF2iRU) | 2024-05-11 | 4:56 | purchased insert, bed seam, designed support, liquid path |
| 13 | 290 | [Create 3D Printed Clocks Easily](https://www.youtube.com/watch?v=Y0bk47STUf0) | 2024-04-30 | 6:18 | self-supporting housing, stable interfaces, controlled variants |
| 14 | 326 | [We Made a Better Football](https://www.youtube.com/watch?v=gPLX-qVDc-o) | 2024-02-14 | 8:40 | internal compliant structure, familiar exterior, unvalidated performance |
| 15 | 330 | [We Made a Better Stanley Cup](https://www.youtube.com/watch?v=hVPvaLmO8bo) | 2024-02-03 | 6:29 | handle transition, insert architecture, internal voids, surface texture |
| 16 | 352 | [Ocado's 3D Printed Robots](https://www.youtube.com/watch?v=gHJtFfH8B88) | 2023-12-18 | 3:22 | topology optimization, lightweighting, MJF case study |
| 17 | 403 | [We Made Dyson's Bladeless Fan for $25](https://www.youtube.com/watch?v=VUjzKhgDdzk) | 2023-08-30 | 7:37 | integrated ducts, module interface, density placement, flow passage |
| 18 | 425 | [452-Piece Snaphouse Building Kit](https://www.youtube.com/watch?v=NUdVFoPgNOU) | 2023-07-21 | 5:12 | system fit, assembly force, orientation consistency, QC |
| 19 | 481 | [Products Using Vase Mode: Bene bFRIENDS](https://www.youtube.com/watch?v=tlol_taTNnU) | 2023-04-27 | 2:53 | continuous-outline structure, intentional layer aesthetic |
| 20 | 489 | [Filament Spools Suck](https://www.youtube.com/watch?v=y9EBTua_lss) | 2023-04-15 | 7:38 | requirements, octagonal flange, corrugated core, assembly stiffness |
| 21 | 506 | [Layer Lines Don't Matter](https://www.youtube.com/watch?v=jIanWhvsWMc) | 2023-03-21 | 4:31 | CAD texture, pattern projection, expectation management |
| 22 | 510 | [3D Printing vs Injection Molding](https://www.youtube.com/watch?v=t0mCGcM2w7g) | 2023-03-11 | 7:11 | process-first design, molded/FDM geometry contrast |
| 23 | 570 | [How To Deal With Overhangs](https://www.youtube.com/watch?v=sZZyOd1iYcM) | 2022-08-12 | 1:38 | model placement, overhang support diagnosis |
| 24 | 591 | [Can 3D Printed Parts be Waterproof?](https://www.youtube.com/watch?v=Yk0I4Tf-E8c) | 2022-05-18 | 3:15 | wall redundancy, defect opportunity, test scope |
| 25 | 613 | [3D Printing vs Injection Molding: Textures](https://www.youtube.com/watch?v=RAn2FP-d21I) | 2021-07-14 | 3:00 | modeled texture, complex surfaces, part consolidation |

## Extracted claims

### 1. Brims, Rafts & Supports — The RIGHT Way

- **Source:** [video](https://www.youtube.com/watch?v=3AZWuVRUh2c), 2025-12-08, 30:10.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-30:10 (last cue 30:07).
- **Claims:**
  - [00:24](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=24s) A generic slicer brim adds removal labor and can mar the part edge; for repeated production, model only the adhesion features actually needed. **Confidence: High.**
  - [03:00](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=180s) Rounded brim outlines avoid peel-prone corners, and a modeled, continuous first-layer region can avoid abrupt perimeter/infill transitions. **Confidence: Medium** because toolpath continuity still depends on the slicer.
  - [05:17](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=317s) Replace a full-sheet brim with a perimeter ring or localized circular “mouse ears” when only the tips/corners need restraint. **Confidence: High.**
  - [06:03](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=363s) Recess the brim contact behind a bottom chamfer so trimming residue does not enlarge the functional outline and the junction provides a deliberate break line. **Confidence: High.**
  - [12:23](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=743s) A modeled raft can define its own rounded footprint, gap, and breakaway links instead of inheriting an unknown slicer profile. **Confidence: High.**
  - [14:24](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=864s) Interrupt long first-layer paths in a raft to reduce continuous shrink paths, while retaining material at its restraint perimeter. **Confidence: Medium;** no controlled comparison is shown.
  - [19:28](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=1168s) The preferred hierarchy is: remove the overhang by orientation/chamfer, prepare an unavoidable local feature for support, then use a purpose-built support body with explicit access and breakaway behavior. **Confidence: High.**
  - [24:03](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=1443s) A support fin needs a broad, stable base and accessible flexible body; sparse one-layer links can stop the part settling into the support while remaining removable. **Confidence: High.**
  - [26:00](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=1560s) Support blocks should be crushable or twistable and may carry visible removal instructions when the customer/post-processor must distinguish them from product geometry. **Confidence: High.**
- **Conditions/exceptions:** CAD-authored ancillary geometry adds model complexity and can lock assumptions about layer height, line width, material expansion, cooling, and machine behavior into the file. Breakaway features require access, safe removal, and inspection. A one-off print may reasonably use generic supports.
- **Internal tension:** The opening calls slicers nearly useless for these features, but [28:01](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=1681s) recommends generating and exporting a support mesh from a slicer as a practical fallback. The video also seeks cross-platform portability while repeatedly requiring test-based spacing changes for particular machines/materials. The portable principle is explicit geometry and verification, not the claim that one geometry is universal.

### 2. Designing Everyday Products for 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=rNTBjT49OqU), 2025-11-07, 29:55.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-29:55 (last cue 29:50).
- **Claims:**
  - [00:33](https://www.youtube.com/watch?v=rNTBjT49OqU&t=33s) Tilting a clock housing’s base can both aim the display and turn an internal horizontal ceiling into a self-supporting slope. **Confidence: High.**
  - [07:02](https://www.youtube.com/watch?v=rNTBjT49OqU&t=422s) A charger stand can use a hollow/conical underside and a stable outer contact ring to remove a broad bed-facing surface while preserving table stability. **Confidence: High.**
  - [11:27](https://www.youtube.com/watch?v=rNTBjT49OqU&t=687s) A lamp intended for a standard, non-vase profile needs its hollow wall explicitly modeled; its base, mounting region, and shade can carry different local thicknesses within one body. **Confidence: High.**
  - [13:01](https://www.youtube.com/watch?v=rNTBjT49OqU&t=781s) Design around the expected seam: place it on a noncritical face, disrupt it with deliberate texture/facets, or make the printed character intentional. **Confidence: High.**
  - [14:31](https://www.youtube.com/watch?v=rNTBjT49OqU&t=871s) A broad flat lamp roof creates a visible overhang/lighting artifact; vary the inner wall thickness or replace the ceiling with an internal chamfer so the roof grows progressively. **Confidence: High.**
  - [20:05](https://www.youtube.com/watch?v=rNTBjT49OqU&t=1205s) The tape-dispenser wedge serves function and manufacture simultaneously: it leads the eye toward the cutting edge, makes the teeth a straight CAD extrusion, and avoids an unsupported shelf. **Confidence: High.**
  - [22:45](https://www.youtube.com/watch?v=rNTBjT49OqU&t=1365s) Crop a nonfunctional sector from a horizontal round roller to create a stable print flat, then support only the remaining small projections with purpose-built breakaways. **Confidence: High.**
  - [26:31](https://www.youtube.com/watch?v=rNTBjT49OqU&t=1591s) When a curved coffee stand must print on its side, reduce the bed interface to a deliberate seam and mirror required support-like points so they read as intentional product geometry. **Confidence: High.**
- **Conditions/exceptions:** Lamp guidance requires thermal, electrical, flammability, optical, and cleaning validation. Bed-contact minimization must not sacrifice adhesion. A cropped roller remains acceptable only if the missing sector never affects rotation or engagement.
- **Internal tension/duplication:** This is a compilation. The clock, charger, and coffee-stand segments substantially repeat videos 13, 11, and 12 below and are not independent corroboration. The lamp segment criticizes vase-mode fragility while video 19 praises continuous-wall vase-mode products; the use cases differ, so neither is a universal rule.

### 3. Redesigning YouTuber Products for 3D Print on Demand

- **Source:** [video](https://www.youtube.com/watch?v=SiGoPAGXuKM), 2025-09-20, 22:48.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-22:48 (last cue 22:43).
- **Claims:**
  - [05:05](https://www.youtube.com/watch?v=SiGoPAGXuKM&t=305s) Begin a folding-hanger redesign from the required folded/open states and print orientation; a tall arm that must rise out of the layer plane needs an added web/shear plate or a different layout. **Confidence: High.**
  - [06:43](https://www.youtube.com/watch?v=SiGoPAGXuKM&t=403s) Offset a hinge axis from the nominal intersection when material trapped inside the fold would otherwise be pinched and prevent parallel closure. **Confidence: High.**
  - [07:31](https://www.youtube.com/watch?v=SiGoPAGXuKM&t=451s) Add small retention bumps only where the hung item would slide under the intended inclined use condition. **Confidence: High.**
  - [11:33](https://www.youtube.com/watch?v=SiGoPAGXuKM&t=693s) When substituting a less costly/weaker material, change the geometry: turn sacrificial support volume into a self-supporting chamfered load path and add local ribs rather than assuming material substitution alone is sufficient. **Confidence: Medium;** no comparative test is shown.
  - [12:53](https://www.youtube.com/watch?v=SiGoPAGXuKM&t=773s) Merge paired wheel brackets when the shared body can provide the missing cross-rib, eliminate duplicate support, and reduce fastener/assembly count. **Confidence: High.**
- **Conditions/exceptions:** Webs and hinge offsets can interfere with the user/load envelope. PETG outdoor suitability and the redesigned parts’ strength are asserted, not tested. Consolidation must preserve service, replacement, wheel spacing, and hardware access.
- **Internal tension/duplication:** The final iPhone-dock segment repeats video 9 rather than providing independent evidence. The statement that “all” strength is in printed walls is an overstatement; load response also depends on geometry, infill, interfaces, material, process, and orientation.

### 4. Perfect Snack Tray for Oreos & Milk

- **Source:** [video](https://www.youtube.com/watch?v=O7uwXBGHN3g), 2025-07-26, 5:35.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:35 (last cue 05:31).
- **Claims:**
  - [01:34](https://www.youtube.com/watch?v=O7uwXBGHN3g&t=94s) Reject an orientation that puts a variable first-layer surface on the customer-facing face; reorient and reshape the edges together rather than treating orientation as a slicer-only choice. **Confidence: High.**
  - [02:05](https://www.youtube.com/watch?v=O7uwXBGHN3g&t=125s) Taper the outside for the intended inclined orientation, open both ends of long cookie bays, and ovalize a large side hole if its upper arc would otherwise sag. **Confidence: High.**
  - [02:31](https://www.youtube.com/watch?v=O7uwXBGHN3g&t=151s) Use a shallow grip recess instead of a through-hole when the hole would unnecessarily cut the load-bearing side tab. **Confidence: High for the shown part.**
  - [03:22](https://www.youtube.com/watch?v=O7uwXBGHN3g&t=202s) Orient/redesign a loaded handle so its primary span is deposited in-plane rather than separated by layer interfaces under bending. **Confidence: High.**
- **Conditions/exceptions:** The proposed food-use object has no food-contact, cleaning, dishwasher, spill, or load test evidence. A recess is not a universal substitute for a through-handle when glove clearance, secure grasp, hanging, or accessibility requires an opening.
- **Internal contradictions:** None material observed; production-scale and food suitability claims remain unsupported.

### 5. How We Would Make a Product for Mr. Beast

- **Source:** [video](https://www.youtube.com/watch?v=9ItEMRg8cxg), 2025-05-31, 8:04.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:04 (last cue 08:01).
- **Claims:**
  - [02:51](https://www.youtube.com/watch?v=9ItEMRg8cxg&t=171s) Consolidate the lid, clips, handle, and hinge into one print-in-place body only if the required colored/cleanable liner remains separable. **Confidence: High.**
  - [04:06](https://www.youtube.com/watch?v=9ItEMRg8cxg&t=246s) Select orientation by considering latch bending, handle bending, hinge-axis continuity, bed contact, and visible-face appearance together; the obvious flat/side orientations may fail different requirements. **Confidence: High.**
  - [05:01](https://www.youtube.com/watch?v=9ItEMRg8cxg&t=301s) The demonstrated orientation keeps latch spines, handle, and hinge axes horizontal/in-plane and uses minimal, symmetric bed contact. **Confidence: High for the shown geometry.**
  - [05:37](https://www.youtube.com/watch?v=9ItEMRg8cxg&t=337s) Use surface noise and recessed/embossed branding as intentional geometry, but keep a crumb-contact liner smooth and removable for cleaning. **Confidence: High.**
- **Conditions/exceptions:** A child-use lunchbox needs hinge-cycle, pinch, small-part, impact, food-contact, cleaning, thermal, and retention validation. Print-in-place mechanisms can trap debris and be difficult to inspect or replace.
- **Internal tension:** “One piece” is used rhetorically, but the demonstrated product is explicitly two printed pieces plus nonprinted functional requirements. The useful claim is selective consolidation, not literal one-piece purity.

### 6. Crystal Creek GoReel

- **Source:** [video](https://www.youtube.com/watch?v=eDgY9_JC7sM), 2025-03-27, 5:57.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:57 (last cue 05:53).
- **Claims:**
  - [00:49](https://www.youtube.com/watch?v=eDgY9_JC7sM&t=49s) Shape the reel flange around the real casting path: a slanted/semi-triangular side lets line exit rather than copying a symmetric storage spool. **Confidence: Medium;** performance is explained but not tested.
  - [01:11](https://www.youtube.com/watch?v=eDgY9_JC7sM&t=71s) Turn lightening holes into ergonomic finger features so the same voids reduce material and support one-handed casting. **Confidence: High.**
  - [01:46](https://www.youtube.com/watch?v=eDgY9_JC7sM&t=106s) Design from a problem the creator understands, then add deliberate exterior grip texture where hands are expected to be wet or muddy. **Confidence: Medium.**
  - [02:22](https://www.youtube.com/watch?v=eDgY9_JC7sM&t=142s) Multicolor branding can constrain throughput; consider same-material relief/texture branding when color changes are not functionally necessary. **Confidence: Medium;** the production penalty is system dependent.
- **Conditions/exceptions:** Grip texture can trap dirt and affect cleaning. Casting, abrasion, UV/water exposure, line damage, and one-handed safety require representative testing.
- **Internal contradictions:** None material observed. “Lightweight because printed” is not universal and depends on material/geometry.

### 7. Belt Holster for a ZYN Can

- **Source:** [video](https://www.youtube.com/watch?v=0mti_RY2WnA), 2025-01-10, 4:32.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:32 (last cue 04:28).
- **Claims:**
  - [00:57](https://www.youtube.com/watch?v=0mti_RY2WnA&t=57s) Print a compliant belt/can clip on its side so the flexing arms bend within deposited layers rather than opening layer interfaces. **Confidence: High for the shown clip.**
  - [01:22](https://www.youtube.com/watch?v=0mti_RY2WnA&t=82s) Put small text/logo detail on a vertical sidewall when that orientation gives a clearer repeated outline than a top/first-layer mark. **Confidence: Medium;** feature resolution is process dependent.
  - [02:09](https://www.youtube.com/watch?v=0mti_RY2WnA&t=129s) Chamfer the bed-facing outline to isolate first-layer expansion and round/curve the opposite exposed edges so the top does not read as one broad flat raster surface. **Confidence: High.**
- **Conditions/exceptions:** Compliance, creep, fatigue, belt thickness, can retention, accidental release, and skin contact must be tested. The video’s depth recommendation for text is not portable.
- **Internal tension:** It says compliance makes tolerance setup easy, but compliant interfaces still require force, wear, creep, dimensional-variation, and over-travel validation.

### 8. Turn Your 3D Printed Design into a REAL PRODUCT

- **Source:** [video](https://www.youtube.com/watch?v=AQKGvPmz0eQ), 2025-01-04, 22:33.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-22:33 (last cue 22:28).
- **Claims:**
  - [03:03](https://www.youtube.com/watch?v=AQKGvPmz0eQ&t=183s) A presentation prototype is not production-ready: inspect hidden glue, cable routing, assembly access, button feel, and other “demo-only” shortcuts before release. **Confidence: High.**
  - [04:25](https://www.youtube.com/watch?v=AQKGvPmz0eQ&t=265s) For recurring-cost reduction, simplify the first layer, reduce unnecessary surface area/size/material, and avoid complex internal geometry that adds time without function. **Confidence: High.**
  - [07:05](https://www.youtube.com/watch?v=AQKGvPmz0eQ&t=425s) Product variants that fit different phones/cases must be listed and verified as distinct interfaces rather than implied to be universal. **Confidence: High.**
  - [10:37](https://www.youtube.com/watch?v=AQKGvPmz0eQ&t=637s) Order production-intent samples and verify color, quality, third-party components, and interface match before connecting the design to fulfillment. **Confidence: High.**
- **Conditions/exceptions:** “Minimize” does not mean smallest/lightest at the expense of strength, stability, ergonomics, or service. Most of the video concerns marketing/pricing rather than CAD and was not extracted.
- **Internal tension:** It urges quick launch before perfection while also requiring manufacturability, fit variants, supplier quality, and honest presentation. The reconciled gate is a minimum safe/functional/inspectable product, not an unfinished geometry.

### 9. Scott Yu-Jan's 3D Printed iPhone Dock

- **Source:** [video](https://www.youtube.com/watch?v=b1RBo7f0Zb0), 2024-09-05, 8:17.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:17 (last cue 08:14).
- **Claims:**
  - [02:44](https://www.youtube.com/watch?v=b1RBo7f0Zb0&t=164s) Before scaling, review every separately placed printed component for consolidation; the dock’s loose eject button is proposed as a print-in-place candidate. **Confidence: Medium;** it is a critique, not a validated redesign.
  - [03:10](https://www.youtube.com/watch?v=b1RBo7f0Zb0&t=190s) A print-in-place sliding button trades assembly reduction against clearance, upper/lower surface quality, and smooth motion; it may be less crisp than a separate part. **Confidence: High.**
  - [03:41](https://www.youtube.com/watch?v=b1RBo7f0Zb0&t=221s) When mass-producing, aggregate related printable pieces into one controlled print only when doing so preserves motion and quality; purchased chargers still require downstream assembly. **Confidence: High.**
  - [04:28](https://www.youtube.com/watch?v=b1RBo7f0Zb0&t=268s) If slicer-applied texture is unavailable or nonportable, model slots, waves, or projected texture into CAD, accepting a larger/heavier mesh. **Confidence: High.**
- **Conditions/exceptions:** Consolidation is not beneficial if it prevents repair, color/material separation, inspection, or smooth motion. Dense modeled texture increases file/meshing cost and can alter fit or cleaning.
- **Internal tension:** The speaker recommends print-in-place consolidation while openly acknowledging that it may reduce crispness and motion quality. This is a trade study, not a default instruction.

### 10. How to Make a Good Product...with Calculators

- **Source:** [video](https://www.youtube.com/watch?v=MK90srPx8wI), 2024-07-27, 29:28.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-29:28 (last cue 29:22).
- **Claims:**
  - [01:08](https://www.youtube.com/watch?v=MK90srPx8wI&t=68s) Define four design gates before refinement: the product solves the user’s problem, communicates use through form, is pleasant to keep/use, and can be manufactured profitably. **Confidence: High as the presenter’s framework.**
  - [05:05](https://www.youtube.com/watch?v=MK90srPx8wI&t=305s) Size, color, and position controls according to frequency/importance; visual symmetry should not make the primary action harder to find or operate. **Confidence: High.**
  - [08:00](https://www.youtube.com/watch?v=MK90srPx8wI&t=480s) A bent display housing may improve viewing but require a cable/two-board arrangement; a shaped exterior base can create viewing angle while retaining a flat internal board. **Confidence: Medium;** internals are inferred from products, not disassembled.
  - [20:00](https://www.youtube.com/watch?v=MK90srPx8wI&t=1200s) Exterior texture, edge transitions, color contrast, and grip/angle geometry are manufacturing decisions as well as styling decisions. **Confidence: High.**
  - [21:35](https://www.youtube.com/watch?v=MK90srPx8wI&t=1295s) Screws may self-center and be easier to automate/service than snaps; snaps can remove hardware but risk damage during assembly. Select the joint from the assembly/service requirement, not part-count ideology. **Confidence: Medium.**
- **Conditions/exceptions:** This is general product-design commentary, not an FDM demonstration. Human-factors conclusions require target-user testing; inferred PCB and assembly layouts were not verified.
- **Internal tension:** The speaker first criticizes screws/part count, then gives a plausible reason to prefer screws. The useful conclusion is explicit assembly trade-off analysis.

### 11. MagSafe Charger Stands

- **Source:** [video](https://www.youtube.com/watch?v=kIFGtNMmxuM), 2024-07-20, 5:02.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:02 (last cue 04:56).
- **Claims:**
  - [00:51](https://www.youtube.com/watch?v=kIFGtNMmxuM&t=51s) Start from the charger’s functional interfaces: seating angle, charger pocket, and cable exit, then shape the body around them. **Confidence: High.**
  - [01:08](https://www.youtube.com/watch?v=kIFGtNMmxuM&t=68s) Replace a broad solid underside with a self-supporting conical cavity and outer contact ring so the stand remains level while reducing warp-sensitive bed area. **Confidence: High.**
  - [01:43](https://www.youtube.com/watch?v=kIFGtNMmxuM&t=103s) Add ribs/spirals/texture to break up a large plain cylindrical surface where layer variation would be visually conspicuous. **Confidence: High.**
- **Conditions/exceptions:** A reduced contact ring still needs adequate adhesion and table stability. Charger heat, cable strain, magnet retention, device/case variation, and electrical clearance require validation.
- **Internal contradictions:** None material observed. Claims about automatic ejection and very high volume are service-specific.

### 12. Minimalist Coffee Stand

- **Source:** [video](https://www.youtube.com/watch?v=Jps5YPF2iRU), 2024-05-11, 4:56.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:56 (last cue 04:50).
- **Claims:**
  - [00:14](https://www.youtube.com/watch?v=Jps5YPF2iRU&t=14s) Do not consolidate across a requirement boundary: keep a standard metal coffee filter as a removable purchased component while printing the structural stand around its interface. **Confidence: High.**
  - [01:24](https://www.youtube.com/watch?v=Jps5YPF2iRU&t=84s) If a curved part must print on its side, create a narrow, intentional bed seam so the bed texture is not a broad customer-facing surface. **Confidence: High.**
  - [02:20](https://www.youtube.com/watch?v=Jps5YPF2iRU&t=140s) A side-printed filter cradle needs modeled support or self-supporting teeth where the top would otherwise sag; mirror the geometry so the accommodation reads as deliberate. **Confidence: High.**
  - [03:03](https://www.youtube.com/watch?v=Jps5YPF2iRU&t=183s) Shape contact points around the desired liquid path, using pointed stand-offs to reduce wet contact and guide drips toward the filter tip. **Confidence: Medium;** flow is explained, not measured.
- **Conditions/exceptions:** Food-contact, heat, cleaning, bacterial retention, liquid leakage, stability, filter compatibility, and failure under a hot filled vessel require authoritative validation. A metal insert is acceptable only if reliably sourced and retained.
- **Internal tension:** The video generally favors consolidation but correctly keeps the food-contact filter separate. This supports requirement-driven consolidation, not maximum consolidation.

### 13. Create 3D Printed Clocks Easily

- **Source:** [video](https://www.youtube.com/watch?v=Y0bk47STUf0), 2024-04-30, 6:18.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-06:18 (last cue 06:12).
- **Claims:**
  - [00:34](https://www.youtube.com/watch?v=Y0bk47STUf0&t=34s) A slight housing tilt can aim the display and eliminate an unsupported horizontal internal channel. **Confidence: High.**
  - [01:45](https://www.youtube.com/watch?v=Y0bk47STUf0&t=105s) Iterate body proportions from observed stability/interaction feedback while preserving the proven purchased-clock interface. **Confidence: High.**
  - [02:33](https://www.youtube.com/watch?v=Y0bk47STUf0&t=153s) Carry forward validated features—stable back, insert position, self-supporting slope—when creating cosmetic variants rather than making unrelated files. **Confidence: High.**
  - [03:06](https://www.youtube.com/watch?v=Y0bk47STUf0&t=186s) Added decorative protrusions should remain self-supporting and should not disturb the common functional core. **Confidence: High.**
- **Conditions/exceptions:** A product-family strategy needs controlled parameters, versioning, interface tests, and SKU management. Customer preference is not evidence of mechanical safety.
- **Internal contradictions:** None material observed; rapid “hundreds of variants” claims are business rhetoric, not a CAD-quality measure.

### 14. We Made a Better Football

- **Source:** [video](https://www.youtube.com/watch?v=gPLX-qVDc-o), 2024-02-14, 8:40.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:40 (last cue 08:38).
- **Claims:**
  - [02:42](https://www.youtube.com/watch?v=gPLX-qVDc-o&t=162s) A distributed internal compliant structure is proposed to replace one pneumatic cavity with many local spring paths while controlling mass. **Confidence: Medium as a design concept; performance is unvalidated.**
  - [04:16](https://www.youtube.com/watch?v=gPLX-qVDc-o&t=256s) Preserve familiar exterior size, texture, seam cues, laces, and mass when introducing a radically different interior so the user interface does not change simultaneously with the mechanism. **Confidence: High as stated design intent.**
  - [06:42](https://www.youtube.com/watch?v=gPLX-qVDc-o&t=402s) Once the baseline interface is validated, internal compliance and exterior texture could be parameterized for distinct training loads/conditions. **Confidence: Low;** no validation or rules compliance is shown.
- **Conditions/exceptions:** Ball rebound, aerodynamics, mass distribution, durability, temperature response, impact safety, league rules, and material aging require controlled testing. No lattice dimensions or force-deflection evidence is provided.
- **Internal tension:** The video says not to radically change user-facing behavior, then proposes adjustable mass, texture, and condition simulation. Those are later variants, not proof that the demonstrated baseline is equivalent.

### 15. We Made a Better Stanley Cup

- **Source:** [video](https://www.youtube.com/watch?v=hVPvaLmO8bo), 2024-02-03, 6:29.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-06:29 (last cue 06:28).
- **Claims:**
  - [00:27](https://www.youtube.com/watch?v=hVPvaLmO8bo&t=27s) Blend the handle broadly into the vessel wall, enlarge the grip/load section, and use a self-supporting lower transition rather than copying a straight molded overhang. **Confidence: High as a geometry critique.**
  - [01:29](https://www.youtube.com/watch?v=hVPvaLmO8bo&t=89s) Separate food-contact/cleaning requirements into a removable stainless liner and use the printed body for insulation, grip, and appearance. **Confidence: High.**
  - [02:10](https://www.youtube.com/watch?v=hVPvaLmO8bo&t=130s) Internal voids/infill are proposed as a way to lengthen heat-transfer paths without making the full section solid. **Confidence: Medium;** no thermal comparison is supplied.
  - [04:18](https://www.youtube.com/watch?v=hVPvaLmO8bo&t=258s) Modeled/process texture can differentiate the exterior without paint and make the deposited surface intentional. **Confidence: High.**
- **Conditions/exceptions:** Liner fit, condensation, trapped liquid, cleaning, heat/creep, grip load, and food-contact boundaries need validation. Material and thermal claims are not established by the video.
- **Internal tension:** The video claims PETG handles normal temperatures and that the printed body is superior to metal based partly on an impact stunt. Neither establishes safe hot-liquid use, thermal performance, or product life.

### 16. Ocado's 3D Printed Robots

- **Source:** [video](https://www.youtube.com/watch?v=gHJtFfH8B88), 2023-12-18, 3:22.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-03:22 (last cue 03:21).
- **Claims:**
  - [00:10](https://www.youtube.com/watch?v=gHJtFfH8B88&t=10s) Treat mass as a system-level requirement: lighter moving structures can reduce motor/energy/infrastructure demand downstream. **Confidence: Medium;** the reported multiplier is not independently verified.
  - [01:03](https://www.youtube.com/watch?v=gHJtFfH8B88&t=63s) In topology optimization, define load/interface regions and allowable space, then remove material not contributing to the required load path. **Confidence: High as a qualitative explanation.**
  - [01:34](https://www.youtube.com/watch?v=gHJtFfH8B88&t=94s) Apply lightweighting to the whole moving assembly, including wheels, rather than optimizing one isolated bracket. **Confidence: Medium.**
- **Conditions/exceptions:** The case uses MJF nylon, not FDM; direct geometry transfer requires FDM orientation, minimum-feature, surface, fatigue, fastener, inspection, and support checks. Topology-optimized output still needs smoothing/parameterization and validation.
- **Internal contradictions:** None material observed. “Five times lighter,” energy, and cost assertions were not promoted as validated facts.

### 17. We Made Dyson's Bladeless Fan for $25

- **Source:** [video](https://www.youtube.com/watch?v=VUjzKhgDdzk), 2023-08-30, 7:37.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-07:37 (last cue 07:34).
- **Claims:**
  - [02:06](https://www.youtube.com/watch?v=VUjzKhgDdzk&t=126s) Consolidate internal ducts, airfoil shell, and distribution channels into one body where additive access removes the need for separately stamped/molded passage components. **Confidence: High as a design strategy.**
  - [02:48](https://www.youtube.com/watch?v=VUjzKhgDdzk&t=168s) Start from a standard purchased blower and model an explicit insertion cavity/interface around it; keep the exterior and flow passages separate in the requirement model. **Confidence: High.**
  - [04:35](https://www.youtube.com/watch?v=VUjzKhgDdzk&t=275s) Place extra mass/density low in a tall product only where it improves stability, instead of increasing density uniformly. **Confidence: Medium.**
  - [05:17](https://www.youtube.com/watch?v=VUjzKhgDdzk&t=317s) A constant-width internal manifold produced uneven discharge in the prototype; taper/area variation should be engineered from the pressure/flow target rather than copied uniformly. **Confidence: High as an observed design defect.**
- **Conditions/exceptions:** This was a 24-hour concept. Airflow, noise, motor cooling, electrical safety, tip stability, ingress, guards, pressure losses, and manufacturability were not validated. Integrated ducts can become impossible to inspect/clean/repair.
- **Internal tension:** The video presents a “one piece plus motor” success while acknowledging uneven airflow and a missing industrial-design/engineering pass. It is a prototype lesson, not a finished-fan design.

### 18. 452-Piece Snaphouse Building Kit

- **Source:** [video](https://www.youtube.com/watch?v=NUdVFoPgNOU), 2023-07-21, 5:12.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:12 (last cue 05:05).
- **Claims:**
  - [00:42](https://www.youtube.com/watch?v=NUdVFoPgNOU&t=42s) For a kit with many interconnecting types, validate the interface system across every part family, not one nominal mating pair. **Confidence: High.**
  - [01:08](https://www.youtube.com/watch?v=NUdVFoPgNOU&t=68s) Iterate fit geometry against process expansion/variation, then create a repeatable certification/inspection method for parts leaving production. **Confidence: High.**
  - [02:01](https://www.youtube.com/watch?v=NUdVFoPgNOU&t=121s) Use a common orientation when consistent visible texture across the kit is important, but compensate interfaces that become weaker or stiffer in that orientation. **Confidence: High.**
  - [02:34](https://www.youtube.com/watch?v=NUdVFoPgNOU&t=154s) Define required insertion/removal force explicitly; loosen selected fits to keep perceived interaction consistent when orientation changes structural response. **Confidence: High.**
  - [03:05](https://www.youtube.com/watch?v=NUdVFoPgNOU&t=185s) Approve assembled sample sets after several iterations before releasing thousands of mutually dependent pieces. **Confidence: High.**
- **Conditions/exceptions:** Kit interfaces need tolerance-stack, wear/cycle, breakage, small-part/choking, material, color, and assembly-error evaluation. “Certification” here is an internal process term, not evidence of regulatory certification.
- **Internal contradictions:** None material observed; exact expansion/force values are absent.

### 19. Products Using Vase Mode: Bene bFRIENDS

- **Source:** [video](https://www.youtube.com/watch?v=tlol_taTNnU), 2023-04-27, 2:53.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-02:53 (last cue 02:48).
- **Claims:**
  - [00:48](https://www.youtube.com/watch?v=tlol_taTNnU&t=48s) Treat a coarse deposited layer as the intended surface language rather than imitating a smooth molded object. **Confidence: High.**
  - [01:09](https://www.youtube.com/watch?v=tlol_taTNnU&t=69s) Design organization walls/compartments as one continuous outline so the same path provides structure, separation, and appearance. **Confidence: High as the described strategy.**
  - [01:53](https://www.youtube.com/watch?v=tlol_taTNnU&t=113s) A family of variants can share the continuous-wall grammar while changing the outline/compartment layout. **Confidence: Medium.**
- **Conditions/exceptions:** Continuous single-wall objects can be vulnerable to impact, seam defects, leakage, top/bottom transition problems, and local loads. Tool width, layer height, path continuity, and slicer behavior must match the modeled outline.
- **Internal tension:** Video 2 calls vase-mode lamp geometry delicate, while this video presents continuous-wall organizers as premium production products. The difference is load case and required durability; neither statement is universal.

### 20. Filament Spools Suck

- **Source:** [video](https://www.youtube.com/watch?v=y9EBTua_lss), 2023-04-15, 7:38.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-07:38 (last cue 07:31).
- **Claims:**
  - [00:11](https://www.youtube.com/watch?v=y9EBTua_lss&t=11s) Start from the actual logistics/use cycle—disposable consumer spool rather than reusable local industrial spool—before preserving legacy geometry. **Confidence: High.**
  - [04:17](https://www.youtube.com/watch?v=y9EBTua_lss&t=257s) Use octagonal flat-sided flanges when shelf stability/packing is more important than rolling on the outer rim; retain a compatible circular inner running surface where machines use the core. **Confidence: High.**
  - [04:42](https://www.youtube.com/watch?v=y9EBTua_lss&t=282s) Remove the unnecessary inner ring/infill and keep material mainly at the winding surface and flange interfaces. **Confidence: High as stated intent.**
  - [05:07](https://www.youtube.com/watch?v=y9EBTua_lss&t=307s) Corrugate the core wall to create section depth and compliance with little material; attaching both flanges then braces the flexible core into a stiffer assembly. **Confidence: Medium;** no load/creep/shipping test is shown.
- **Conditions/exceptions:** An octagonal flange is incompatible with rim rollers. Core buckling, winding pressure, filament snagging, humidity, flange adhesive, shipping loads, spool-holder interfaces, recycling streams, and concentricity need validation.
- **Internal tension:** The design rejects reusable spools primarily on user/logistics assumptions; those assumptions can differ in closed-loop or local systems.

### 21. Layer Lines Don't Matter

- **Source:** [video](https://www.youtube.com/watch?v=jIanWhvsWMc), 2023-03-21, 4:31.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:31 (last cue 04:28).
- **Claims:**
  - [01:29](https://www.youtube.com/watch?v=jIanWhvsWMc&t=89s) For portable production, create a texture patch in CAD and pattern/project it across the intended surface rather than depending entirely on a slicer effect. **Confidence: High.**
  - [01:46](https://www.youtube.com/watch?v=jIanWhvsWMc&t=106s) Curved-surface texture can be computationally expensive and difficult to pattern without visible repetition; generative/randomized construction can reduce obvious tiling. **Confidence: High.**
  - [03:30](https://www.youtube.com/watch?v=jIanWhvsWMc&t=210s) Use surface language that matches the process; a molded-looking smooth design makes residual bands look unintended, while deliberate texture changes the expectation. **Confidence: High.**
- **Conditions/exceptions:** Texture can change dimensions, friction, sealing, cleaning, visibility, tactile response, and file size. It masks or reframes surface variation; it does not fix dimensional, bonding, or structural defects.
- **Internal tension:** The title says layer lines do not matter, but the video devotes most of its guidance to hiding or replacing their appearance. The portable conclusion is that acceptability is product-specific and should be designed intentionally. Absolute claims that molding cannot use texture are unsupported.

### 22. 3D Printing vs Injection Molding: From Design to Price

- **Source:** [video](https://www.youtube.com/watch?v=t0mCGcM2w7g), 2023-03-11, 7:11.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-07:11 (last cue 07:09).
- **Claims:**
  - [00:27](https://www.youtube.com/watch?v=t0mCGcM2w7g&t=27s) Select the intended production process before final CAD; a model optimized for molding should not be treated as automatically optimized for FDM, and vice versa. **Confidence: High.**
  - [00:51](https://www.youtube.com/watch?v=t0mCGcM2w7g&t=51s) The molded cube example adds draft, removes the solid center, controls walls, and rounds edges; the FDM version can retain a thick/closed volume because internal fill is process-generated. **Confidence: Medium;** the spoken “fully solid” wording is ambiguous relative to infill.
  - [05:45](https://www.youtube.com/watch?v=t0mCGcM2w7g&t=345s) When producing in batches, preserve the ability to update the model between releases instead of freezing all inventory before user feedback. **Confidence: High as a production strategy.**
- **Conditions/exceptions:** Draft, wall, infill, and edge rules depend on part function and the chosen molding/FDM process. The side-by-side quote is one proprietary scenario; it is not a general cost crossover.
- **Internal tension:** The video uses a very simple cube to argue broad process economics while acknowledging at [06:34](https://www.youtube.com/watch?v=t0mCGcM2w7g&t=394s) that geometry can radically change the result. Pricing and lead-time numbers were not promoted.

### 23. How To Deal With Overhangs

- **Source:** [video](https://www.youtube.com/watch?v=sZZyOd1iYcM), 2022-08-12, 1:38.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-01:38 (last cue 01:33).
- **Claims:**
  - [00:12](https://www.youtube.com/watch?v=sZZyOd1iYcM&t=12s) Unsupported downward details require either support or a geometry/orientation redesign; a slicer cannot recover material that starts in free space. **Confidence: High.**
  - [00:47](https://www.youtube.com/watch?v=sZZyOd1iYcM&t=47s) Stair-stepped support under an intended flat datum can indicate that the imported model was slightly tilted; inspect placement and seat the intended datum flush before adding support. **Confidence: High.**
- **Conditions/exceptions:** “Lay flat” is correct only when that datum also satisfies strength, visible surface, fit, and support requirements. The video is primarily slicer diagnosis, not a production CAD tutorial.
- **Internal tension:** It recommends generic slicer support, unlike video 1’s production preference for modeled support. The contexts differ: beginner repair/one-off versus repeatable manufacturing.

### 24. Can 3D Printed Parts be Waterproof?

- **Source:** [video](https://www.youtube.com/watch?v=Yk0I4Tf-E8c), 2022-05-18, 3:15.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-03:15 (last cue 03:10).
- **Claims:**
  - [00:43](https://www.youtube.com/watch?v=Yk0I4Tf-E8c&t=43s) Do not assume all layered parts leak; define the actual requirement—floating, low-pressure containment, immersion, or pressure—then validate the complete part. **Confidence: Medium;** the examples are asserted, not documented.
  - [01:24](https://www.youtube.com/watch?v=Yk0I4Tf-E8c&t=84s) Multiple perimeter paths/wall thickness add redundant barriers so one local bead defect is less likely to create a through leak. **Confidence: Medium.**
  - [02:00](https://www.youtube.com/watch?v=Yk0I4Tf-E8c&t=120s) Larger shells create more opportunities for an isolated defect, so watertightness risk and inspection burden can grow with path length/area. **Confidence: High as qualitative risk reasoning.**
- **Conditions/exceptions:** Material permeability, seams, start/stop locations, under-extrusion, wall paths, layer bonding, fittings, pressure, time, temperature, chemicals, and test method matter. No pressure, duration, sample count, or failure data is supplied.
- **Internal tension:** The opening gives an absolute “yes,” while the second half says high pressure and larger parts are difficult. The usable claim is requirement-specific testing, not universal waterproofness.

### 25. 3D Printing vs Injection Molding: Manufacturing Textures

- **Source:** [video](https://www.youtube.com/watch?v=RAn2FP-d21I), 2021-07-14, 3:00.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-03:00 (last cue 02:57).
- **Claims:**
  - [00:14](https://www.youtube.com/watch?v=RAn2FP-d21I&t=14s) Model surface texture as part geometry when it is required on multiple faces or complex forms, rather than treating it as a post-process decoration. **Confidence: High.**
  - [01:00](https://www.youtube.com/watch?v=RAn2FP-d21I&t=60s) Additive manufacture can carry fine texture around several faces without splitting the product into flat molded panels solely for tool access. **Confidence: Medium.**
  - [02:02](https://www.youtube.com/watch?v=RAn2FP-d21I&t=122s) Part consolidation can avoid fold/assembly seams introduced only to make textured faces tool-accessible. **Confidence: Medium.**
- **Conditions/exceptions:** Texture must respect minimum feature resolution, mesh size, wall thickness, dimensional interfaces, cleaning, friction, support, and orientation. Molding can produce texture using appropriate tooling; comparative cost/feasibility is geometry- and process-specific.
- **Internal tension:** “Whatever you can do in CAD can be printed” and “impossible to injection mold” are unsupported absolutes. Treat the video as a complexity/tool-access comparison, not a universal process claim.

## Cross-video contradictions and reconciliations

1. **Slicer independence vs slicer fallback.** Video 1 argues that support/brim/raft intent belongs in CAD for portability, then recommends exporting a support mesh from a slicer. Reconciliation: persist verified geometry when repeatability matters; the tool used to author that geometry can still be a slicer.
2. **Universal geometry vs machine/material tuning.** Video 1 promotes one uploaded model across systems but repeatedly says gaps and breakaways must be tested for the actual material/machine. Reconciliation: preserve intent in geometry, but do not assume universal clearance or layer-dependent features.
3. **Minimal bed contact vs deliberate adhesion features.** Videos 4, 5, 11, and 12 minimize visible/automated bed contact; video 1 deliberately adds brims/rafts. Reconciliation: use the least contact that satisfies adhesion, orientation, appearance, and removal risk—not minimum or maximum as an absolute.
4. **Consolidate everything vs preserve requirement boundaries.** Videos 3, 5, 9, and 17 favor consolidation; videos 12 and 15 retain metal/cleanable inserts, and video 9 retains purchased chargers. Reconciliation: consolidate printed structure only while preserving material, maintenance, cleaning, color, inspection, and replacement boundaries.
5. **Vase mode is premium vs vase mode is delicate.** Video 19 praises continuous-wall office products; video 2 calls vase-mode lamp parts weak/delicate. Reconciliation: continuous-wall geometry is application-specific and must be validated for load, impact, top/bottom closure, seam, and safety.
6. **Layer lines do not matter vs extensive masking guidance.** Videos 5, 6, 9, 11, 15, 19, 21, and 25 all manipulate layer appearance. Reconciliation: layer texture is not inherently defective, but it matters whenever it conflicts with the intended surface, cleaning, optics, grip, or customer expectation.
7. **Beginner support vs production support.** Video 23 recommends enabling slicer support to rescue a one-off model; video 1 rejects generic support for repeatable production. The user, volume, and evidence requirements differ.
8. **One-piece rhetoric vs real assemblies.** Videos 5, 9, 12, 15, and 17 all keep purchased parts, liners, motors, filters, or chargers. “One piece” should mean eliminate unnecessary printed assembly, not erase functional interfaces.

## Unsupported or nonportable numeric heuristics

The following spoken numbers were captured but **must not be promoted as universal skill defaults** without independent tests and clear units:

| Video | Timestamp | Spoken heuristic | Why not portable |
|---|---:|---|---|
| Brims, Rafts & Supports | [02:17](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=137s) | Brim stated as “2” to “.3” thick | Automatic captions likely dropped a decimal; depends on layer height/profile. |
| Brims, Rafts & Supports | [06:03](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=363s) | 0.5 mm bottom chamfer | Depends on first-layer expansion, tolerance, line width, removal method. |
| Brims, Rafts & Supports | [12:52](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=772s) | Raft gap approximately one layer / “.2” | Layer height, material, cooling, and support-interface behavior vary. |
| Brims, Rafts & Supports | [13:36](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=816s) | 1 mm raft breakaway struts | Strength/removal depends on material, count, orientation, and toolpath. |
| Brims, Rafts & Supports | [16:42](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=1002s) | One-layer 0.4-0.5 mm “Velcro” interface | Caption/units are ambiguous and profile-specific. |
| Brims, Rafts & Supports | [22:12](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=1332s) | 2-3 mm designed-support spacing | Far larger than typical layer-scale interfaces; geometry/material context is unclear. |
| Brims, Rafts & Supports | [24:35](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=1475s) | 0.5 mm thick, 0.5-1 mm wide support-fin links | Tool width, material, number of links, load, and removal access vary. |
| Brims, Rafts & Supports | [25:54](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=1554s) | Most machines bridge 1-2 inches | Machine, material, cooling, speed, strand count, and quality target vary greatly. |
| Brims, Rafts & Supports | [26:08](https://www.youtube.com/watch?v=3AZWuVRUh2c&t=1568s) | 0.2-0.3 clearance around support block | Material/process/interface-area dependent; caption decimals uncertain. |
| Everyday Products | [11:31](https://www.youtube.com/watch?v=rNTBjT49OqU&t=691s) | Lamp wall no thicker than about 1 mm | Optical, strength, heat, material/color, and path count vary. |
| Everyday Products | [12:50](https://www.youtube.com/watch?v=rNTBjT49OqU&t=770s) | 25% infill, 0.2 mm layers, two walls | A service-specific prototype profile, not slicer-agnostic CAD guidance. |
| Everyday Products / Coffee Stand | [25:46](https://www.youtube.com/watch?v=rNTBjT49OqU&t=1546s) | 3-5% infill | Depends on geometry, load, material, process, and required life. |
| YouTuber Redesigns | [06:43](https://www.youtube.com/watch?v=SiGoPAGXuKM&t=403s) | Hinge raised about one centimeter | Product-specific clearance for folded fabric. |
| Belt Holster | [01:27](https://www.youtube.com/watch?v=0mti_RY2WnA&t=87s) | Text/logo about 0.5 mm deep | Depends on font, orientation, tool width, surface, and viewing distance. |
| Football | [00:14](https://www.youtube.com/watch?v=gPLX-qVDc-o&t=14s) | Regulation pressure and claimed equivalence | Sports-performance claim lacks controlled test/rules evidence. |
| Waterproof Parts | [02:14](https://www.youtube.com/watch?v=Yk0I4Tf-E8c&t=134s) | Keep pressure vessels “not bigger than a fist” | No pressure, wall, material, time, or sample data; size is not the governing requirement alone. |

Other cost, price, volume, energy, weight-reduction, and capacity numbers in these videos were outside CAD scope or unsupported by accessible primary evidence and were not promoted.

## Validation summary

- Manifest entries: **25**.
- Video sections: **25**.
- Complete-caption access statements: **25/25**.
- Selected video IDs overlapping batches 01-04: **0**.
- Selected video IDs overlapping reserved batches 05-06: **0**.
- Every extracted claim has a timestamped official-video link and confidence label.
- Every video section records conditions/exceptions and contradiction/tension status.
- Reused compilation footage is labeled and not treated as independent corroboration.
- Ambiguous numerical rules promoted as universal guidance: **0**.
- Independent corroboration performed: **none**.
