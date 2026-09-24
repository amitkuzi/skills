# Slant 3D claim extraction: core design and orientation, batch 05

- **Research date:** 2026-09-24
- **Scope:** 25 definite-relevance videos not present in batches 01-04, selected for reusable CAD, orientation, support, fit, assembly, and production-preparation guidance.
- **Purpose:** preserve timestamped channel claims before independent engineering reconciliation.
- **Not done here:** endorsement, independent validation, or automatic conversion of a claim into a skill rule.

## Method and evidence limits

The complete official YouTube English automatic-caption track (`en-orig`) was read for every video, from its first event through its final event. Metadata supplied title, date, duration, and URL. Caption files were transient and are not reproduced here.

Claims are paraphrased. “Confidence” is confidence that the paraphrase represents the video, not that the engineering proposition is correct.

- **High:** clear spoken claim at an unambiguous point.
- **Medium:** clear proposal whose usefulness depends on geometry, material, process, or unshown testing.
- **Low:** important numerical or causal assertion inadequately supported by the accessible evidence.

No manually authored English captions were available. On-screen dimensions and unspoken CAD details are outside scope. Ambiguous numerical captions were not converted into rules. No video in this batch was inaccessible; all 25 caption tracks ran from 00:00 to the final seconds of the listed duration.

## Batch manifest

| # | Video | Date | Duration | Primary topics |
|---:|---|---:|---:|---|
| 1 | [Designing Wheels Using Shapr3D's Parametric Modeling](https://www.youtube.com/watch?v=id_b-5kcIpo) | 2024-01-23 | 18:18 | parameters, references, variants |
| 2 | [3D Printed Christmas Ornaments](https://www.youtube.com/watch?v=Iauvzy5mR90) | 2023-12-23 | first layers, loops, designed support |
| 3 | [3D Printing Engineer Reacts To Raspberry Pi Cases](https://www.youtube.com/watch?v=31FVZIg4rDs) | 2023-11-22 | enclosures, mounts, ports, assembly |
| 4 | [3D Printing Engineer Reacts to Phone Stands](https://www.youtube.com/watch?v=d6bt-QtZhqI) | 2023-10-21 | islands, overhangs, consolidation |
| 5 | [Impossible Gears](https://www.youtube.com/watch?v=vsYtffk44J0) | 2023-09-22 | pulleys, hollow forms, variants |
| 6 | [Upgrading Filament Extrusion Line](https://www.youtube.com/watch?v=oUTYhkFzn3w) | 2023-09-16 | grip grooves, orientation, flow paths |
| 7 | [Designing Panel Covers](https://www.youtube.com/watch?v=DnPu7slvBVk) | 2023-09-06 | chamfers, edge printing, stabilization |
| 8 | [Rounded Electrical Enclosures](https://www.youtube.com/watch?v=m20UPm0TOto) | 2023-09-01 | facets, vents, internal mounts |
| 9 | [Command Strip Wall Hooks](https://www.youtube.com/watch?v=W45TqjY51Zg) | 2023-08-25 | hook orientation, adhesive faces, folding |
| 10 | [Customizable Organizer Drawers](https://www.youtube.com/watch?v=CpQGNRWWXs8) | 2023-08-24 | print-together assemblies, inspection |
| 11 | [Can you 3D Print a Water Bottle?](https://www.youtube.com/watch?v=7-LP9UcdAWc) | 2023-08-18 | split shells, liner, impact protection |
| 12 | [Command Strip Handles](https://www.youtube.com/watch?v=tb1yqVOyAM8) | 2023-08-11 | handle strength, adhesive loading |
| 13 | [Corner Brackets](https://www.youtube.com/watch?v=NLeTvSaPJIs) | 2023-08-01 | brackets, hollow volume, extrusion wraps |
| 14 | [Lid Loops](https://www.youtube.com/watch?v=oYEV-ndgwdk) | 2023-07-25 | loop orientation, chamfers, flush loops |
| 15 | [These Cooling Vents are Impossible](https://www.youtube.com/watch?v=vcgsQyMSSiY) | 2023-07-22 | vents, islands, light paths, airflow |
| 16 | [3D Printed Golf Tees](https://www.youtube.com/watch?v=yz8bgl1qnMc) | 2023-07-20 | load paths, ribs, deliberate breakaway |
| 17 | [Handle Variations Part 2](https://www.youtube.com/watch?v=ofUlxe7GfKI) | 2023-07-13 | low-material handles, handed variants |
| 18 | [Optimizing Wall Mounted Electrical Enclosures](https://www.youtube.com/watch?v=SSHoQLuVJFk) | 2023-06-29 | first-layer ties, holes, reinforcement |
| 19 | [Unique Handle Variations](https://www.youtube.com/watch?v=rUUq4kgi7t4) | 2023-06-17 | fin handles, loop roots, ergonomics |
| 20 | [Designing Text for Mass Production 3D Printing](https://www.youtube.com/watch?v=TH82TSjI67I) | 2023-06-10 | text placement, embossing, internal marks |
| 21 | [3D Printing Surface Finishes](https://www.youtube.com/watch?v=FVZ5wAzNAB0) | 2023-06-02 | layer height, texture, post-processing |
| 22 | [Make any Wheel You Need](https://www.youtube.com/watch?v=0wXasxfPBi4) | 2023-06-01 | compliant wheels, hubs, customization |
| 23 | [Ethernet Switch Bracket](https://www.youtube.com/watch?v=Wd0MR4sPcK0) | 2023-03-29 | slots, cable roofs, fastener support |
| 24 | [AVOID These Common Mistakes with 3D Printed Products](https://www.youtube.com/watch?v=sQflKQHDGsI) | 2023-03-14 | process fit, scale, cost, product value |
| 25 | [Improve Designs Using Fillets](https://www.youtube.com/watch?v=C0H_4fOm9CQ) | 2022-10-25 | tool motion, corners, ringing |

## Extracted claims

### 1. Designing Wheels Using Shapr3D's Parametric Modeling

- **Source:** [video](https://www.youtube.com/watch?v=id_b-5kcIpo), 2024-01-23, 18:18.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-18:17.
- **Claims:**
  - [03:44](https://www.youtube.com/watch?v=id_b-5kcIpo&t=224s) Define relationships between functional features instead of fixing every dimension independently, so a wheel family can change without losing intent. **Confidence: High.**
  - [04:13](https://www.youtube.com/watch?v=id_b-5kcIpo&t=253s) Extruding to an existing face/object can preserve a through-feature when body thickness changes. **Confidence: High.**
  - [05:45](https://www.youtube.com/watch?v=id_b-5kcIpo&t=345s) Constrain mounting-hole spacing independently from outside diameter when those interfaces must vary separately. **Confidence: High.**
  - [07:44](https://www.youtube.com/watch?v=id_b-5kcIpo&t=464s) Apply a fillet to the seed feature before patterning it when the fillet must repeat; feature-history order controls the result. **Confidence: High.**
  - [14:05](https://www.youtube.com/watch?v=id_b-5kcIpo&t=845s) Preserve a working baseline and use history breakpoints or duplicates when exploring variants. **Confidence: High.**
- **Conditions/exceptions:** Parametric methods and names are CAD-specific; referenced topology can still break after large edits. Example dimensions are not manufacturing limits.
- **Internal tension:** The video promotes rapid family generation, but does not demonstrate that every generated size retains printable wall thickness, clearance, or load capacity.

### 2. 3D Printed Christmas Ornaments

- **Source:** [video](https://www.youtube.com/watch?v=Iauvzy5mR90), 2023-12-23, 16:05.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-16:04.
- **Claims:**
  - [00:52](https://www.youtube.com/watch?v=Iauvzy5mR90&t=52s) Blunt an otherwise perfect printed tip so a tiny upper cross-section does not dwell under the nozzle and deform. **Confidence: High.**
  - [02:01](https://www.youtube.com/watch?v=Iauvzy5mR90&t=121s) A temporary spine or small ties can connect fragile, separated first-layer regions into a more reliable path. **Confidence: High.**
  - [02:32](https://www.youtube.com/watch?v=Iauvzy5mR90&t=152s) An upright hanging loop loads interlayer bonds; integrate the loop into a stronger body feature or orient its main path in-layer. **Confidence: High.**
  - [04:12](https://www.youtube.com/watch?v=Iauvzy5mR90&t=252s) Round or merge multiple sharp first-layer islands into fewer continuous regions. **Confidence: High.**
  - [10:13](https://www.youtube.com/watch?v=Iauvzy5mR90&t=613s) If support is unavoidable, model a known, localized breakaway feature rather than accepting broad generated support. **Confidence: High.**
- **Conditions/exceptions:** Tie thickness, loop durability, and tip truncation depend on nozzle, material, cooling, and expected handling. Ornament loading does not qualify safety-critical hanging hardware.
- **Internal tension:** The video values intricate appearance but repeatedly simplifies the same geometry for reliable production; appearance and yield must be explicitly traded.

### 3. Raspberry Pi Cases

- **Source:** [video](https://www.youtube.com/watch?v=31FVZIg4rDs), 2023-11-22, 17:21.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-17:20.
- **Claims:**
  - [02:12](https://www.youtube.com/watch?v=31FVZIg4rDs&t=132s) Integrate feet and board-locating features into the enclosure when separate parts add assembly without needed adjustability. **Confidence: High.**
  - [03:09](https://www.youtube.com/watch?v=31FVZIg4rDs&t=189s) Printing an enclosure on an edge can expose cleaner walls and place port openings in more favorable orientations. **Confidence: High.**
  - [05:51](https://www.youtube.com/watch?v=31FVZIg4rDs&t=351s) Designed support may be appropriate directly under ports when edge orientation otherwise leaves a poor underside. **Confidence: High.**
  - [07:26](https://www.youtube.com/watch?v=31FVZIg4rDs&t=446s) Reduce fastener count by using locating or snap features for alignment and screws only where retention requires them. **Confidence: High.**
  - [15:41](https://www.youtube.com/watch?v=31FVZIg4rDs&t=941s) Keep a connector opening wholly within one shell half when splitting it across halves would duplicate alignment and overhang problems. **Confidence: High.**
- **Conditions/exceptions:** Port access, board tolerances, cooling, ESD, serviceability, and fastener retention still require system-level validation. Folding one-piece enclosures depend strongly on material and hinge orientation.
- **Internal tension:** Eliminating hardware simplifies assembly but can reduce serviceability and fatigue life; the video presents both snaps and screws without a universal winner.

### 4. Phone Stands

- **Source:** [video](https://www.youtube.com/watch?v=d6bt-QtZhqI), 2023-10-21, 22:55.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-22:54.
- **Claims:**
  - [01:14](https://www.youtube.com/watch?v=d6bt-QtZhqI&t=74s) Avoid a complex first layer made of many independent islands because each start/stop increases failure opportunities. **Confidence: High.**
  - [02:40](https://www.youtube.com/watch?v=d6bt-QtZhqI&t=160s) Vertical ripples can stiffen a thin vase-like wall while retaining a continuous toolpath. **Confidence: High.**
  - [04:20](https://www.youtube.com/watch?v=d6bt-QtZhqI&t=260s) Replace a broad unsupported underside with a pyramidal or arched transition that grows progressively. **Confidence: High.**
  - [07:07](https://www.youtube.com/watch?v=d6bt-QtZhqI&t=427s) A symmetric pointed top and bottom can make orientation-dependent surface transitions less visually inconsistent. **Confidence: Medium.**
  - [17:01](https://www.youtube.com/watch?v=d6bt-QtZhqI&t=1021s) Consolidate parts or use print-in-place motion when it truly removes assembly and separate inventory. **Confidence: High.**
- **Conditions/exceptions:** Continuous paths, clearances, and surface equality require slicing and physical trials. Consolidation can hinder repair or force an unfavorable orientation.
- **Internal tension:** The video favors single-part products while also showing cases where separate features simplify printing; consolidation is conditional, not absolute.

### 5. Impossible Gears

- **Source:** [video](https://www.youtube.com/watch?v=vsYtffk44J0), 2023-09-22, 8:48.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:47.
- **Claims:**
  - [01:47](https://www.youtube.com/watch?v=vsYtffk44J0&t=107s) Begin by checking the actual pulley load; a metal component may be unnecessary in a low-stress transfer. **Confidence: Medium.**
  - [03:35](https://www.youtube.com/watch?v=vsYtffk44J0&t=215s) Rapidly test several diameters rather than assuming the first ratio or belt path is correct. **Confidence: High.**
  - [05:06](https://www.youtube.com/watch?v=vsYtffk44J0&t=306s) A thick hollow pulley can retain useful section depth while reducing mass and material relative to a solid form. **Confidence: High.**
  - [05:58](https://www.youtube.com/watch?v=vsYtffk44J0&t=358s) Parameterized families can supply many low-volume sizes without maintaining equivalent physical inventory. **Confidence: High.**
- **Conditions/exceptions:** Tooth geometry, wear, temperature, creep, balance, shaft fit, and duty cycle require testing. The [04:36](https://www.youtube.com/watch?v=vsYtffk44J0&t=276s) statement that the printed pulley is as strong as the belt or steel counterpart is unsupported by a shown test and is not adopted.
- **Internal tension:** The video argues from low applied stress, then uses broad material-strength language; those are not equivalent claims.

### 6. Upgrading Filament Extrusion Line

- **Source:** [video](https://www.youtube.com/watch?v=oUTYhkFzn3w), 2023-09-16, 4:56.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:55.
- **Claims:**
  - [01:14](https://www.youtube.com/watch?v=oUTYhkFzn3w&t=74s) Use printable gripping grooves rather than sharp teeth below the process's reliable feature scale. **Confidence: High.**
  - [01:46](https://www.youtube.com/watch?v=oUTYhkFzn3w&t=106s) An octagonal exterior provides a flat print face while retaining multiple working orientations. **Confidence: High.**
  - [03:12](https://www.youtube.com/watch?v=oUTYhkFzn3w&t=192s) Angle outlet slots so each layer can grow from existing material instead of starting disconnected islands. **Confidence: High.**
  - [03:26](https://www.youtube.com/watch?v=oUTYhkFzn3w&t=206s) Favor a continuous loop around the flow feature when repeated isolated starts would reduce production reliability. **Confidence: High.**
- **Conditions/exceptions:** Groove grip and outlet flow depend on polymer, temperature, pressure, and mating geometry; the video does not quantify either.
- **Internal contradictions:** None material observed.

### 7. Designing Panel Covers

- **Source:** [video](https://www.youtube.com/watch?v=DnPu7slvBVk), 2023-09-06, 6:46.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-06:45.
- **Claims:**
  - [00:57](https://www.youtube.com/watch?v=DnPu7slvBVk&t=57s) Use a chamfer rather than an underside fillet on the bed-facing perimeter so the transition grows from supported material. **Confidence: High.**
  - [02:21](https://www.youtube.com/watch?v=DnPu7slvBVk&t=141s) Contrast textured panel surfaces with smoother text or logos to improve legibility without another material. **Confidence: High.**
  - [03:18](https://www.youtube.com/watch?v=DnPu7slvBVk&t=198s) Put important side text in an orientation where it is produced by vertical walls rather than a rough top or first layer. **Confidence: High.**
  - [04:05](https://www.youtube.com/watch?v=DnPu7slvBVk&t=245s) Print a large thin cover on edge when that improves visible finish and automated removal, then model feet/fins to stabilize that orientation. **Confidence: High.**
- **Conditions/exceptions:** Edge printing increases height and can worsen wobble, warp, or cycle time. Stabilizers must not obstruct the product interface and may need removal.
- **Internal tension:** The preferred edge orientation reduces bed contact, then requires extra geometry to restore stability.

### 8. Rounded Electrical Enclosures

- **Source:** [video](https://www.youtube.com/watch?v=m20UPm0TOto), 2023-09-01, 12:23.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-12:22.
- **Claims:**
  - [00:27](https://www.youtube.com/watch?v=m20UPm0TOto&t=27s) Many thin vent features create brittle geometry and excessive tool starts; reduce their count or increase section size. **Confidence: High.**
  - [02:42](https://www.youtube.com/watch?v=m20UPm0TOto&t=162s) Faceting a rounded enclosure can create a stable print face and make surface texture intentional. **Confidence: High.**
  - [03:23](https://www.youtube.com/watch?v=m20UPm0TOto&t=203s) Truncate the lower part of a curve as it approaches horizontal instead of forcing a progressively worse underside. **Confidence: High.**
  - [03:46](https://www.youtube.com/watch?v=m20UPm0TOto&t=226s) Make vent openings longer and walls thicker, then angle the slots to preserve opening area with more robust features. **Confidence: High.**
  - [05:02](https://www.youtube.com/watch?v=m20UPm0TOto&t=302s) Join individual internal standoffs into a plate when a common base improves printing and alignment. **Confidence: High.**
- **Conditions/exceptions:** Vent area is not equivalent to cooling performance; airflow, pressure drop, EMI, ingress, and heat still require analysis and test.
- **Internal tension:** The design removes thin details for reliability while adding faceted texture; any texture must remain above the same feature-size threshold.

### 9. Command Strip Wall Hooks

- **Source:** [video](https://www.youtube.com/watch?v=W45TqjY51Zg), 2023-08-25, 5:59.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:58.
- **Claims:**
  - [00:55](https://www.youtube.com/watch?v=W45TqjY51Zg&t=55s) Side orientation places hook loads more within layer planes, but creates different visible finishes on opposing faces. **Confidence: High.**
  - [01:54](https://www.youtube.com/watch?v=W45TqjY51Zg&t=114s) Vertical orientation is production-friendly for wall shape but exposes the hook root to interlayer loading. **Confidence: High.**
  - [03:18](https://www.youtube.com/watch?v=W45TqjY51Zg&t=198s) A triangular or sloped slot can avoid a flat unsupported roof while retaining access for the adhesive tab. **Confidence: High.**
  - [03:33](https://www.youtube.com/watch?v=W45TqjY51Zg&t=213s) Put the adhesive contact face on the bed when a flat, consistent bonding surface is more important than preserving its cosmetic texture. **Confidence: High.**
  - [04:38](https://www.youtube.com/watch?v=W45TqjY51Zg&t=278s) A print-in-place folding hook can align its final load path after printing and remove assembly. **Confidence: Medium.**
- **Conditions/exceptions:** Adhesive preparation, hinge fatigue, creep, release-tab access, and rated wall load require physical validation.
- **Internal tension:** No single orientation simultaneously optimizes hook strength, surface finish, adhesive face, and automatic production; the video deliberately exposes the tradeoff.

### 10. Customizable Organizer Drawers

- **Source:** [video](https://www.youtube.com/watch?v=CpQGNRWWXs8), 2023-08-24, 11:48.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-11:47.
- **Claims:**
  - [02:37](https://www.youtube.com/watch?v=CpQGNRWWXs8&t=157s) A drawer and housing can print together if the back is open and clearances/chamfers prevent captive overhangs. **Confidence: High.**
  - [03:42](https://www.youtube.com/watch?v=CpQGNRWWXs8&t=222s) Rib a front handle into the drawer body so pulling force is not concentrated at a weak layer boundary. **Confidence: High.**
  - [04:19](https://www.youtube.com/watch?v=CpQGNRWWXs8&t=259s) Add a visual inspection gap and a small state indicator so workers can see whether the drawer exists and has been reset. **Confidence: High.**
  - [08:17](https://www.youtube.com/watch?v=CpQGNRWWXs8&t=497s) Digitally pattern a standard module to create larger organizers instead of assembling repeated shells. **Confidence: High.**
  - [08:46](https://www.youtube.com/watch?v=CpQGNRWWXs8&t=526s) A small sacrificial shipping tie can keep a moving component closed until first use. **Confidence: High.**
- **Conditions/exceptions:** Print-in-place clearance, tie force, wear, and shipping shock are process and material dependent; consolidation may make a damaged drawer housing harder to repair.
- **Internal contradictions:** None material observed.

### 11. Can you 3D Print a Water Bottle?

- **Source:** [video](https://www.youtube.com/watch?v=7-LP9UcdAWc), 2023-08-18, 9:06.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-09:02.
- **Claims:**
  - [03:35](https://www.youtube.com/watch?v=7-LP9UcdAWc&t=215s) External fins can protect a contained vessel from impact while also defining the shell's aesthetic. **Confidence: Medium.**
  - [04:03](https://www.youtube.com/watch?v=7-LP9UcdAWc&t=243s) Split the protective shell into two repeatable halves when that creates printable faces and simplifies manufacturing. **Confidence: High.**
  - [04:16](https://www.youtube.com/watch?v=7-LP9UcdAWc&t=256s) Chamfer or facet the split-shell print face instead of leaving a broad rounded underside. **Confidence: High.**
  - [04:35](https://www.youtube.com/watch?v=7-LP9UcdAWc&t=275s) Use tongue-and-groove registration to align shell halves and transfer shear across the joint. **Confidence: High.**
  - [06:11](https://www.youtube.com/watch?v=7-LP9UcdAWc&t=371s) Use a separate qualified inner bladder for liquid contact and sealing while the printed shell supplies structure and appearance. **Confidence: High.**
- **Conditions/exceptions:** Food contact, cleaning, leakage, impact, and liner replacement must be independently qualified. The shell alone is not established as hygienic or watertight.
- **Internal tension:** The title asks whether a bottle can be printed, but the workable proposal relies on a separate liner; it is a printed bottle system, not proof of a fully FDM liquid vessel.

### 12. Command Strip Handles

- **Source:** [video](https://www.youtube.com/watch?v=tb1yqVOyAM8), 2023-08-11, 14:43.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-14:42.
- **Claims:**
  - [01:39](https://www.youtube.com/watch?v=tb1yqVOyAM8&t=99s) Print a pull handle on its side so the main loop and pulling load lie more within the layers. **Confidence: High.**
  - [02:32](https://www.youtube.com/watch?v=tb1yqVOyAM8&t=152s) Move adhesive pads toward the load to reduce the peel moment rather than relying only on adhesive area. **Confidence: High.**
  - [02:56](https://www.youtube.com/watch?v=tb1yqVOyAM8&t=176s) Recess the adhesive strip thickness so the surrounding body can sit flush against the surface. **Confidence: High.**
  - [07:26](https://www.youtube.com/watch?v=tb1yqVOyAM8&t=446s) An upside-down corner-handle geometry can let each wall grow without generated support and minimize bed contact. **Confidence: High.**
- **Conditions/exceptions:** Adhesive specifications, surface preparation, sustained peel, creep, and user load govern safety. Orientation alone does not establish capacity.
- **Internal tension:** Reducing bed contact may improve visible surfaces but reduces adhesion during printing; the geometry must manage both.

### 13. Corner Brackets

- **Source:** [video](https://www.youtube.com/watch?v=NLeTvSaPJIs), 2023-08-01, 8:40.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:36.
- **Claims:**
  - [01:01](https://www.youtube.com/watch?v=NLeTvSaPJIs&t=61s) A simple upright L-bracket can split at its elbow or through layer interfaces under opening load. **Confidence: High.**
  - [02:30](https://www.youtube.com/watch?v=NLeTvSaPJIs&t=150s) Prefer a substantial joined volume over a collection of thin ribs when ribs create fragile starts and stress raisers. **Confidence: Medium.**
  - [03:33](https://www.youtube.com/watch?v=NLeTvSaPJIs&t=213s) Select orientation so deposited paths wrap around the corner/load path instead of stacking the joint as a peel plane. **Confidence: High.**
  - [05:16](https://www.youtube.com/watch?v=NLeTvSaPJIs&t=316s) Wrap the bracket around an extrusion to combine corner connection, end cap, and fastener location. **Confidence: High.**
  - [07:16](https://www.youtube.com/watch?v=NLeTvSaPJIs&t=436s) A thick hollow body can obtain depth and outer perimeters without paying the mass cost of a solid block. **Confidence: High.**
- **Conditions/exceptions:** The best orientation changes with load direction, screw access, dimensional accuracy, and bed stability. Thick shells are not proof against buckling or creep.
- **Internal tension:** The video favors thick volume over ribs, but a well-engineered rib can be more efficient; the criticism applies to the demonstrated thin, poorly oriented ribs, not all ribbing.

### 14. Lid Loops

- **Source:** [video](https://www.youtube.com/watch?v=oYEV-ndgwdk), 2023-07-25, 5:41.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:36.
- **Claims:**
  - [01:19](https://www.youtube.com/watch?v=oYEV-ndgwdk&t=79s) Keep a pull loop in the layer plane when possible so the loop and its roots are continuous. **Confidence: High.**
  - [02:25](https://www.youtube.com/watch?v=oYEV-ndgwdk&t=145s) If the loop must grow outward, chamfer its underside instead of leaving a horizontal overhang. **Confidence: High.**
  - [03:55](https://www.youtube.com/watch?v=oYEV-ndgwdk&t=235s) An embedded diagonal loop can preserve a low external profile while avoiding an unsupported horizontal roof. **Confidence: High.**
  - [04:21](https://www.youtube.com/watch?v=oYEV-ndgwdk&t=261s) Recess a U-like loop/channel into the lid when a flush, snag-resistant surface is required. **Confidence: Medium.**
- **Conditions/exceptions:** Finger access, local wall thickness, notch sensitivity, cleaning, and repeated pull fatigue must be tested.
- **Internal tension:** Making a loop flush reduces snagging but can reduce access; ergonomics and printability compete.

### 15. These Cooling Vents are Impossible

- **Source:** [video](https://www.youtube.com/watch?v=vcgsQyMSSiY), 2023-07-22, 11:05.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-11:03.
- **Claims:**
  - [00:57](https://www.youtube.com/watch?v=vcgsQyMSSiY&t=57s) A field of small through-holes produces many isolated perimeters and tool starts and can act like a perforation line. **Confidence: High.**
  - [03:18](https://www.youtube.com/watch?v=vcgsQyMSSiY&t=198s) Add connecting ribs or designed support where a vent slot would otherwise begin in midair. **Confidence: High.**
  - [03:37](https://www.youtube.com/watch?v=vcgsQyMSSiY&t=217s) Angle slots so their roofs grow progressively and their cross-section can be larger than unsupported horizontal holes. **Confidence: High.**
  - [04:14](https://www.youtube.com/watch?v=vcgsQyMSSiY&t=254s) An S-shaped light path can block a direct line of sight while retaining an airflow passage, but needs sufficient enclosure thickness. **Confidence: High.**
- **Conditions/exceptions:** Airflow, pressure drop, acoustics, filtration, ingress, and thermal performance require simulation or physical testing. The [07:22](https://www.youtube.com/watch?v=vcgsQyMSSiY&t=442s) vortex/flow-improvement proposal is unmeasured and must not be treated as validated.
- **Internal tension:** Enlarging and redirecting vents improves printability but can increase wall thickness and flow resistance; “more printable” is not automatically “better cooling.”

### 16. 3D Printed Golf Tees

- **Source:** [video](https://www.youtube.com/watch?v=yz8bgl1qnMc), 2023-07-20, 8:43.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:42.
- **Claims:**
  - [02:18](https://www.youtube.com/watch?v=yz8bgl1qnMc&t=138s) Orient a long tee on its side when axial strength and a continuous shaft are priorities. **Confidence: High.**
  - [03:40](https://www.youtube.com/watch?v=yz8bgl1qnMc&t=220s) Limit the ground-entering cross-section so insertion force does not grow merely to obtain strength elsewhere. **Confidence: High.**
  - [04:10](https://www.youtube.com/watch?v=yz8bgl1qnMc&t=250s) Place wide ribs far from the centerline to increase section efficiency while keeping the penetrating tip narrow. **Confidence: High.**
  - [04:42](https://www.youtube.com/watch?v=yz8bgl1qnMc&t=282s) Orientation and notch geometry can deliberately tune a tee from reusable to predictably breakaway. **Confidence: Medium.**
- **Conditions/exceptions:** Soil, impact, material, temperature, club contact, and litter behavior affect performance. The choice between durability and breakaway is a product requirement, not a universal strength objective.
- **Internal tension:** The video alternates between maximizing strength and designing easy breakage; both are coherent only for different user requirements.

### 17. Handle Variations Part 2

- **Source:** [video](https://www.youtube.com/watch?v=ofUlxe7GfKI), 2023-07-13, 10:42.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-10:38.
- **Claims:**
  - [00:34](https://www.youtube.com/watch?v=ofUlxe7GfKI&t=34s) Begin with the minimum handling feature—possibly no loop, only nubs—when the user needs purchase rather than full finger clearance. **Confidence: High.**
  - [00:58](https://www.youtube.com/watch?v=ofUlxe7GfKI&t=58s) Fin-like handles can provide finger engagement with continuous, low-material geometry. **Confidence: High.**
  - [04:04](https://www.youtube.com/watch?v=ofUlxe7GfKI&t=244s) Eye-style handles should be oriented so the ring grows in-plane rather than forming a weak upright loop. **Confidence: High.**
  - [05:12](https://www.youtube.com/watch?v=ofUlxe7GfKI&t=312s) Produce mirrored left- and right-handed variants digitally when hand-specific ergonomics matters. **Confidence: High.**
  - [07:38](https://www.youtube.com/watch?v=ofUlxe7GfKI&t=458s) Thicker sculpted handles may improve grip, but must retain printable transitions and adequate root area. **Confidence: Medium.**
- **Conditions/exceptions:** User hand range, gloves, accessibility, load, cleaning, and fatigue require testing. Minimal handles can be inaccessible even if printable.
- **Internal contradictions:** None material observed.

### 18. Optimizing Wall Mounted Electrical Enclosures

- **Source:** [video](https://www.youtube.com/watch?v=SSHoQLuVJFk), 2023-06-29, 8:23.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:22.
- **Claims:**
  - [01:42](https://www.youtube.com/watch?v=SSHoQLuVJFk&t=102s) Connect frail first-layer spines to the main body with small sacrificial ties so they cannot peel independently. **Confidence: High.**
  - [03:10](https://www.youtube.com/watch?v=SSHoQLuVJFk&t=190s) Rotate mounting holes from vertical to horizontal when this places their loaded material more within the layers. **Confidence: High.**
  - [03:38](https://www.youtube.com/watch?v=SSHoQLuVJFk&t=218s) Add local thickness and a chamfered transition around mounting features rather than thickening the entire enclosure. **Confidence: High.**
  - [05:57](https://www.youtube.com/watch?v=SSHoQLuVJFk&t=357s) Use modeled texture and embedded branding to make layer appearance intentional without a separate finishing operation. **Confidence: High.**
- **Conditions/exceptions:** Fastener torque, countersink geometry, wall pull-out, tie removal, and electrical enclosure requirements need validation. Horizontal holes may be less dimensionally round.
- **Internal tension:** Texture can hide layer variation but adds geometry and tool motion; it is not free production quality.

### 19. Unique Handle Variations

- **Source:** [video](https://www.youtube.com/watch?v=rUUq4kgi7t4), 2023-06-17, 10:18.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-10:14.
- **Claims:**
  - [00:06](https://www.youtube.com/watch?v=rUUq4kgi7t4&t=6s) A traditional upright loop often needs underside support and can retain weak layer-loaded roots. **Confidence: High.**
  - [03:17](https://www.youtube.com/watch?v=rUUq4kgi7t4&t=197s) A fin handle can provide grip with a continuous outward-and-return toolpath. **Confidence: High.**
  - [04:02](https://www.youtube.com/watch?v=rUUq4kgi7t4&t=242s) Continuous geometry around the vessel can reduce stops and locally integrate the handle root. **Confidence: High.**
  - [06:26](https://www.youtube.com/watch?v=rUUq4kgi7t4&t=386s) A ring-and-fin hybrid can preserve familiar finger capture while gaining a more printable base. **Confidence: Medium.**
  - [08:20](https://www.youtube.com/watch?v=rUUq4kgi7t4&t=500s) Shape the fin's curvature for the expected hand posture rather than optimizing only the print. **Confidence: High.**
- **Conditions/exceptions:** Hot contents, filled mass, hand size, root fatigue, and cleaning govern suitability. A continuous path does not alone establish structural capacity.
- **Internal tension:** The video criticizes traditional loops but reintroduces ring geometry when user familiarity and grip demand it.

### 20. Designing Text for Mass Production 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=TH82TSjI67I), 2023-06-10, 7:39.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-07:38.
- **Claims:**
  - [00:04](https://www.youtube.com/watch?v=TH82TSjI67I&t=4s) Place text on a vertical side when possible so character edges are formed as wall paths rather than unsupported top details. **Confidence: High.**
  - [00:38](https://www.youtube.com/watch?v=TH82TSjI67I&t=38s) Both shallow embossing and engraving can work on a side wall; select relief direction based on snagging, contrast, and wall thickness. **Confidence: High.**
  - [02:22](https://www.youtube.com/watch?v=TH82TSjI67I&t=142s) On top surfaces, engraving is often more reliable than small raised letters that begin as separate islands. **Confidence: High.**
  - [04:44](https://www.youtube.com/watch?v=TH82TSjI67I&t=284s) Avoid critical bed-facing text because first-layer compression and bed texture distort it. **Confidence: High.**
  - [05:50](https://www.youtube.com/watch?v=TH82TSjI67I&t=350s) Internal buried identifiers are possible when the goal is traceability rather than visual reading. **Confidence: Medium.**
- **Conditions/exceptions:** Font, stroke width, nozzle, layer height, viewing distance, and scanner resolution matter. The spoken half-millimeter and similar depths are process-specific heuristics, not universal limits; QR/barcode scan reliability is not demonstrated.
- **Internal tension:** Hidden text can aid traceability only if a suitable inspection method can detect it; the video does not establish that method.

### 21. 3D Printing Surface Finishes

- **Source:** [video](https://www.youtube.com/watch?v=FVZ5wAzNAB0), 2023-06-02, 4:18.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:17.
- **Claims:**
  - [00:55](https://www.youtube.com/watch?v=FVZ5wAzNAB0&t=55s) Layer height trades visible resolution against print time; choose it for the product rather than maximizing resolution by default. **Confidence: High.**
  - [01:26](https://www.youtube.com/watch?v=FVZ5wAzNAB0&t=86s) Manual smoothing and painting add labor that is difficult to scale for routine production. **Confidence: High.**
  - [01:51](https://www.youtube.com/watch?v=FVZ5wAzNAB0&t=111s) Modeled texture can change appearance, grip, and surface interaction while hiding some layer-line variation. **Confidence: High.**
  - [02:08](https://www.youtube.com/watch?v=FVZ5wAzNAB0&t=128s) A slicer's fuzzy-surface feature offers another texture route but makes the result dependent on slicer implementation and settings. **Confidence: High.**
- **Conditions/exceptions:** The 0.2 mm recommendation is a platform-specific heuristic, not a cross-printer rule. Texture can enlarge files, slow motion, trap dirt, and alter fit.
- **Internal tension:** The video advocates CAD-first production but includes a slicer-only texture technique; the transferable principle is intentional surface design, not one implementation.

### 22. Make any Wheel You Need

- **Source:** [video](https://www.youtube.com/watch?v=0wXasxfPBi4), 2023-06-01, 5:06.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:05.
- **Claims:**
  - [01:25](https://www.youtube.com/watch?v=0wXasxfPBi4&t=85s) Enclose compliant pockets inside a tire instead of exposing open grooves that collect debris. **Confidence: High.**
  - [01:38](https://www.youtube.com/watch?v=0wXasxfPBi4&t=98s) Internal void patterns can tune compliance while the outer tread remains continuous. **Confidence: Medium.**
  - [03:12](https://www.youtube.com/watch?v=0wXasxfPBi4&t=192s) Separate hub and tread parameters so a supplier or bolt-interface change does not force a complete redesign. **Confidence: High.**
  - [04:11](https://www.youtube.com/watch?v=0wXasxfPBi4&t=251s) Digital variants can reduce tooling and finished-goods inventory for low-volume custom wheels. **Confidence: High.**
- **Conditions/exceptions:** Compliance, rolling resistance, wear, heat, hub retention, balance, and debris sealing need tests. Business claims about tooling and inventory depend on production volume and equipment utilization.
- **Internal tension:** Enclosed voids avoid dirt but make internal defects harder to inspect and can trap moisture.

### 23. Ethernet Switch Bracket

- **Source:** [video](https://www.youtube.com/watch?v=Wd0MR4sPcK0), 2023-03-29, 9:21.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-09:19.
- **Claims:**
  - [01:33](https://www.youtube.com/watch?v=Wd0MR4sPcK0&t=93s) Use rounded slot ends and chamfered entries to reduce sharp transitions and simplify printable walls. **Confidence: High.**
  - [02:55](https://www.youtube.com/watch?v=Wd0MR4sPcK0&t=175s) Give the power cord an explicit routed opening rather than forcing it through a generic rectangular cutout. **Confidence: High.**
  - [04:36](https://www.youtube.com/watch?v=Wd0MR4sPcK0&t=276s) Put local solid material beneath a screw head and around its bearing path instead of relying on sparse interior. **Confidence: High.**
  - [05:23](https://www.youtube.com/watch?v=Wd0MR4sPcK0&t=323s) Chamfer low-value outer volume away while retaining material along load and contact paths. **Confidence: High.**
  - [06:51](https://www.youtube.com/watch?v=Wd0MR4sPcK0&t=411s) Add fillets at vertical stress and cable-contact corners when they do not create underside overhangs. **Confidence: High.**
- **Conditions/exceptions:** Fastener torque, pull-out, cable bend radius, heat, and device retention need validation. “Solid” depends on generated paths, not merely nominal CAD volume.
- **Internal tension:** Fillets are useful on vertical corners here, but the same geometry can be harmful on bed-facing undersides; placement matters.

### 24. AVOID These Common Mistakes with 3D Printed Products

- **Source:** [video](https://www.youtube.com/watch?v=sQflKQHDGsI), 2023-03-14, 4:58.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:56.
- **Claims:**
  - [00:55](https://www.youtube.com/watch?v=sQflKQHDGsI&t=55s) Match the CAD design to the intended manufacturing process instead of sending an unchanged injection-molded form to FDM. **Confidence: High.**
  - [01:25](https://www.youtube.com/watch?v=sQflKQHDGsI&t=85s) Plan for the actual production scale because inspection, quality drift, and failure impact change with quantity. **Confidence: High.**
  - [02:30](https://www.youtube.com/watch?v=sQflKQHDGsI&t=150s) Evaluate cost per acceptable part rather than assuming additive manufacture is automatically cheaper. **Confidence: High.**
  - [04:16](https://www.youtube.com/watch?v=sQflKQHDGsI&t=256s) Product usefulness and customer expectations should control process choice; process novelty is not product value. **Confidence: High.**
- **Conditions/exceptions:** The video supplies principles, not a cost model or quality threshold. Volumes, labor, capital, scrap, and service obligations vary by product.
- **Internal contradictions:** None material observed.

### 25. Improve Designs Using Fillets

- **Source:** [video](https://www.youtube.com/watch?v=C0H_4fOm9CQ), 2022-10-25, 4:04.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-03:57.
- **Claims:**
  - [00:43](https://www.youtube.com/watch?v=C0H_4fOm9CQ&t=43s) Round vertical corners to avoid abrupt direction changes that can excite ringing and leave blobs. **Confidence: High.**
  - [01:58](https://www.youtube.com/watch?v=C0H_4fOm9CQ&t=118s) In the demonstrated part, a three-millimeter fillet reportedly reduced the slice estimate by roughly four to five minutes. **Confidence: Low** because only one example and no controlled comparison are shown.
  - [02:45](https://www.youtube.com/watch?v=C0H_4fOm9CQ&t=165s) Smoother vertical paths may improve exterior consistency by reducing sharp accelerations. **Confidence: High.**
  - [03:35](https://www.youtube.com/watch?v=C0H_4fOm9CQ&t=215s) The video generalizes that filleted designs print better. **Confidence: Low** as a universal claim.
- **Conditions/exceptions:** Functional corners, mating interfaces, tool access, stress direction, and bed-facing surfaces may require sharp corners or chamfers. The numerical time saving is an unsupported single-slice heuristic, not a rule.
- **Internal tension:** The categorical “fillets print better” framing conflicts with later Slant 3D guidance in this batch and earlier batches that warns against underside fillets; the defensible claim is limited to appropriately placed, mainly vertical fillets.

## Batch-level synthesis

Repeated themes across these 25 videos:

1. Choose orientation from the functional load path, then redesign overhangs and first-layer geometry around it.
2. Prefer continuous, connected toolpaths over isolated islands, thin ribs, and repeated tiny features.
3. Use chamfers, facets, arches, slots, and designed sacrificial ties to make unavoidable transitions self-supporting.
4. Consolidate parts only when it removes real assembly without sacrificing serviceability, tolerance, or a better per-part orientation.
5. Parameterize functional interfaces and variants, but revalidate walls, clearances, loads, and printability for every generated size.
6. Treat surface texture, text, and product state indicators as design features, while accounting for file size, hygiene, and inspection.
7. Separate structural shells from qualified liners or hardware when FDM alone cannot meet sealing, food-contact, wear, or safety requirements.

## Unsupported numerical and categorical heuristics flagged

- `vsYtffk44J0` [04:36]: “as strong as” belt/steel language lacks a shown test.
- `TH82TSjI67I` [01:08]: half-millimeter text depth is process specific.
- `FVZ5wAzNAB0` [00:55]: 0.2 mm layer-height preference is platform/product specific.
- `C0H_4fOm9CQ` [01:58]: four-to-five-minute saving comes from one example.
- `C0H_4fOm9CQ` [03:35]: universal fillet claim conflicts with geometry-specific later advice.
- `vcgsQyMSSiY` [07:22]: vortex/airflow improvement lacks measurement.

## Validation record

- Manifest entries: **25**.
- Unique video IDs: **25**.
- Videos with complete official `en-orig` caption review: **25/25**.
- Video sections with timestamped claims: **25/25**.
- Video sections with explicit conditions/exceptions: **25/25**.
- Video sections with contradiction/tension review: **25/25**.
- Timestamped claim bullets: **113**.
- Overlap with batches 01-04: **0**.
- Inaccessible selected videos: **0**.
- Ambiguous caption-derived numbers promoted to rules: **0**.
