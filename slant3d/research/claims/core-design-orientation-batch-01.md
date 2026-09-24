# Slant 3D claim extraction: core design and orientation, batch 01

- **Research date:** 2026-09-24
- **Scope:** 25 high-signal videos selected from the definite candidates in `relevant-video-candidates-2026-09-24.md`.
- **Purpose:** capture what Slant 3D actually says about CAD geometry, orientation, support, holes, fillets/chamfers, walls, strength, tolerances, and production preparation.
- **Not done here:** independent engineering corroboration, endorsement, or conversion of the claims into skill rules.

## Method and evidence limits

For every video below, the complete official YouTube English automatic-caption track (`en-orig`) was read from the first caption event through the end of the video. Official YouTube metadata supplied the title, publication date, duration, and URL. The caption files were used transiently and were deleted after extraction; no full transcript is reproduced or retained in this document.

Claims are paraphrased rather than quoted. Each claim links to the point in the official video where it is stated. "Confidence" means confidence that the paraphrase accurately reflects the video, **not** confidence that the engineering claim is true.

Confidence scale:

- **High:** clear spoken claim with an unambiguous timestamp.
- **Medium:** clear general claim, but its scope depends on the shown geometry/process, or automatic captions make a number/unit uncertain.
- **Low:** important numerical or causal claim is ambiguous or internally inconsistent in the accessible caption evidence.

The following evidence was not accessible or not used:

- Manually authored captions were not published for these videos; the accessible track was YouTube automatic captions.
- Some player UIs reported captions unavailable even though YouTube's official caption endpoint exposed `en-orig`; therefore the endpoint track, not the player transcript panel, was used.
- Fine on-screen CAD dimensions, labels, force readouts, and geometry details that were not spoken are not captured here.
- Audio was not separately human-audited. Decimal points and units are therefore treated cautiously where automatic captions were ambiguous.
- Comments, sponsor/service claims, linked downloads, and external web pages were not used as engineering evidence.

## Batch manifest

All 25 videos had full-length automatic-caption coverage.

| # | Video | Date | Duration | Primary topics |
|---:|---|---:|---:|---|
| 1 | [The Seven Deadly Sins of 3D Printing](https://www.youtube.com/watch?v=iiCsQIN_PyQ) | 2026-08-21 | 11:56 | first layer, fillets/chamfers, slicer independence, microfeatures, support |
| 2 | [10 Ways to Make Perfect 3D Printed Holes](https://www.youtube.com/watch?v=3BIvSiuQVWQ) | 2026-06-26 | top-facing holes, lead-ins, reinforcement, compliance |
| 3 | [How to Design Better Support Fins for 3D Printing](https://www.youtube.com/watch?v=vnn4XeKQobs) | 2026-06-05 | diagonal orientation, support fins, tine direction, removability |
| 4 | [The Correct Way to Design Holes for 3D Printing](https://www.youtube.com/watch?v=ip70-Tw6tBE) | 2026-05-29 | side holes, orientation, sag, threaded holes, microfeatures |
| 5 | [6 Ways To Make Snap Fits for 3D Printing](https://www.youtube.com/watch?v=rsfZgT3ZEI8) | 2026-05-22 | snap fits, layer direction, compliance, support-free geometry |
| 6 | [You're Designing Handles Wrong](https://www.youtube.com/watch?v=CjDpfGzLTmY) | 2026-05-15 | handles, bridges, designed support, orientation, hinges |
| 7 | [Ribs and Trusses are Made Wrong in 3D Printing](https://www.youtube.com/watch?v=OcxfQeeKn-s) | 2026-03-06 | ribs/trusses, first layer, hidden microfeatures |
| 8 | [Stop Pausing to Insert Stuff](https://www.youtube.com/watch?v=WMbmDfGEygk) | 2026-02-17 | inserts, captive nuts, no-pause production |
| 9 | [You Don't Use Fins Enough](https://www.youtube.com/watch?v=6gPPAiqSkBc) | 2026-02-10 | grip fins, support fins, tolerance compensation |
| 10 | [We Redesigned This Injection Molded Product for Mass-Production 3D Printing](https://www.youtube.com/watch?v=uvnJ9E7_VWA) | 2026-02-06 | molded-to-FDM redesign, part consolidation, orientation |
| 11 | [How to Eliminate Shrink Lines](https://www.youtube.com/watch?v=d61u_lKFa-U) | 2026-01-17 | hull lines, textures, floor/wall decoupling |
| 12 | [I Tried to Design the Perfect 3D Printed Drawer](https://www.youtube.com/watch?v=cdyqNocFCpQ) | 2026-01-10 | one-piece production, chamfers, bridging, tolerances |
| 13 | [How to Design a Cookie Cutter for Mass Production 3D Printing](https://www.youtube.com/watch?v=oz51t5p9gXo) | 2025-12-23 | thin walls, blade tips, bed contact, cleaning |
| 14 | [20+ Ways to Make Your 3D Prints Stronger](https://www.youtube.com/watch?v=81qmDc5unYM) | 2025-11-15 | wall placement, orientation, clips, loops, screw holes |
| 15 | [NEVER Let Your Parts Warp Again](https://www.youtube.com/watch?v=iPZoDltS30A) | 2025-10-31 | warping, corners, continuous paths, infill interruption |
| 16 | [Horizontal Pins with Perfect Tolerance](https://www.youtube.com/watch?v=Iyxp_Rjz3wo) | 2025-08-22 | horizontal pins/holes, sag, tapered fits, compliant tabs |
| 17 | [How to Design a Print with Perfect Tolerance EVERY Time](https://www.youtube.com/watch?v=XKrDUnZCmQQ) | 2025-07-31 | tolerance, contact control, compliant interfaces, creep |
| 18 | [Stop Using Slicer Supports](https://www.youtube.com/watch?v=_R2E8VwyNz0) | 2025-05-23 | support avoidance, designed support, support export |
| 19 | [Watch This Before You Sell 3D Printed Lamps](https://www.youtube.com/watch?v=4WIfbKN-vkg) | 2025-01-18 | shelling, wall thickness, overhangs, seams/textures |
| 20 | [How to Prepare Your Parts for 3D Print on Demand & Reduce Costs](https://www.youtube.com/watch?v=f4fJ5AbUF6Q) | 2024-08-29 | production preflight, supports, first layer, texture, prototype |
| 21 | [The Correct Orientation to Print Boxes](https://www.youtube.com/watch?v=8NKVNwVaZU0) | 2024-01-25 | diagonal enclosure orientation, designed support, strength |
| 22 | [How Does Wall Thickness Affect 3D Printed Part Strength?](https://www.youtube.com/watch?v=PQHKQH5imkI) | 2023-12-29 | wall-thickness test |
| 23 | [Design Better Fillets for Mass Production 3D Printing](https://www.youtube.com/watch?v=IrvxX0MtGMM) | 2023-12-22 | bottom fillets, custom profiles, chamfers |
| 24 | [8 Essential Design Rules for Mass Production 3D Printing](https://www.youtube.com/watch?v=1n_R8shlGcs) | 2023-11-18 | minimum features, first layer, cavities, compliance, ejection |
| 25 | [Rods](https://www.youtube.com/watch?v=WfP-ZOnlFPM) | 2023-09-26 | rod orientation, strength, bed contact, non-round sections |

## Extracted claims

### 1. The Seven Deadly Sins of 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=iiCsQIN_PyQ), 2026-08-21, 11:56.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-11:56.
- **Claims:**
  - [01:04](https://www.youtube.com/watch?v=iiCsQIN_PyQ&t=64s) Keep the first layer simple, visually noncritical, and as small as practical; text/detail and a customer-facing first layer increase rejection and removal risk. **Confidence: High.**
  - [02:39](https://www.youtube.com/watch?v=iiCsQIN_PyQ&t=159s) Avoid conventional fillets on underside/horizontal transitions because their first steps act as overhangs; use a chamfer for a consistently supported staircase. **Confidence: High.**
  - [03:43](https://www.youtube.com/watch?v=iiCsQIN_PyQ&t=223s) Encode local strength and support intent in CAD rather than relying on slicer-only modifiers or painted support, so the model transfers more reliably between machines and workflows. **Confidence: High.**
  - [06:29](https://www.youtube.com/watch?v=iiCsQIN_PyQ&t=389s) Very small internal cuts can force perimeter paths at selected high-stress regions, functioning like geometry-encoded local reinforcement. **Confidence: Medium** because the stated nominal width is process dependent.
  - [07:53](https://www.youtube.com/watch?v=iiCsQIN_PyQ&t=473s) Prefer eliminating support; if support is unavoidable, design only the required support into the model for predictable placement and removal. **Confidence: High.**
- **Conditions/exceptions:** The portability goal is production across differing slicers, machines, and materials, not a claim that slicer settings are irrelevant to print quality. The speaker says a heavily supported model may be a poor FDM candidate at all ([07:53](https://www.youtube.com/watch?v=iiCsQIN_PyQ&t=473s)).
- **Internal tension:** The video says not to rely on the slicer, then recommends microfeatures precisely because slicers convert those cuts into walls ([06:29](https://www.youtube.com/watch?v=iiCsQIN_PyQ&t=389s)). The intended distinction appears to be geometry that provokes ordinary perimeter behavior versus a proprietary/local modifier profile.

### 2. 10 Ways to Make Perfect 3D Printed Holes

- **Source:** [video](https://www.youtube.com/watch?v=3BIvSiuQVWQ), 2026-06-26, 13:10.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-13:10.
- **Claims:**
  - [01:22](https://www.youtube.com/watch?v=3BIvSiuQVWQ&t=82s) A plain Boolean top hole can leave a weak/poorly bonded perimeter at the top skin; blend the opening into the top with a fillet or, preferably, a chamfer. **Confidence: High.**
  - [02:25](https://www.youtube.com/watch?v=3BIvSiuQVWQ&t=145s) Chamfered lead-ins are presented as crisper and more predictable than curved fillets and also help guide inserted parts. **Confidence: High.**
  - [03:34](https://www.youtube.com/watch?v=3BIvSiuQVWQ&t=214s) Reinforce a hole locally in CAD with corrugations, threads, or hidden microfeatures rather than globally raising wall/infill settings. **Confidence: High.**
  - [05:02](https://www.youtube.com/watch?v=3BIvSiuQVWQ&t=302s) For an interference fastener, use sacrificial/compliant teeth or relief slots so the fastener has material to bite without wedging a rigid cylinder apart. **Confidence: High.**
  - [09:25](https://www.youtube.com/watch?v=3BIvSiuQVWQ&t=565s) Do not completely isolate a reinforced cylindrical region with a continuous micro-cut; connect it to the surrounding body or deliberately turn it into a compliant feature. **Confidence: High.**
- **Conditions/exceptions:** Grip-fin dimensions and stiffness must be chosen for the insert and use; the video notes that fewer/thicker fins are more rigid ([11:09](https://www.youtube.com/watch?v=3BIvSiuQVWQ&t=669s)). Thread details below the process resolution can disappear ([04:19](https://www.youtube.com/watch?v=3BIvSiuQVWQ&t=259s)).
- **Internal contradictions:** None material observed. Broad portability language is stronger than the later admission that shrink and feature resolution still vary.

### 3. How to Design Better Support Fins for 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=vnn4XeKQobs), 2026-06-05, 16:48.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-16:48.
- **Claims:**
  - [00:49](https://www.youtube.com/watch?v=vnn4XeKQobs&t=49s) A support fin can stabilize a part printed diagonally so several visible faces avoid distinct top/bottom finishes and layer paths can be better aligned. **Confidence: High.**
  - [02:46](https://www.youtube.com/watch?v=vnn4XeKQobs&t=166s) Do not balance a diagonal part or fin on a mathematical edge; add a small flat/chamfer for real bed contact. **Confidence: High.**
  - [04:36](https://www.youtube.com/watch?v=vnn4XeKQobs&t=276s) Give the fin itself a broad, peelable base; the video uses a thin fin above a wider pad so stability does not require a bulky support body. **Confidence: High.**
  - [06:39](https://www.youtube.com/watch?v=vnn4XeKQobs&t=399s) Connect the fin to the model with tines aligned horizontally in the print plane, not tiny near-vertical posts, so each connection is laid as a continuous path and avoids repeated retractions. **Confidence: High.**
  - [11:09](https://www.youtube.com/watch?v=vnn4XeKQobs&t=669s) Make tines approximately one layer high and one/two nozzle passes wide, use only enough to stabilize the part, and move witness marks to a hidden edge where possible. **Confidence: Medium** because the exact dimensions are process specific.
- **Conditions/exceptions:** A fin on only one side constrains only one direction unless it is connected to the model; long/deep parts may need fins at both ends ([13:35](https://www.youtube.com/watch?v=vnn4XeKQobs&t=815s)). The video also concedes that scaled-down support may cease to print reliably ([14:44](https://www.youtube.com/watch?v=vnn4XeKQobs&t=884s)).
- **Internal contradictions:** None material observed.

### 4. The Correct Way to Design Holes for 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=ip70-Tw6tBE), 2026-05-29, 18:41.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-18:41.
- **Claims:**
  - [00:58](https://www.youtube.com/watch?v=ip70-Tw6tBE&t=58s) A side-facing circular hole has two distinct risks: roof sag/ovality and splitting along the surrounding layer planes. **Confidence: High.**
  - [01:51](https://www.youtube.com/watch?v=ip70-Tw6tBE&t=111s) Before reshaping the hole, test a diagonal part orientation that removes the unsupported roof and wraps layer loops more favorably around the opening; add a bed flat and designed stabilizer. **Confidence: High.**
  - [05:50](https://www.youtube.com/watch?v=ip70-Tw6tBE&t=350s) A pointed/teardrop roof avoids the circular overhang, but the video rejects it for precision fits because it adds clearance/slop. **Confidence: High.**
  - [06:39](https://www.youtube.com/watch?v=ip70-Tw6tBE&t=399s) For some fasteners, a circumscribed polygonal opening can eliminate the unsupported circular roof and provide debris/relief corners while retaining contact faces. **Confidence: High.**
  - [08:03](https://www.youtube.com/watch?v=ip70-Tw6tBE&t=483s) Relief slots can make a circular side hole compliant and remove the unsupported roof region; for modeled threads, remove the top (and optionally bottom) portions that would sag, leaving functional side threads. **Confidence: High.**
  - [10:47](https://www.youtube.com/watch?v=ip70-Tw6tBE&t=647s) Hidden angled micro-cuts can induce walls around a stress concentration, but a cut directly through the center may create a zipper-like weak plane. **Confidence: Medium** because exact cut widths depend on mesh repair and slicer behavior.
- **Conditions/exceptions:** Orientation cannot always change; geometry alternatives are then required ([04:11](https://www.youtube.com/watch?v=ip70-Tw6tBE&t=251s)). Threads remain limited by printable feature size ([09:42](https://www.youtube.com/watch?v=ip70-Tw6tBE&t=582s)).
- **Internal tension:** The video promises designs that work on any machine/material/resolution ([04:42](https://www.youtube.com/watch?v=ip70-Tw6tBE&t=282s)) but later states that tiny microfeatures can be closed by slicer/mesh repair and must be sized accordingly ([11:08](https://www.youtube.com/watch?v=ip70-Tw6tBE&t=668s)).

### 5. 6 Ways To Make Snap Fits for 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=rsfZgT3ZEI8), 2026-05-22, 14:32.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-14:32.
- **Claims:**
  - [00:21](https://www.youtube.com/watch?v=rsfZgT3ZEI8&t=21s) A molded-style cantilever snap printed upright can fracture at a layer plane near its root. **Confidence: High.**
  - [01:09](https://www.youtube.com/watch?v=rsfZgT3ZEI8&t=69s) Reorient a compliant arm so its flex runs within the printed layers rather than opening a layer interface. **Confidence: High.**
  - [02:30](https://www.youtube.com/watch?v=rsfZgT3ZEI8&t=150s) Horizontal leaf-spring snaps permit more travel; adjust stiffness with arm length/thickness and protect their first-layer tips with a tiny tie-back or local adhesion feature. **Confidence: High.**
  - [05:08](https://www.youtube.com/watch?v=rsfZgT3ZEI8&t=308s) Chamfer overhanging snap shoulders so they grow layer by layer without support. **Confidence: High.**
  - [08:12](https://www.youtube.com/watch?v=rsfZgT3ZEI8&t=492s) For snaps on four sides, rotate the whole interface so all arms lie in the build plane, then remove the unsupported inner volume and chamfer upper/downward faces. **Confidence: High.**
- **Conditions/exceptions:** Reorientation may create new overhangs and bed-contact problems that must be designed out; eliminating the inner backstop also permits greater deflection and can raise break risk unless the arms are resized ([11:31](https://www.youtube.com/watch?v=rsfZgT3ZEI8&t=691s)).
- **Internal uncertainty:** The title says six ways while the spoken introduction says seven ([00:00](https://www.youtube.com/watch?v=rsfZgT3ZEI8&t=0s)); this does not affect the extracted design principles.

### 6. You're Designing Handles Wrong

- **Source:** [video](https://www.youtube.com/watch?v=CjDpfGzLTmY), 2026-05-15, 21:58.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-21:58.
- **Claims:**
  - [00:30](https://www.youtube.com/watch?v=CjDpfGzLTmY&t=30s) A simple side-hole handle concentrates pullout load at the opening; add material around the opening and chamfer its underside instead of creating a support-demanding shelf. **Confidence: High.**
  - [01:33](https://www.youtube.com/watch?v=CjDpfGzLTmY&t=93s) A long horizontal handle opening may bridge poorly; if it cannot be redesigned away, use a removable designed insert with a consistent clearance and an accessible pull feature. **Confidence: High.**
  - [03:21](https://www.youtube.com/watch?v=CjDpfGzLTmY&t=201s) Ask whether a through-hole is functionally necessary: a closed grip recess can remove the bridge and reduce a layer-splitting stress concentration. **Confidence: High.**
  - [04:35](https://www.youtube.com/watch?v=CjDpfGzLTmY&t=275s) If a through-slot is required, angle its roof toward a self-supporting profile; the video shows about 45 degrees working better than a steeper 30-degree attempt. **Confidence: Medium** because angle reference conventions are not stated.
  - [11:01](https://www.youtube.com/watch?v=CjDpfGzLTmY&t=661s) A box can be printed on an edge/diagonal so flat handles lie in the layer plane, visible faces share a similar finish, and support is avoided; the handles themselves can act as stabilizing fins. **Confidence: High.**
  - [18:22](https://www.youtube.com/watch?v=CjDpfGzLTmY&t=1102s) For a print-in-place hinge lying on the bed, nested conical pivots are preferred over a thin through-pin; start bed-facing curved edges with a chamfer before blending to a fillet. **Confidence: High.**
- **Conditions/exceptions:** Compliant living hinges are material dependent and fatigue over time; the video specifically warns against brittle matte PLA for repeated flexing ([16:18](https://www.youtube.com/watch?v=CjDpfGzLTmY&t=978s)). Upside-down boxes may still bridge/sag internally even when the exterior is support-free ([17:25](https://www.youtube.com/watch?v=CjDpfGzLTmY&t=1045s)).
- **Internal contradictions:** None material observed; several alternatives are explicitly presented as trade-offs among appearance, strength, cost, and manufacturability.

### 7. Ribs and Trusses are Made Wrong in 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=OcxfQeeKn-s), 2026-03-06, 5:10.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:10.
- **Claims:**
  - [00:20](https://www.youtube.com/watch?v=OcxfQeeKn-s&t=20s) An open truss copied from another process can impose orientation limits, exposed pinch/dirt cavities, and a complex first layer. **Confidence: High.**
  - [01:05](https://www.youtube.com/watch?v=OcxfQeeKn-s&t=65s) A backing plate simplifies the first layer, resists warping, and adds shear-panel behavior. **Confidence: High.**
  - [01:47](https://www.youtube.com/watch?v=OcxfQeeKn-s&t=107s) If strength comes from perimeter paths around truss members, hide those paths inside a closed body by cutting very thin truss-shaped microfeatures; the surrounding volume may then use low infill. **Confidence: Medium** because effectiveness depends on slicer interpretation and no mechanical test is shown here.
- **Conditions/exceptions:** The speaker says a solid body with low infill is also acceptable ([02:11](https://www.youtube.com/watch?v=OcxfQeeKn-s&t=131s)); hidden microfeatures are an alternative for controlled internal paths, not a universal replacement.
- **Internal contradictions:** None material observed.

### 8. Stop Pausing to Insert Stuff

- **Source:** [video](https://www.youtube.com/watch?v=WMbmDfGEygk), 2026-02-17, 7:49.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-07:49.
- **Claims:**
  - [00:19](https://www.youtube.com/watch?v=WMbmDfGEygk&t=19s) Mid-print pauses for hardware add labor and permit the cooling part to develop restart/shrink artifacts, making them poor defaults for volume production. **Confidence: High.**
  - [01:11](https://www.youtube.com/watch?v=WMbmDfGEygk&t=71s) A plain printed thread/hole may suit small, low-torque, one-time fastening, but larger/tighter fasteners can split the plastic and repeated/high-torque use favors metal hardware. **Confidence: High.**
  - [01:44](https://www.youtube.com/watch?v=WMbmDfGEygk&t=104s) Relief features give a self-tapping fastener controlled material to cut and space for displaced polymer, reducing outward wedge stress. **Confidence: High.**
  - [02:36](https://www.youtube.com/watch?v=WMbmDfGEygk&t=156s) Load nuts from the back or side into modeled pockets instead of pausing; use jigs where needed to position them during assembly. **Confidence: High.**
  - [05:43](https://www.youtube.com/watch?v=WMbmDfGEygk&t=343s) A top slot leading to a wider internal chamber can let a nut drop, rotate flat, and be pulled into its retaining seat by the screw after printing. **Confidence: High.**
- **Conditions/exceptions:** A side-loaded slot creates a stress concentration in the layer plane and may be unsuitable under high pullout load ([04:50](https://www.youtube.com/watch?v=WMbmDfGEygk&t=290s)). Paused insertion remains acceptable when the hardware/geometry truly requires it, but restricts scaling options ([07:13](https://www.youtube.com/watch?v=WMbmDfGEygk&t=433s)).
- **Internal contradictions:** None material observed.

### 9. You Don't Use Fins Enough

- **Source:** [video](https://www.youtube.com/watch?v=6gPPAiqSkBc), 2026-02-10, 9:00.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-09:00.
- **Claims:**
  - [00:17](https://www.youtube.com/watch?v=6gPPAiqSkBc&t=17s) Grip fins replace a single rigid tolerance with multiple compliant contacts so mating parts can accommodate shrink/process variation. **Confidence: High.**
  - [01:08](https://www.youtube.com/watch?v=6gPPAiqSkBc&t=68s) Start from an intentionally undersized hole, cut slots to form fins, and free their roots with an undercut/disc; longer or thinner fins give a softer fit. **Confidence: High.**
  - [02:36](https://www.youtube.com/watch?v=6gPPAiqSkBc&t=156s) Diagonal orientation can improve strength and surface consistency, but it requires real bed flats and stabilization rather than balancing on a corner. **Confidence: High.**
  - [04:32](https://www.youtube.com/watch?v=6gPPAiqSkBc&t=272s) A support fin should be connected to the part and use horizontal tines so the nozzle lays each connection continuously in one layer. **Confidence: High.**
  - [06:46](https://www.youtube.com/watch?v=6gPPAiqSkBc&t=406s) Minimize the fin body while retaining a broad base: the base supplies adhesion and the thin fin supplies removable lateral stability. **Confidence: High.**
- **Conditions/exceptions:** Fin stiffness and grip are intentionally tunable, not dimensionally universal. The repeated claim of working with "any" process is an aspiration to robustness, not demonstrated coverage across all printers/materials.
- **Internal contradictions:** None material observed.

### 10. We Redesigned This Injection Molded Product for Mass-Production 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=uvnJ9E7_VWA), 2026-02-06, 9:10.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-09:10.
- **Claims:**
  - [00:44](https://www.youtube.com/watch?v=uvnJ9E7_VWA&t=44s) Do not preserve molding-driven hollows and multipart assembly by default; FDM can consolidate retainers and mechanisms into fewer parts. **Confidence: High.**
  - [02:12](https://www.youtube.com/watch?v=uvnJ9E7_VWA&t=132s) Model retaining overhangs into the printed housing to eliminate a screwed-on cover and downstream assembly. **Confidence: High.**
  - [03:00](https://www.youtube.com/watch?v=uvnJ9E7_VWA&t=180s) Use thick external geometry with sparse/controlled interiors where molding would require thin walls for sink/shrink control. **Confidence: High** as a report of the redesign; generalization remains uncorroborated.
  - [03:30](https://www.youtube.com/watch?v=uvnJ9E7_VWA&t=210s) Trim a nonfunctional end to create a diagonal bed interface, add a small engineered stabilizer, and orient major loops diagonally so retention features do not split along one plane. **Confidence: High.**
  - [05:18](https://www.youtube.com/watch?v=uvnJ9E7_VWA&t=318s) Redesign the plunger as a solid/closed body and place its flexible arms in the layer plane; thicken the pinch surfaces locally for grip and load distribution. **Confidence: High.**
- **Conditions/exceptions:** Outdoor durability and compliant-arm behavior still depend on material selection; the video suggests PETG or ASA for its example ([05:55](https://www.youtube.com/watch?v=uvnJ9E7_VWA&t=355s)).
- **Internal contradictions:** None material observed.

### 11. How to Eliminate Shrink Lines

- **Source:** [video](https://www.youtube.com/watch?v=d61u_lKFa-U), 2026-01-17, 11:37.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-11:37.
- **Claims:**
  - [00:44](https://www.youtube.com/watch?v=d61u_lKFa-U&t=44s) A visible hull/shrink line appears where a thick base transitions to a thin wall; simply thickening the wall did not remove it in the shown comparison. **Confidence: High.**
  - [02:10](https://www.youtube.com/watch?v=d61u_lKFa-U&t=130s) Surface patterning can conceal the line; CAD-authored texture is proposed when the geometry must remain portable across slicers. **Confidence: High.**
  - [04:03](https://www.youtube.com/watch?v=d61u_lKFa-U&t=243s) A shallow interior dish/chamfer changed but did not meaningfully eliminate the line in the shown sample. **Confidence: High.**
  - [05:16](https://www.youtube.com/watch?v=d61u_lKFa-U&t=316s) A narrow groove around the floor perimeter decoupled the thick top/floor surface from the wall and nearly eliminated the visible line in this test while leaving lower geometry connected. **Confidence: High for the shown result; Medium for generalization.**
  - [07:29](https://www.youtube.com/watch?v=d61u_lKFa-U&t=449s) If interrupting a continuous top surface with a grid, raise a connected grid rather than isolated islands to avoid many retractions; the experiment still left a dotted line aligned with the ribs. **Confidence: High.**
- **Conditions/exceptions:** The video concedes that complete elimination is not demonstrated and recommends texture when possible ([09:37](https://www.youtube.com/watch?v=d61u_lKFa-U&t=577s)). It does not solve rib-induced lines generally ([10:28](https://www.youtube.com/watch?v=d61u_lKFa-U&t=628s)).
- **Internal tension:** At [09:37](https://www.youtube.com/watch?v=d61u_lKFa-U&t=577s) the narration says the only way to "completely" deal with the line is decoupling, but immediately notes a residual line; the supported conclusion is reduction, not guaranteed elimination.

### 12. I Tried to Design the Perfect 3D Printed Drawer

- **Source:** [video](https://www.youtube.com/watch?v=cdyqNocFCpQ), 2026-01-10, 11:23.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-11:23.
- **Claims:**
  - [00:15](https://www.youtube.com/watch?v=cdyqNocFCpQ&t=15s) Design the drawer/module as one vertically printed unit when production cost and part count matter, then solve the resulting overhangs in geometry. **Confidence: High.**
  - [00:46](https://www.youtube.com/watch?v=cdyqNocFCpQ&t=46s) Use mating chamfers as a rear stop and entry guide; unlike a fillet, their straight slope provides a more consistent contact surface. **Confidence: High.**
  - [01:11](https://www.youtube.com/watch?v=cdyqNocFCpQ&t=71s) Replace a flat internal roof with a rounded/self-supporting transition and add a center rib if the bridge/span becomes too long at a steeper angle. **Confidence: High.**
  - [03:46](https://www.youtube.com/watch?v=cdyqNocFCpQ&t=226s) Avoid large flat cosmetic top surfaces when a deliberate concave profile can turn layer stepping into an intentional texture and make defects less conspicuous. **Confidence: High.**
  - [08:19](https://www.youtube.com/watch?v=cdyqNocFCpQ&t=499s) Preserve a vertical build for tolerance-critical sliding faces and integrate the finger pull into a chamfered underside rather than adding an unsupported front handle. **Confidence: High.**
- **Conditions/exceptions:** A round module improved corner-free printing but created orientation, grip, and thick-wall trade-offs ([06:03](https://www.youtube.com/watch?v=cdyqNocFCpQ&t=363s)); the video ultimately treats design choice as use-specific.
- **Internal contradictions:** None material observed.

### 13. How to Design a Cookie Cutter for Mass Production 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=oz51t5p9gXo), 2025-12-23, 8:12.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:12.
- **Claims:**
  - [01:24](https://www.youtube.com/watch?v=oz51t5p9gXo&t=84s) Give the cutter a wide handle/base for hand pressure and bed adhesion, and chamfer/round its lower transitions to limit elephant-foot interference. **Confidence: High.**
  - [02:02](https://www.youtube.com/watch?v=oz51t5p9gXo&t=122s) A solid back is more reliable to print than a network of narrow support bars, but may trap food; separating the outline cutter from the stamp is proposed when cleaning access matters. **Confidence: High.**
  - [03:03](https://www.youtube.com/watch?v=oz51t5p9gXo&t=183s) Use roughly a 1 mm blade wall in the demonstrated setup so fine features receive multiple extrusion paths and resist breakage. **Confidence: Medium** because this is nozzle/process dependent.
  - [03:37](https://www.youtube.com/watch?v=oz51t5p9gXo&t=217s) Taper the cutting edge from the outside so displaced dough moves outward, and leave a nozzle-width land rather than a mathematically sharp tip that may print intermittently or shed. **Confidence: High for the principle; Low for the captioned numeric range.**
  - [04:50](https://www.youtube.com/watch?v=oz51t5p9gXo&t=290s) Round interior/exterior corners and avoid crevices to improve cleanability. **Confidence: High.**
- **Conditions/exceptions:** A solid back conflicts with cleaning access; the split cutter/stamp is the stated alternative. Material and wash-temperature claims are outside this CAD batch and require separate safety corroboration.
- **Internal uncertainty:** Automatic captions render the cutting-tip dimension inconsistently (apparently a missing decimal); this document deliberately records only "nozzle-width land."

### 14. 20+ Ways to Make Your 3D Prints Stronger

- **Source:** [video](https://www.youtube.com/watch?v=81qmDc5unYM), 2025-11-15, 22:48.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-22:48.
- **Claims:**
  - [00:39](https://www.youtube.com/watch?v=81qmDc5unYM&t=39s) For bending members, place more material toward the outside where tension/compression are highest; encode that wall placement with thin internal geometry instead of a slicer-only wall count. **Confidence: High.**
  - [02:17](https://www.youtube.com/watch?v=81qmDc5unYM&t=137s) Microfeatures must be small enough that adjacent paths fuse rather than form a detached sleeve, yet large enough to survive slicing/mesh processing. **Confidence: Medium** because the captioned dimensions are inconsistent.
  - [04:33](https://www.youtube.com/watch?v=81qmDc5unYM&t=273s) For clips on a ring, first align clip flex with the layer plane; if orientation is constrained, reinforce roots with chamfers and choose a tougher material, accepting reduced flexibility. **Confidence: High.**
  - [06:01](https://www.youtube.com/watch?v=81qmDc5unYM&t=361s) Printing a ring at an angle improves clip-layer alignment but may require a bed flat, local adhesion/support, and rounded overhang edges. **Confidence: High.**
  - [09:25](https://www.youtube.com/watch?v=81qmDc5unYM&t=565s) Replace a thin wire-like side loop with a broad plate and local rim/rib around its hole to spread pullout load. **Confidence: High.**
  - [12:08](https://www.youtube.com/watch?v=81qmDc5unYM&t=728s) Around wall-mount screw holes, add visible rings/struts or hidden vertical micro-slats so cracks encounter more perimeter material instead of an unreinforced layer plane. **Confidence: High.**
- **Conditions/exceptions:** Solid infill is acknowledged as the simplest strength option when weight/material are acceptable ([03:42](https://www.youtube.com/watch?v=81qmDc5unYM&t=222s)). Material, orientation, over-extrusion, and tolerance constraints still affect the result ([04:52](https://www.youtube.com/watch?v=81qmDc5unYM&t=292s)).
- **Internal uncertainty:** Automatic captions alternate between values that appear to have lost decimal points for microfeature width. No exact numeric rule is extracted from this video.

### 15. NEVER Let Your Parts Warp Again

- **Source:** [video](https://www.youtube.com/watch?v=iPZoDltS30A), 2025-10-31, 11:08.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-11:08.
- **Claims:**
  - [00:05](https://www.youtube.com/watch?v=iPZoDltS30A&t=5s) Warping force grows with long continuous shrinking paths; larger dimensions turn the same shrink percentage into larger displacement/stress. **Confidence: High.**
  - [01:01](https://www.youtube.com/watch?v=iPZoDltS30A&t=61s) Round sharp outer corners to distribute peel force over more bed-contact area; add designed mouse ears if sharp corners must remain. **Confidence: High.**
  - [02:17](https://www.youtube.com/watch?v=iPZoDltS30A&t=137s) Shallow checker/groove cuts can interrupt long solid paths above a thin continuous first skin, trading some first-layer complexity for shorter shrink spans. **Confidence: Medium** because spacing/depth depend on scale/material.
  - [06:00](https://www.youtube.com/watch?v=iPZoDltS30A&t=360s) Interrupt long side walls with relief cuts, ripples, or gentle curvature so shrink can consume geometric slack rather than peel corners. **Confidence: High for the proposed mechanism; Medium for universal effectiveness.**
  - [08:34](https://www.youtube.com/watch?v=iPZoDltS30A&t=514s) Hidden holes/slits can break long infill runs that otherwise pull diagonally on corners; the idea is to make the CAD robust even if the downstream infill pattern changes. **Confidence: High.**
- **Conditions/exceptions:** The speaker explicitly says the demonstrations are concepts, not universally applicable prescriptions ([07:59](https://www.youtube.com/watch?v=iPZoDltS30A&t=479s)). Cuts can weaken functional parts, and spacing should vary with material and size ([03:28](https://www.youtube.com/watch?v=iPZoDltS30A&t=208s)).
- **Internal tension:** Broad claims that the design can work with any machine/material/scale ([04:44](https://www.youtube.com/watch?v=iPZoDltS30A&t=284s)) are narrowed by the later statement that the demonstrated solutions are not universal and require material/geometry judgment.

### 16. Horizontal Pins with Perfect Tolerance

- **Source:** [video](https://www.youtube.com/watch?v=Iyxp_Rjz3wo), 2025-08-22, 8:05.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:05.
- **Claims:**
  - [00:16](https://www.youtube.com/watch?v=Iyxp_Rjz3wo&t=16s) A horizontal pin is strong along its layers, but a round horizontal pin and round side hole create underside support and roof-sag/tolerance problems. **Confidence: High.**
  - [01:07](https://www.youtube.com/watch?v=Iyxp_Rjz3wo&t=67s) Chamfer the pin tip for a supported, printable lead-in and blend the mating entry; reshape the hole roof rather than accepting a sagged circle. **Confidence: High.**
  - [02:43](https://www.youtube.com/watch?v=Iyxp_Rjz3wo&t=163s) Convert the disposable support under a horizontal pin into functional flanges, then chamfer top and bottom into a keyhole/slot whose high-precision side faces control fit. **Confidence: High.**
  - [04:07](https://www.youtube.com/watch?v=Iyxp_Rjz3wo&t=247s) A tapered tab can guarantee an easy start and progressively tighten; paired/offset contacts can self-center. **Confidence: High.**
  - [05:09](https://www.youtube.com/watch?v=Iyxp_Rjz3wo&t=309s) Split a rigid tab into compliant fingers and optionally add mating bumps/recesses so process variation is absorbed by spring motion rather than a single nominal clearance. **Confidence: High.**
- **Conditions/exceptions:** A plain roof-relieved round hole may be adequate where fit is not demanding ([01:45](https://www.youtube.com/watch?v=Iyxp_Rjz3wo&t=105s)); compliance is introduced when cross-machine repeatability or retention is more important.
- **Internal contradictions:** None material observed.

### 17. How to Design a Print with Perfect Tolerance EVERY Time

- **Source:** [video](https://www.youtube.com/watch?v=XKrDUnZCmQQ), 2025-07-31, 12:34.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-12:34.
- **Claims:**
  - [00:00](https://www.youtube.com/watch?v=XKrDUnZCmQQ&t=0s) The same nominal model can fit differently with color, material, layer height, infill, nozzle, or machine, so robust mating geometry should not depend on one calibrated clearance. **Confidence: High.**
  - [01:04](https://www.youtube.com/watch?v=XKrDUnZCmQQ&t=64s) Round mating corners to avoid local dimensional error at abrupt direction changes, and chamfer the bed-facing edge to isolate elephant-foot effects. **Confidence: High.**
  - [02:01](https://www.youtube.com/watch?v=XKrDUnZCmQQ&t=121s) Add a lead-in taper so assembly begins at a loose dimension and progressively wedges toward the holding dimension. **Confidence: High.**
  - [03:29](https://www.youtube.com/watch?v=XKrDUnZCmQQ&t=209s) Reduce uncontrolled infill shrink in a mating plug by hollowing/thinning it, then deliberately limit contact to a few flexible regions rather than the full perimeter. **Confidence: High.**
  - [05:05](https://www.youtube.com/watch?v=XKrDUnZCmQQ&t=305s) Free compliant walls from the backing plate with a designed gap; too small a gap may be healed during mesh/slicing, while too large a gap may deform. **Confidence: High for the trade-off; Medium for the captioned dimensions.**
  - [08:00](https://www.youtube.com/watch?v=XKrDUnZCmQQ&t=480s) Alternatively make the receiver compliant: remove corner contact and add short relief splits only as a safety margin, not as large-deflection springs across weak layer planes. **Confidence: High.**
  - [10:05](https://www.youtube.com/watch?v=XKrDUnZCmQQ&t=605s) Multiple grip fins can approximate constant insertion/retention force, but polymer creep can reduce pressure over time. **Confidence: High.**
- **Conditions/exceptions:** Relief gaps are subject to STL repair/slicer behavior, and compliant elements must be limited so they do not unzip layer planes. Plastic creep and duty cycle constrain the "every time" framing.
- **Internal tension:** The title and early narration promise machine/material-independent perfect tolerance, while the video itself acknowledges mesh healing, material creep, and the need to tune gaps ([05:24](https://www.youtube.com/watch?v=XKrDUnZCmQQ&t=324s), [10:34](https://www.youtube.com/watch?v=XKrDUnZCmQQ&t=634s)).

### 18. Stop Using Slicer Supports

- **Source:** [video](https://www.youtube.com/watch?v=_R2E8VwyNz0), 2025-05-23, 12:17.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-12:17.
- **Claims:**
  - [00:18](https://www.youtube.com/watch?v=_R2E8VwyNz0&t=18s) Auto support is a generic fallback; distributed products need controlled support placement/removal to avoid user- and slicer-dependent results. **Confidence: High.**
  - [01:47](https://www.youtube.com/watch?v=_R2E8VwyNz0&t=107s) First try to eliminate support through orientation and chamfered/self-supporting geometry. **Confidence: High.**
  - [02:25](https://www.youtube.com/watch?v=_R2E8VwyNz0&t=145s) For a hanging tooth/spike, a designed "thumbtack" contact can anchor its first layers so it does not settle into a loose support nest. **Confidence: High.**
  - [03:25](https://www.youtube.com/watch?v=_R2E8VwyNz0&t=205s) A custom support body should contour the target surface with an intentional separation, support only the required region, and be verified by test prints. **Confidence: High.**
  - [06:24](https://www.youtube.com/watch?v=_R2E8VwyNz0&t=384s) A diagonal support fin needs horizontal breakaway tines, a removable/flexible body, and a broad enough base to resist peeling. **Confidence: High.**
  - [08:02](https://www.youtube.com/watch?v=_R2E8VwyNz0&t=482s) For a supported bridge, use a crushable/hollow insert or chamfered removable block and provide clear removal affordances/instructions. **Confidence: High.**
  - [10:08](https://www.youtube.com/watch?v=_R2E8VwyNz0&t=608s) A designer who cannot model support can generate it in a slicer that exports support as mesh, then distribute that geometry with the model rather than requiring each user to regenerate it. **Confidence: High.**
- **Conditions/exceptions:** Clearances are material/process specific and require prototypes ([04:09](https://www.youtube.com/watch?v=_R2E8VwyNz0&t=249s)). Auto support is accepted for one-off/home use; the objection is repeatable professional production ([11:18](https://www.youtube.com/watch?v=_R2E8VwyNz0&t=678s)).
- **Internal tension:** The video says to be isolated from the slicer, but later uses a slicer as a support-geometry generator. This is reconciled by exporting a fixed mesh; the final recipient is no longer responsible for regenerating support.

### 19. Watch This Before You Sell 3D Printed Lamps

- **Source:** [video](https://www.youtube.com/watch?v=4WIfbKN-vkg), 2025-01-18, 8:08.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:08.
- **Claims:**
  - [00:32](https://www.youtube.com/watch?v=4WIfbKN-vkg&t=32s) Model the lamp as an actual shell rather than relying on vase mode; this permits thicker/solid mounting regions and thin translucent regions in one monolithic part. **Confidence: High.**
  - [01:08](https://www.youtube.com/watch?v=4WIfbKN-vkg&t=68s) A conventional multi-wall profile is presented as more durable than single-wall vase mode for shipped products. **Confidence: Medium** because no comparative test is shown.
  - [02:02](https://www.youtube.com/watch?v=4WIfbKN-vkg&t=122s) Hide or intentionally place the seam with modeled texture or irregular surface geometry instead of assuming it will disappear. **Confidence: High.**
  - [03:34](https://www.youtube.com/watch?v=4WIfbKN-vkg&t=214s) A uniform thin spherical shell creates a flat top overhang/bright artifact; thicken or chamfer the internal roof and use texture to diffuse residual variation. **Confidence: High.**
  - [06:00](https://www.youtube.com/watch?v=4WIfbKN-vkg&t=360s) Internal patterns can selectively block/transmit light while leaving the outer surface smooth, enabling hidden imagery/messages. **Confidence: High.**
- **Conditions/exceptions:** The wall/profile numbers are explicitly tied to Slant 3D/Teleport's process and lighting goal, not universal mechanical limits ([00:32](https://www.youtube.com/watch?v=4WIfbKN-vkg&t=32s)). Optical performance varies with color/material; those claims require separate validation.
- **Internal uncertainty:** Automatic captions omit decimal points in several profile values, so no exact lamp wall/layer/infill numbers are adopted here.

### 20. How to Prepare Your Parts for 3D Print on Demand & Reduce Costs

- **Source:** [video](https://www.youtube.com/watch?v=f4fJ5AbUF6Q), 2024-08-29, 6:20.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-06:20.
- **Claims:**
  - [00:48](https://www.youtube.com/watch?v=f4fJ5AbUF6Q&t=48s) Unnecessary support raises both material and post-processing cost and can make a complex part unsuitable for the service workflow. **Confidence: High.**
  - [01:34](https://www.youtube.com/watch?v=f4fJ5AbUF6Q&t=94s) Prefer modeled ribs/fins, negative features, altered orientation, or exported fixed support geometry over relying on the destination's auto-support rules. **Confidence: High.**
  - [02:23](https://www.youtube.com/watch?v=f4fJ5AbUF6Q&t=143s) Treat the first layer as critical: encode elephant-foot clearance with a bottom chamfer and add local mouse ears where thin outboard features need adhesion. **Confidence: High.**
  - [03:38](https://www.youtube.com/watch?v=f4fJ5AbUF6Q&t=218s) Model fine surface texture when cosmetics matter and dimensions permit; texture can conceal layer artifacts without depending on a particular slicer profile. **Confidence: High.**
  - [04:29](https://www.youtube.com/watch?v=f4fJ5AbUF6Q&t=269s) Order a representative prototype through the intended end-to-end workflow before sale/production; CAD review alone does not validate output and fulfillment. **Confidence: High.**
- **Conditions/exceptions:** The opening profile numbers and support threshold are Slant 3D service settings, not slicer-agnostic design laws ([00:00](https://www.youtube.com/watch?v=f4fJ5AbUF6Q&t=0s)).
- **Internal contradictions:** None material observed.

### 21. The Correct Orientation to Print Boxes

- **Source:** [video](https://www.youtube.com/watch?v=8NKVNwVaZU0), 2024-01-25, 5:59.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:59.
- **Claims:**
  - [00:00](https://www.youtube.com/watch?v=8NKVNwVaZU0&t=0s) Flat printing can be reliable but may not fit a small bed; upright printing fits but creates internal/side support and a dominant split plane. **Confidence: High.**
  - [02:02](https://www.youtube.com/watch?v=8NKVNwVaZU0&t=122s) Print an enclosure diagonally to distribute layer directions through walls and mounting bosses, but design a support fin because the center of mass may not sit over the bed contact. **Confidence: High.**
  - [02:40](https://www.youtube.com/watch?v=8NKVNwVaZU0&t=160s) Space the fin from the enclosure, connect it with horizontal breakaway sprues, and flatten/chamfer the actual bed edge. **Confidence: High for the geometry; Medium for captioned dimensions.**
  - [04:01](https://www.youtube.com/watch?v=8NKVNwVaZU0&t=241s) Diagonal layers loop around screw bosses and cross potential wall split planes, improving multidirectional robustness relative to a single upright/flat plane. **Confidence: High as the video's design rationale; mechanical magnitude untested here.**
- **Conditions/exceptions:** The lid uses a different demonstrated angle from the box ([04:48](https://www.youtube.com/watch?v=8NKVNwVaZU0&t=288s)); orientation should be selected per part, not imposed on an assembly as a whole.
- **Internal contradictions:** None material observed.

### 22. How Does Wall Thickness Affect 3D Printed Part Strength?

- **Source:** [video](https://www.youtube.com/watch?v=PQHKQH5imkI), 2023-12-29, 3:54.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-03:54.
- **Claims:**
  - [00:08](https://www.youtube.com/watch?v=PQHKQH5imkI&t=8s) In the shown compression series, nominally 40 mm cubes with walls from 1 mm to 5 mm carried progressively greater load as wall thickness increased. **Confidence: High for the qualitative trend.**
  - [01:29](https://www.youtube.com/watch?v=PQHKQH5imkI&t=89s) The narration positions roughly 3 mm walls as a heavy functional range in this no-infill cube setup. **Confidence: Medium; not a general threshold.**
  - [03:11](https://www.youtube.com/watch?v=PQHKQH5imkI&t=191s) Infill was deliberately omitted; the speaker expects infill to alter buckling/failure substantially by bracing the walls. **Confidence: High.**
- **Conditions/exceptions:** The accessible evidence does not state replicate count, material conditioning, print orientation/profile, crosshead speed, or statistical uncertainty. Failure mode also changes from buckling to fracture as walls thicken, so the results are not a clean material-property curve.
- **Internal/data contradiction:** Captioned force conversions are impossible as written (for example pounds and newtons do not match at [00:42](https://www.youtube.com/watch?v=PQHKQH5imkI&t=42s) and [01:15](https://www.youtube.com/watch?v=PQHKQH5imkI&t=75s)). Exact loads are therefore inaccessible from captions and are not recorded as claims.

### 23. Design Better Fillets for Mass Production 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=IrvxX0MtGMM), 2023-12-22, 3:00.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-03:00.
- **Claims:**
  - [00:00](https://www.youtube.com/watch?v=IrvxX0MtGMM&t=0s) Conventional tangent fillets at a bed-facing edge begin with near-horizontal steps that sag or require support. **Confidence: High.**
  - [00:31](https://www.youtube.com/watch?v=IrvxX0MtGMM&t=31s) If a rounded aesthetic is required, use a custom noncircular blend that begins with a printable slope and curves later, accepting a changed footprint/sharper initial edge. **Confidence: High.**
  - [01:34](https://www.youtube.com/watch?v=IrvxX0MtGMM&t=94s) A straight chamfer is the more predictable default because every layer advances by a consistent step. **Confidence: High.**
- **Conditions/exceptions:** The spoken 30-degree recommendation is ambiguous because the reference axis is not stated and the narration uses "maximum," "minimum," and "shallower" inconsistently ([01:07](https://www.youtube.com/watch?v=IrvxX0MtGMM&t=67s)). Treat it as an example, not a portable threshold.
- **Internal uncertainty:** Angle wording is internally inconsistent/underspecified; only the supported qualitative principle is extracted.

### 24. 8 Essential Design Rules for Mass Production 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=1n_R8shlGcs), 2023-11-18, 5:47.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:47.
- **Claims:**
  - [00:00](https://www.youtube.com/watch?v=1n_R8shlGcs&t=0s) For the stated standard 0.4 mm-nozzle context, the video recommends at least about 1 mm for reliable vertical walls/features so multiple paths form them. **Confidence: Medium** because it is a profile-specific heuristic.
  - [00:48](https://www.youtube.com/watch?v=1n_R8shlGcs&t=48s) Replace horizontal shelves with chamfers where possible to remove support, surface damage, and manual post-processing. **Confidence: High.**
  - [01:17](https://www.youtube.com/watch?v=1n_R8shlGcs&t=77s) Make the first layer simple and rounded, avoid fine text/sharp corners, and round vertical travel corners to reduce abrupt nozzle speed/direction changes. **Confidence: High.**
  - [02:25](https://www.youtube.com/watch?v=1n_R8shlGcs&t=145s) Do not copy molding-driven cavities/ribs automatically; closed, chunky infilled volumes may be stronger and easier to print. **Confidence: High as the video's recommendation; suitability is use-dependent.**
  - [03:34](https://www.youtube.com/watch?v=1n_R8shlGcs&t=214s) Use compliant geometry such as reliefs/grip fins for high-variation fits instead of demanding one rigid nominal clearance. **Confidence: High.**
  - [04:00](https://www.youtube.com/watch?v=1n_R8shlGcs&t=240s) For automated production, minimize bed-contact area enough for ejection and consider a supported edge/diagonal orientation rather than a broad base. **Confidence: High.**
- **Conditions/exceptions:** The minimum-wall and ejection rules are tied to a standard nozzle and Slant 3D's automated farm; they are not universal printer-agnostic constants.
- **Internal tension:** The video asks for both a simple/reliable first layer and minimized bed contact. These goals can conflict; the practical reading is "small enough for release, broad/simple enough for adhesion," requiring orientation-specific trade-off analysis.

### 25. Rods

- **Source:** [video](https://www.youtube.com/watch?v=WfP-ZOnlFPM), 2023-09-26, 3:48.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-03:48.
- **Claims:**
  - [00:00](https://www.youtube.com/watch?v=WfP-ZOnlFPM&t=0s) A short rod may be printed vertically for easy bed release and detail, with a bottom chamfer to isolate first-layer deformation. **Confidence: High.**
  - [00:35](https://www.youtube.com/watch?v=WfP-ZOnlFPM&t=35s) A tall vertical rod is more vulnerable to layer-plane bending failure, shrink, and top vibration; lay it horizontally when bending strength dominates. **Confidence: High.**
  - [01:15](https://www.youtube.com/watch?v=WfP-ZOnlFPM&t=75s) A circular rod laid on its side has insufficient bed contact; flatten one side or change to a polygonal section so the part has a stable first layer without a brim. **Confidence: High.**
  - [02:27](https://www.youtube.com/watch?v=WfP-ZOnlFPM&t=147s) A rod need not be circular: a hexagonal/octagonal-like section can preserve most of the functional envelope while supplying a printable flat. **Confidence: High.**
- **Conditions/exceptions:** Vertical is accepted for short/detail-oriented rods, horizontal for long/strength-oriented rods. Mating holes may need redesign for a polygonal shaft ([02:42](https://www.youtube.com/watch?v=WfP-ZOnlFPM&t=162s)).
- **Internal uncertainty:** The 35-degree limit is spoken without a clear angle reference ([01:49](https://www.youtube.com/watch?v=WfP-ZOnlFPM&t=109s)); it should not be treated as a universal numeric threshold until corroborated.

## Batch-level patterns for later corroboration

These are repeated source themes, not yet validated best practices:

1. **Orientation is a geometry decision, not a slicer afterthought.** Multiple videos choose a build direction that puts flexible/load-bearing features within layer paths, then redesign bed contact and stabilization around that direction.
2. **Chamfer first, fillet selectively.** Chamfers are repeatedly preferred at bed-facing and downward-facing transitions; fillets remain useful on vertical/cosmetic/stress transitions where their curvature does not create an unsupported start.
3. **Design out support, then design support.** The sequence is: change orientation/shape; if support remains, model only what is needed; make it stable, accessible, labeled where useful, and intentionally breakable.
4. **Replace rigid nominal tolerance with compliance.** Grip fins, split tabs, tapered entries, relief slots, and limited contact surfaces are recurring methods for absorbing process variation.
5. **Encode local toolpath intent in geometry.** Small cuts/holes are used to provoke extra perimeters around stress regions. This is also the theme most dependent on slicer/mesh behavior and therefore needs careful independent testing.
6. **Production preparation includes removal and inspection.** First-layer release, support-removal access, witness-mark placement, part count, hardware insertion, and a full workflow prototype recur alongside printability.
7. **Avoid turning Slant 3D heuristics into constants.** Several videos use a 0.4 mm-nozzle/approximately 0.2 mm-layer production context, while titles/narration sometimes overstate universality. Numeric rules must be parameterized and independently verified.

