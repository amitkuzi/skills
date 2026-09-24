# Slant 3D claim extraction: core design and orientation, batch 06

- **Research date:** 2026-09-24
- **Scope:** 25 further high-value videos from the definite-relevance set in `relevant-video-candidates-2026-09-24.md`, excluding all sources assigned to batches 01-05.
- **Selection priority:** remaining dedicated CAD/FDM tutorials and product case studies with transferable lessons about orientation, supports, load paths, compliant fits, first-layer contact, feature consolidation, and production handling.
- **Purpose:** record what Slant 3D states before independent validation or conversion into final skill guidance.
- **Not done here:** independent corroboration, engineering endorsement, safety approval, or conversion into universal numeric rules.

## Method and evidence limits

For every source, the complete official YouTube English automatic-caption track (`en-orig`) was retrieved with `yt-dlp` in JSON3 format and reviewed from its first caption event through its final event. Official YouTube metadata supplied title, upload date, duration, and URL. Caption files were transient and were deleted after extraction; no full transcript is retained or reproduced here.

Claims are concise paraphrases. Each claim links to the official video at the relevant timestamp. “Confidence” indicates confidence that the paraphrase represents the video, **not** confidence that the engineering advice is correct.

- **High:** clear spoken claim with an unambiguous timestamp.
- **Medium:** clear general claim whose applicability depends on the shown geometry, material, machine, or load case.
- **Low:** an absolute, safety-sensitive, numerical, or causal claim that the accessible evidence does not adequately support.

Evidence gaps and exclusions:

- No manually authored English captions were available; the evidence was the official automatic-caption track.
- Fine on-screen dimensions and geometry not described aloud were not inferred.
- Audio was not separately human-audited. Ambiguous numbers and units were not turned into portable rules.
- Product safety, regulatory compliance, durability, and sales-volume statements were not independently verified.
- All 25 selected videos exposed full-length captions. Inaccessible primary-caption evidence: **none**.

## Batch manifest

| # | Video | Date | Duration | Primary topics |
|---:|---|---:|---:|---|
| 1 | [I Made a Round Ruler](https://www.youtube.com/watch?v=Ilw96xcxDz4) | 2026-03-13 | 23:56 | iterative product design, overhangs, fits, consolidation |
| 2 | [Can I Design a Perfect iPhone Standby Dock](https://www.youtube.com/watch?v=QcqTncnBDAw) | 2025-09-27 | 12:16 | side orientation, fillets, prototypes, surface finish |
| 3 | [Perry Parts are a Masterclass in 3D Printing Design](https://www.youtube.com/watch?v=Lmr4LKI0Hfc) | 2025-06-13 | 11:28 | engineered infill, compression, threads, qualification |
| 4 | [Is This the Perfect 3D Print?](https://www.youtube.com/watch?v=JuJEnuLlJgk) | 2025-04-10 | 8:13 | support-free walls, openings, function simplification |
| 5 | [Can We 3D Print Better Pumpkin Carving Tools?](https://www.youtube.com/watch?v=yFUBXBoDT4I) | 2024-10-18 | 9:39 | load orientation, print-in-place assembly, bed details |
| 6 | [We Fixed Morley Kert's OneWheel Stand](https://www.youtube.com/watch?v=boN1uiaIdVA) | 2024-09-25 | 9:54 | supports, ribs, consolidation, local reinforcement |
| 7 | [We Solved Simone Giertz's Problem](https://www.youtube.com/watch?v=GDEMxa4WdRw) | 2024-09-21 | 12:29 | flat orientation, membranes, hinge geometry, retention |
| 8 | [Make the Best Organizer](https://www.youtube.com/watch?v=enj80Vc7i0s) | 2024-08-08 | 4:22 | vertical orientation, stackability, variants |
| 9 | [5 Everyday Products Redesigned with 3D Printing](https://www.youtube.com/watch?v=WVTJOAeZLQ8) | 2024-07-11 | 17:48 | reusable negatives, ducts, side orientation, ribs |
| 10 | [Why You Should 3D Print Your Electrical Enclosures](https://www.youtube.com/watch?v=jNguIjkLo6g) | 2024-06-22 | 5:21 | diagonal enclosures, stabilization, standoffs |
| 11 | [We 3D Printed a Coffee Maker](https://www.youtube.com/watch?v=QBg63t-Gk7s) | 2024-04-25 | 5:40 | orientation, faceting, material efficiency, hybrid parts |
| 12 | [Camouflaging Electrical Enclosures](https://www.youtube.com/watch?v=mV-FWHjlwBk) | 2024-04-18 | 4:07 | Boolean negatives, reusable interfaces, organic shells |
| 13 | [The 3D Printed Product Urban Outfitters Sold Out 4 Times](https://www.youtube.com/watch?v=PbGnxQifEq0) | 2024-03-29 | 9:00 | first layer, compliance, color/process variation, QC |
| 14 | [We Fixed the Dune Popcorn Bucket](https://www.youtube.com/watch?v=chULpzksGSQ) | 2024-03-27 | 5:56 | manufacturing constraints, complex geometry, licensing |
| 15 | [We Made a Better Piggy Bank](https://www.youtube.com/watch?v=KbKeCcvn6_s) | 2024-03-14 | 7:28 | negative tooling, internal ledges, part consolidation |
| 16 | [We Made a Better Spoon](https://www.youtube.com/watch?v=uCxRJxvsoe0) | 2024-02-27 | 4:47 | curved surfaces, vertical orientation, support combs |
| 17 | [Massage Roller Kits](https://www.youtube.com/watch?v=u97dyLy_FuE) | 2023-08-22 | 8:21 | layer direction, texture, hybrid assembly, bed contact |
| 18 | [Birdhouses](https://www.youtube.com/watch?v=reIXSlL6mKA) | 2023-08-05 | 10:24 | inversion, support removal, thick walls, outdoor claims |
| 19 | [Design a Lamp for Mass Production 3D Printing](https://www.youtube.com/watch?v=xEjtyA2b5I0) | 2023-04-05 | 18:58 | reusable base, cable routing, bed recess, edge finishing |
| 20 | [These Free STL's are Better than Tree Supports](https://www.youtube.com/watch?v=YL5lYEXbLDo) | 2023-02-04 | 8:06 | designed tacks, comb supports, small features |
| 21 | [Easiest Way to Eliminate Supports](https://www.youtube.com/watch?v=FMs-VGAu_PQ) | 2022-11-29 | 4:03 | fillets, chamfers, overhang transitions |
| 22 | [3D Printed Parts as Strong As Molded](https://www.youtube.com/watch?v=p-GuXDxQYkA) | 2022-11-08 | 5:35 | load paths, section geometry, material distribution |
| 23 | [The Power of Diagonals](https://www.youtube.com/watch?v=8TIhkxQNINY) | 2022-10-15 | 5:46 | diagonal orientation, supports, cosmetic faces, ejection |
| 24 | [Design for 3D Printing: Grip Fins](https://www.youtube.com/watch?v=yzg_NXM-NRs) | 2022-06-25 | 5:21 | compliant fits, layer direction, lead-ins, fatigue |
| 25 | [Best Design Tips for 3D Printing Production](https://www.youtube.com/watch?v=NaQ_Sa1BaqU) | 2022-05-09 | 6:30 | corner geometry, section efficiency, overhangs, color QC |

## Extracted claims

### 1. I Made a Round Ruler

- **Source:** [video](https://www.youtube.com/watch?v=Ilw96xcxDz4), 2026-03-13, 23:56.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-23:56.
- **Claims:**
  - [03:00](https://www.youtube.com/watch?v=Ilw96xcxDz4&t=180s) Use an intentionally incomplete first prototype to test several uncertain aspects at once rather than polishing an unverified concept. **Confidence: High.**
  - [03:30](https://www.youtube.com/watch?v=Ilw96xcxDz4&t=210s) A local flat can provide a tactile/indexing event, but changing a wheel's circumference also changes its measurement, so the cue affects the primary function. **Confidence: High.**
  - [05:30](https://www.youtube.com/watch?v=Ilw96xcxDz4&t=330s) Replacing spherical side recesses with conical recesses removes the problematic underside overhang in the shown orientation. **Confidence: High.**
  - [06:30](https://www.youtube.com/watch?v=Ilw96xcxDz4&t=390s) A geometry that appears workable can fail through interface behavior—in this case, pinching and low surface friction make the measuring wheel slide instead of roll. **Confidence: High.**
  - [10:00](https://www.youtube.com/watch?v=Ilw96xcxDz4&t=600s) Press-fit dimensions for purchased bearings required prototype correction for material/process shrinkage; a nominal CAD fit was not sufficient. **Confidence: High.**
  - [16:40](https://www.youtube.com/watch?v=Ilw96xcxDz4&t=1000s) Fine engraved notches became visually and functionally weak, while tight corners accumulated material; interaction features must be sized for both the marking tool and the extrusion process. **Confidence: High.**
  - [18:14](https://www.youtube.com/watch?v=Ilw96xcxDz4&t=1094s) Adding bearings and caps turned a one-part concept into a larger five-part product without solving its main problem, so the design returned to the simpler monolithic version. **Confidence: High.**
- **Conditions/exceptions:** Measurement tools require calibration, quantified slip/rolling error, wear, repeatability, and reference-surface tests. The video does not establish metrology-grade accuracy. Press fits depend on the exact material, printer, feature orientation, and bearing tolerance.
- **Internal tension:** The final monolithic object is described as reliable and precise, but the video also identifies slip, circumference distortion, overhang artifacts, and missing customer feedback; the performance conclusion is not demonstrated quantitatively.

### 2. Can I Design a Perfect iPhone Standby Dock

- **Source:** [video](https://www.youtube.com/watch?v=QcqTncnBDAw), 2025-09-27, 12:16.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-12:16.
- **Claims:**
  - [00:32](https://www.youtube.com/watch?v=QcqTncnBDAw&t=32s) A constant bent profile was chosen partly because the dock could print on its side while preserving that profile. **Confidence: High.**
  - [02:31](https://www.youtube.com/watch?v=QcqTncnBDAw&t=151s) A fillet beginning at the build plate creates a near-horizontal initial region; the speaker expected, and the prototype later showed, underside sag there. **Confidence: High.**
  - [02:50](https://www.youtube.com/watch?v=QcqTncnBDAw&t=170s) Put multiple questions into an early prototype so one print reveals form, fit, overhang, wall, and interface problems. **Confidence: High.**
  - [04:15](https://www.youtube.com/watch?v=QcqTncnBDAw&t=255s) Low-infill prints were used for quick form prototypes before committing to final construction. **Confidence: High.**
  - [05:23](https://www.youtube.com/watch?v=QcqTncnBDAw&t=323s) The preferred bend keeps inner and outer curves centered on the same rotation point, avoiding the visually inconsistent result of unrelated radii. **Confidence: Medium** because this is partly an industrial-design judgment.
  - [08:16](https://www.youtube.com/watch?v=QcqTncnBDAw&t=496s) Cropping/truncating the lowest portion of a bed-facing fillet removes its immediate horizontal tangent and improved printability in the redesign. **Confidence: High.**
  - [09:40](https://www.youtube.com/watch?v=QcqTncnBDAw&t=580s) Large uninterrupted visible flats amplify surface defects and create visually inactive space, so they should be justified rather than used by default. **Confidence: Medium.**
- **Conditions/exceptions:** Side printing must still meet stability, seam, load, and visible-surface requirements. Prototype infill should not be used for final strength decisions. Charger placement, phone/case clearance, camera bump, cable bend radius, heat, and electrical compliance need separate validation.
- **Internal tension:** The piece calls the dock final while its concealed cable route still fails the USB bend requirement at [10:27](https://www.youtube.com/watch?v=QcqTncnBDAw&t=627s). The title's “perfect” framing is therefore not an engineering conclusion.

### 3. Perry Parts are a Masterclass in 3D Printing Design

- **Source:** [video](https://www.youtube.com/watch?v=Lmr4LKI0Hfc), 2025-06-13, 11:28.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-11:28.
- **Claims:**
  - [04:19](https://www.youtube.com/watch?v=Lmr4LKI0Hfc&t=259s) CAD-designed internal lattice geometry is used as a progressive spring, controlling how a TPU bump stop compresses instead of relying on a solid rubber block. **Confidence: High.**
  - [05:03](https://www.youtube.com/watch?v=Lmr4LKI0Hfc&t=303s) Internal and external corrugations are presented as functional load-control geometry that also makes the part unsuitable for conventional molding. **Confidence: High.**
  - [06:02](https://www.youtube.com/watch?v=Lmr4LKI0Hfc&t=362s) Printed threads are accepted because they locate/retain a component whose service load is primarily compression, not thread pullout. **Confidence: High.**
  - [07:01](https://www.youtube.com/watch?v=Lmr4LKI0Hfc&t=421s) The product is said to be qualified on a compression dynamometer for 100,000 impacts/cycles rather than accepted from geometry alone. **Confidence: Medium** because the video reports the test but does not show its protocol or records.
  - [07:31](https://www.youtube.com/watch?v=Lmr4LKI0Hfc&t=451s) Keeping the primary load compressive reduces direct layer-separation risk, but the speaker explicitly retains fatigue across layers as a separate failure concern. **Confidence: High.**
  - [08:42](https://www.youtube.com/watch?v=Lmr4LKI0Hfc&t=522s) A multi-element spring function can be consolidated into a monolithic compliant print when the internal geometry is designed for the desired response. **Confidence: High.**
- **Conditions/exceptions:** This is a safety-relevant automotive component. Material batch, temperature, UV/chemical exposure, vehicle mass, travel, mounting, progressive-rate curve, fatigue, and failure consequence must be qualified for each application. Printed threads are appropriate only when their actual load path and retention duty permit them.
- **Internal tension:** The video gives broad material-superiority and durability language, yet the useful engineering lesson is precisely that the part is application-specific and test-qualified. Neither “TPU is best” nor “compression avoids layer issues” is a universal rule.

### 4. Is This the Perfect 3D Print?

- **Source:** [video](https://www.youtube.com/watch?v=JuJEnuLlJgk), 2025-04-10, 8:13.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:13.
- **Claims:**
  - [03:21](https://www.youtube.com/watch?v=JuJEnuLlJgk&t=201s) The reviewed measuring-cup block combines a flat base, rounded bottom edges, thin walls, legible text, and no support-requiring overhangs, which the speaker treats as a robust production layout. **Confidence: High.**
  - [04:02](https://www.youtube.com/watch?v=JuJEnuLlJgk&t=242s) Orienting the largest cup opening upward avoids a broad top skin whose raster would look different from the vertical walls. **Confidence: High.**
  - [04:30](https://www.youtube.com/watch?v=JuJEnuLlJgk&t=270s) Features that are manufacturable but awkward to use should still be removed; the redesign separates small spoons from larger cups rather than preserving every cavity in one block. **Confidence: High.**
  - [04:53](https://www.youtube.com/watch?v=JuJEnuLlJgk&t=293s) Thinning the scoop edges improves access and pouring while making visible surfaces more uniform. **Confidence: High for the shown redesign.**
  - [06:18](https://www.youtube.com/watch?v=JuJEnuLlJgk&t=378s) Multi-directional internal cavities are presented as geometry that suits additive production but would require complex tooling or multiple operations by other processes. **Confidence: High.**
- **Conditions/exceptions:** A measuring product needs volumetric calibration, drainage/cleaning access, food-contact assessment, heat/chemical compatibility, and tolerance verification. Thin walls and text must be checked against the chosen extrusion width and layer height.
- **Internal tension:** At [03:35](https://www.youtube.com/watch?v=JuJEnuLlJgk&t=215s) the speaker says the design works with any material and resolution; that absolute conflicts with material-dependent shrinkage, feature resolution, food use, and cleaning, so it is not portable guidance. “Perfect” is also undercut by the usability redesign.

### 5. Can We 3D Print Better Pumpkin Carving Tools?

- **Source:** [video](https://www.youtube.com/watch?v=yFUBXBoDT4I), 2024-10-18, 9:39.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-09:39.
- **Claims:**
  - [01:30](https://www.youtube.com/watch?v=yFUBXBoDT4I&t=90s) Printing the punch vertically aligns its main hammer load with compression through the layer stack rather than transverse delamination. **Confidence: High.**
  - [02:00](https://www.youtube.com/watch?v=yFUBXBoDT4I&t=120s) The cutting edge is placed away from the build plate so first-layer expansion does not blunt the smallest intended feature. **Confidence: High.**
  - [03:30](https://www.youtube.com/watch?v=yFUBXBoDT4I&t=210s) The body, plunger, and handles are printed as a working one-build assembly to eliminate separate assembly and part inventory. **Confidence: High.**
  - [06:00](https://www.youtube.com/watch?v=yFUBXBoDT4I&t=360s) Small bottom-edge chamfers separate nearby first-layer outlines that might otherwise merge through first-layer expansion. **Confidence: High.**
  - [06:23](https://www.youtube.com/watch?v=yFUBXBoDT4I&t=383s) Side handles use trapezoidal transitions rather than horizontal undersides so they build without separate support. **Confidence: High.**
  - [07:30](https://www.youtube.com/watch?v=yFUBXBoDT4I&t=450s) A long knife is rotated diagonally on the bed to fit within a nominally smaller rectangular build envelope. **Confidence: High.**
  - [08:00](https://www.youtube.com/watch?v=yFUBXBoDT4I&t=480s) Increasing handle leverage and ergonomics can improve control yet overload a printed blade; user safety and part strength must be designed together. **Confidence: High.**
- **Conditions/exceptions:** This is an impact and cutting tool. Material toughness, notch sensitivity, layer adhesion, edge geometry, hammer misuse, fragment risk, hygiene, age/user population, fatigue, and protective measures require real testing. “One holiday use” is not a sufficient safety basis.
- **Internal tension:** The video describes the tool as robust and ready from the machine but also identifies weak grip flanges, thickening at the blade, insufficient local density, circular tracking, and overload from handle leverage. Those prototype shortcomings prevent a general durability claim.

### 6. We Fixed Morley Kert's OneWheel Stand

- **Source:** [video](https://www.youtube.com/watch?v=boN1uiaIdVA), 2024-09-25, 9:54.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-09:54.
- **Claims:**
  - [02:23](https://www.youtube.com/watch?v=boN1uiaIdVA&t=143s) Replacing slicer support beneath a cantilevered leg with an underside chamfer puts the material into the finished load path and removes support-removal labor. **Confidence: High.**
  - [03:08](https://www.youtube.com/watch?v=boN1uiaIdVA&t=188s) A local internal rib reinforces the hinge/leg junction when it does not interfere with the wheel or assembly envelope. **Confidence: High.**
  - [03:46](https://www.youtube.com/watch?v=boN1uiaIdVA&t=226s) Merging two side pieces into one central yoke reduces part count and enables a continuous through-rod assembly. **Confidence: High.**
  - [06:54](https://www.youtube.com/watch?v=boN1uiaIdVA&t=414s) A thick external envelope can remain material-efficient through internal infill while providing room to shape stronger blends and interfaces. **Confidence: Medium** because actual efficiency depends on slicer paths and section geometry.
  - [07:27](https://www.youtube.com/watch?v=boN1uiaIdVA&t=447s) Small enclosed CAD voids are proposed to force additional internal perimeters at a wear zone when downstream production accepts only default settings. **Confidence: Medium** because the feature size and resulting paths are profile-dependent and no strength test is shown.
  - [08:07](https://www.youtube.com/watch?v=boN1uiaIdVA&t=487s) A light modeled texture can reduce the visual prominence of layer lines on a production surface. **Confidence: High.**
- **Conditions/exceptions:** The bracket must be validated for vehicle mass, shock, pavement contact, axle bending, fastener retention, wheel clearance, outdoor exposure, creep, and fatigue. CAD microvoids require slice inspection because they may disappear or create stress raisers. Material substitutions cannot be justified by price alone.
- **Internal tension:** The video says strength is in the skin and likens the print to an I-beam, then proposes local internal paths for reinforcement. Both may be useful descriptions, but neither replaces a load-case analysis or test of the redesigned stand.

### 7. We Solved Simone Giertz's Problem

- **Source:** [video](https://www.youtube.com/watch?v=GDEMxa4WdRw), 2024-09-21, 12:29.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-12:29.
- **Claims:**
  - [06:29](https://www.youtube.com/watch?v=GDEMxa4WdRw&t=389s) A folding hanger is laid flat so the hook and primary beam lie in the layer plane, then fitted diagonally inside the available bed envelope. **Confidence: High.**
  - [07:14](https://www.youtube.com/watch?v=GDEMxa4WdRw&t=434s) A branch printed vertically from that flat body is vulnerable across layers; a thin membrane/shear plate connects the branch back to the body to limit bending. **Confidence: High.**
  - [08:12](https://www.youtube.com/watch?v=GDEMxa4WdRw&t=492s) Raising the hinge axis above the arm centerline lets the two halves fold alongside each other instead of pinching a garment at the original pivot. **Confidence: High.**
  - [08:57](https://www.youtube.com/watch?v=GDEMxa4WdRw&t=537s) Small modeled bumps add local resistance so a garment is less likely to slide from a hanger used at an unusual angle. **Confidence: High.**
  - [09:32](https://www.youtube.com/watch?v=GDEMxa4WdRw&t=572s) Material/aesthetic substitutions can require geometry changes; the video specifically warns that weaker wood-filled filament would need re-engineering. **Confidence: High.**
- **Conditions/exceptions:** Garment weight, long-term creep, hinge cycle life, impact against a wall, sharp edges, membrane tearing, hook opening, bed size, and material conditioning require testing. A thin membrane may be unsuitable where a clean opening or flexible clearance is required.
- **Internal tension:** The proof of concept is repeatedly described as strong, yet the speaker also says the hinge and central support could be redesigned and that alternative materials are weaker. No load or cycle evidence is supplied.

### 8. Make the Best Organizer

- **Source:** [video](https://www.youtube.com/watch?v=enj80Vc7i0s), 2024-08-08, 4:22.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:22.
- **Claims:**
  - [01:24](https://www.youtube.com/watch?v=enj80Vc7i0s&t=84s) Both drawer and housing were designed around vertical printing, with overhangs removed before aesthetic edge rounding was added. **Confidence: High.**
  - [01:46](https://www.youtube.com/watch?v=enj80Vc7i0s&t=106s) Rounding vertical exterior edges can improve the visual language without creating the bed-facing overhang problem of a horizontal fillet. **Confidence: High.**
  - [01:56](https://www.youtube.com/watch?v=enj80Vc7i0s&t=116s) External grooves, feet, and mating recesses act as locating features so modules stack and a chosen level can be handled as a unit. **Confidence: High.**
  - [02:25](https://www.youtube.com/watch?v=enj80Vc7i0s&t=145s) A multi-drawer set may be supplied as one arranged production file, while separable drawers preserve color customization without redesigning the geometry. **Confidence: High.**
  - [02:43](https://www.youtube.com/watch?v=enj80Vc7i0s&t=163s) A shared outer interface can support multiple drawer-interior variants for different objects without changing the stack system. **Confidence: High.**
- **Conditions/exceptions:** Stack fits require tolerance, maximum-height stability, lateral-load, wear, and tip-over tests. Vertical orientation must be assessed against drawer loads and pull direction. Smooth pockets should also be checked for cleanability and object access.
- **Internal tension:** The video promotes thick, smooth filled volumes as a printing advantage but does not compare their print time/material with thinner alternatives or quantify stack strength.

### 9. 5 Everyday Products Redesigned with 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=WVTJOAeZLQ8), 2024-07-11, 17:48.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-17:48.
- **Claims:**
  - [01:23](https://www.youtube.com/watch?v=WVTJOAeZLQ8&t=83s) Model a reusable negative of a functional internal cavity, then subtract it from multiple exterior forms to create a product family with a consistent interface. **Confidence: High.**
  - [02:08](https://www.youtube.com/watch?v=WVTJOAeZLQ8&t=128s) A diagonal internal ledge can stop coins from falling directly through a monolithic bank while guiding them toward a separate exit during tilting. **Confidence: High.**
  - [04:53](https://www.youtube.com/watch?v=WVTJOAeZLQ8&t=293s) Internal air channels, splitters, and outlet slots can consolidate what would otherwise be multiple fan components, though performance still depends on aerodynamic design. **Confidence: High for the geometry claim.**
  - [11:58](https://www.youtube.com/watch?v=WVTJOAeZLQ8&t=718s) A curved coffee stand is printed on its side, with narrow chamfered seams deliberately made the only bed-contact regions so bed texture is less visible. **Confidence: High.**
  - [13:22](https://www.youtube.com/watch?v=WVTJOAeZLQ8&t=802s) Downward filter-locating teeth receive integral pointed/chamfered under-geometry, mirrored on the opposite side so the support strategy reads as intentional form. **Confidence: High.**
  - [15:24](https://www.youtube.com/watch?v=WVTJOAeZLQ8&t=924s) A narrow stake is strengthened by moving broad ribs away from the neutral axis while cutting the center away to retain a small ground-entry cross-section. **Confidence: High.**
  - [16:28](https://www.youtube.com/watch?v=WVTJOAeZLQ8&t=988s) Printing that ribbed stake on its side aligns the length with the layer plane for the expected bending load. **Confidence: High.**
- **Conditions/exceptions:** Reusable negatives need controlled clearances and wall-thickness checks in every host form. Airflow claims require pressure/flow/noise tests. Coffee-contact geometry requires food, heat, cleaning, and liquid-path validation. Rib layouts must follow actual load directions.
- **Internal tension:** The compilation repeatedly calls geometries impossible by other methods, an overstatement because multipart molding, machining, forming, or assembly may be possible. It also implies that printed coffee-contact separation is sufficient without supporting thermal or hygiene evidence.

### 10. Why You Should 3D Print Your Electrical Enclosures

- **Source:** [video](https://www.youtube.com/watch?v=jNguIjkLo6g), 2024-06-22, 5:21.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:21.
- **Claims:**
  - [02:42](https://www.youtube.com/watch?v=jNguIjkLo6g&t=162s) Do not send a molded enclosure design unchanged to FDM; redesign its geometry and orientation for the additive process. **Confidence: High.**
  - [03:02](https://www.youtube.com/watch?v=jNguIjkLo6g&t=182s) Adding a chamfered corner gives a rectangular enclosure a deliberate diagonal bed face, distributing layers across the box and reducing broad cosmetic bed contact. **Confidence: High.**
  - [03:22](https://www.youtube.com/watch?v=jNguIjkLo6g&t=202s) A rear rib is proposed to stabilize the enclosure in that edge orientation during printing. **Confidence: High.**
  - [03:33](https://www.youtube.com/watch?v=jNguIjkLo6g&t=213s) Board standoffs should be widened and blended into the wall as pyramidal/chamfered masses instead of copied as thin molded posts. **Confidence: High.**
  - [04:14](https://www.youtube.com/watch?v=jNguIjkLo6g&t=254s) Required cable and mounting holes can be integrated into the printed enclosure rather than drilled into a generic purchased box afterward. **Confidence: High.**
- **Conditions/exceptions:** Enclosure geometry must still satisfy voltage spacing, flammability, ingress, heat, EMI/ESD, grounding, fastener torque, PCB access, sealing, and applicable certification. Diagonal orientation is not automatically strongest for every load, and a stabilizing rib may affect assembly or appearance.
- **Internal tension:** The video moves from the availability of UL-rated or ESD-safe feedstock to claims about a box being rated. Material recognition alone does not certify the finished enclosure, print process, thickness, or assembly.

### 11. We 3D Printed a Coffee Maker

- **Source:** [video](https://www.youtube.com/watch?v=QBg63t-Gk7s), 2024-04-25, 5:40.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:40.
- **Claims:**
  - [00:34](https://www.youtube.com/watch?v=QBg63t-Gk7s&t=34s) Printing the U-shaped stand on its back would put the narrow lower spine in an unfavorable layer/load relationship, so orientation was treated as a structural constraint from the start. **Confidence: High.**
  - [00:58](https://www.youtube.com/watch?v=QBg63t-Gk7s&t=58s) A diagonal orientation was chosen to avoid a full cosmetic side on the bed, enlarge effective fit within the build volume, and change the layer path through the spine. **Confidence: High.**
  - [01:34](https://www.youtube.com/watch?v=QBg63t-Gk7s&t=94s) The form changed from rounded to faceted/chamfered because the faceted language better matched the diagonal manufacturing strategy and reduced problematic bed artifacts. **Confidence: High.**
  - [02:37](https://www.youtube.com/watch?v=QBg63t-Gk7s&t=157s) Cropping a bulky rear volume retained the main silhouette while reducing print material. **Confidence: High.**
  - [03:11](https://www.youtube.com/watch?v=QBg63t-Gk7s&t=191s) A commodity metal filter/grate is retained as a hybrid component rather than forcing the printed body to perform every material function. **Confidence: High.**
  - [03:40](https://www.youtube.com/watch?v=QBg63t-Gk7s&t=220s) Pointed fins space the hot filter from the body and direct drips toward its outlet, combining thermal separation and liquid-path control. **Confidence: Medium** because the thermal and fluid performance is asserted rather than measured.
- **Conditions/exceptions:** This product handles hot liquid and food. Polymer temperature, creep, additives, cleaning, porosity, retained liquid, microbial risk, tip stability, filter fit, and burn risk need independent evaluation. The metal insert does not by itself make the printed assembly safe.
- **Internal tension:** The video suggests the fins make PLA suitable near hot coffee, but provides no temperature or migration data. It also calls the final product reliable without structural, thermal, or stability test evidence.

### 12. Camouflaging Electrical Enclosures

- **Source:** [video](https://www.youtube.com/watch?v=mV-FWHjlwBk), 2024-04-18, 4:07.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:07.
- **Claims:**
  - [01:43](https://www.youtube.com/watch?v=mV-FWHjlwBk&t=103s) Design the electronics interface separately from the decorative exterior to avoid rebuilding standoffs and mounting logic for every shell. **Confidence: High.**
  - [01:56](https://www.youtube.com/watch?v=mV-FWHjlwBk&t=116s) Represent the board envelope, split plane, standoffs, and mounting holes as a Boolean negative. **Confidence: High.**
  - [02:17](https://www.youtube.com/watch?v=mV-FWHjlwBk&t=137s) Subtracting that negative from a host body simultaneously creates the cavity, interface features, and separable lid/body geometry. **Confidence: High.**
  - [02:55](https://www.youtube.com/watch?v=mV-FWHjlwBk&t=175s) Reusing the same interface negative across multiple outer bodies preserves the electronics fit while enabling cosmetic variants. **Confidence: High.**
- **Conditions/exceptions:** Each host body must still be checked for minimum wall, trapped volumes, ventilation, antenna attenuation, cable routing, service access, sealing, fastener loads, assembly sequence, and print orientation. A Boolean operation can create inaccessible support or thin remnants.
- **Internal tension:** The video praises very thick walls and organic shells but does not address electronics heat dissipation, RF behavior, ingress, or maintainability. “Affordable” and production-volume claims are commercial assertions, not geometry validation.

### 13. The 3D Printed Product Urban Outfitters Sold Out 4 Times

- **Source:** [video](https://www.youtube.com/watch?v=PbGnxQifEq0), 2024-03-29, 9:00.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-09:00.
- **Claims:**
  - [00:56](https://www.youtube.com/watch?v=PbGnxQifEq0&t=56s) Establish measurable product/QC requirements before geometry and process refinement; the case study tightened a vague “3D printed” acceptance standard into repeatable cosmetic criteria. **Confidence: High.**
  - [01:29](https://www.youtube.com/watch?v=PbGnxQifEq0&t=89s) An underside cavity reduces the first layer to a perimeter-like contact region, limiting visible staining and broad-layer squish on the product bottom. **Confidence: High.**
  - [02:20](https://www.youtube.com/watch?v=PbGnxQifEq0&t=140s) An accessory fit should be designed against the distribution of mating-item sizes and states, not a single sample; the lighter varied by mold and by full/empty condition. **Confidence: High.**
  - [03:16](https://www.youtube.com/watch?v=PbGnxQifEq0&t=196s) Compliant grip fins were added inside the cavity to absorb mating-part variation while maintaining a controlled pull feel. **Confidence: High.**
  - [04:49](https://www.youtube.com/watch?v=PbGnxQifEq0&t=289s) Colorant changes material flow and dimensional response enough that a narrow-tolerance part may require cross-color process qualification. **Confidence: High.**
  - [05:19](https://www.youtube.com/watch?v=PbGnxQifEq0&t=319s) The team sought one robust production recipe coordinated with CAD rather than maintaining a fragile special recipe for each color. **Confidence: High.**
  - [06:07](https://www.youtube.com/watch?v=PbGnxQifEq0&t=367s) The speaker reports nearly 100 iterations before the file/process combination was stable across colors. **Confidence: Medium** because iteration records are not shown.
- **Conditions/exceptions:** Required insertion/pull force, fin strain, cycle life, lighter temperature, fuel exposure, wall thickness, color batches, machine population, and inspection method must be specified. The video's stated 1-2 lb pull target is product-specific and not a generic tolerance rule.
- **Internal tension:** The case study demonstrates that CAD is not independent of material color, slicer paths, and first-layer behavior. It therefore contradicts any stronger channel phrasing that a robust model is fully settings- or material-agnostic.

### 14. We Fixed the Dune Popcorn Bucket

- **Source:** [video](https://www.youtube.com/watch?v=chULpzksGSQ), 2024-03-27, 5:56.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:56.
- **Claims:**
  - [01:18](https://www.youtube.com/watch?v=chULpzksGSQ&t=78s) Product requirements and manufacturing constraints can compound into undesirable form; mold-ejection needs are presented as one driver of the original flexible, open mouth geometry. **Confidence: High.**
  - [02:51](https://www.youtube.com/watch?v=chULpzksGSQ&t=171s) Additive production permits a complex inward-facing mouth geometry without the same mold-draft/ejection constraint. **Confidence: High.**
  - [03:08](https://www.youtube.com/watch?v=chULpzksGSQ&t=188s) The revised decorative upper section is engineered to snap onto a separate bucket rather than forcing the entire food container into one printed part. **Confidence: High.**
  - [03:47](https://www.youtube.com/watch?v=chULpzksGSQ&t=227s) A licensed existing art model can supply the complex visual form, after which production engineering adds scale, attachment, and functional interface changes. **Confidence: High.**
- **Conditions/exceptions:** Licensing and attribution must be verified. A popcorn product needs food-contact, cleaning, sharp-point, entrapment, breakage, assembly-retention, and material-flammability review. The snap interface needs tolerance and cycle tests.
- **Internal tension:** The video treats tens of thousands of complex prints as straightforward but supplies no packing, cycle-time, yield, support, cleaning, or safety evidence. “Impossible” by molding is also broader than the shown comparison supports.

### 15. We Made a Better Piggy Bank

- **Source:** [video](https://www.youtube.com/watch?v=KbKeCcvn6_s), 2024-03-14, 7:28.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-07:28.
- **Claims:**
  - [03:22](https://www.youtube.com/watch?v=KbKeCcvn6_s&t=202s) Build a scaled negative containing the coin slot, storage cavity, and outlet, then reuse it to convert multiple outer animal meshes into the same functional product. **Confidence: High.**
  - [04:05](https://www.youtube.com/watch?v=KbKeCcvn6_s&t=245s) A diagonal internal shelf prevents a coin from passing directly from top slot to bottom opening while preserving a monolithic shell. **Confidence: High.**
  - [04:25](https://www.youtube.com/watch?v=KbKeCcvn6_s&t=265s) Tilting the bank makes the same internal geometry funnel stored coins toward the side/bottom outlet. **Confidence: High.**
  - [04:35](https://www.youtube.com/watch?v=KbKeCcvn6_s&t=275s) Printing the internal shelf with the body removes the separate insert and joining operation that an equivalent multipart construction would need. **Confidence: High.**
- **Conditions/exceptions:** The negative must be checked after every host-body Boolean for shell thickness, printable roofs, trapped support, coin access, drainage, sharp internal edges, choking/child safety, and retained foreign objects. Exterior meshes may require repair before Boolean use.
- **Internal tension:** This is the same piggy-bank segment reused in video 9, so it is repeated channel evidence rather than independent corroboration. Claims that the shelf is impossible by any other process overlook multipart manufacture.

### 16. We Made a Better Spoon

- **Source:** [video](https://www.youtube.com/watch?v=uCxRJxvsoe0), 2024-02-27, 4:47.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:47.
- **Claims:**
  - [00:41](https://www.youtube.com/watch?v=uCxRJxvsoe0&t=41s) A flat-backed handle gives a stable print option while the mouth-facing side remains tapered and rounded for use. **Confidence: High.**
  - [02:43](https://www.youtube.com/watch?v=uCxRJxvsoe0&t=163s) Shallow bowl surfaces show visible stair-stepping in the flat orientation; turning the spoon upright changes that surface artifact. **Confidence: High.**
  - [03:08](https://www.youtube.com/watch?v=uCxRJxvsoe0&t=188s) The upright option stands on the handle end rather than the eating edge so the bowl lip remains curved. **Confidence: High.**
  - [03:38](https://www.youtube.com/watch?v=uCxRJxvsoe0&t=218s) A detachable support comb widens the base of a tall thin spoon and can be snapped off after printing. **Confidence: High.**
  - [03:50](https://www.youtube.com/watch?v=uCxRJxvsoe0&t=230s) Multiple upright spoons can be arranged as a rack while retaining small individual bed contacts. **Confidence: High.**
- **Conditions/exceptions:** Upright printing requires adequate machine stability, collision clearance, adhesion, and comb removal without sharp remnants. A utensil also requires food-contact, bite-edge, heat, cleaning, porosity, fatigue, and breakage validation.
- **Internal tension:** A claimed minimum overhang angle at [01:08](https://www.youtube.com/watch?v=uCxRJxvsoe0&t=68s) is ambiguous in wording and profile-dependent, so it is not promoted as a rule. The claims that upright printing is cheaper and structurally adequate are not backed by comparative tests.

### 17. Massage Roller Kits

- **Source:** [video](https://www.youtube.com/watch?v=u97dyLy_FuE), 2023-08-22, 8:21.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:21.
- **Claims:**
  - [03:17](https://www.youtube.com/watch?v=u97dyLy_FuE&t=197s) The cylindrical roller is oriented so its circumference and operating rotation lie in the layer plane, avoiding a transverse split through a standing cylinder. **Confidence: High.**
  - [03:40](https://www.youtube.com/watch?v=u97dyLy_FuE&t=220s) A modeled matte/bark-like texture makes process lines less visually dominant and supports the intended product aesthetic. **Confidence: High.**
  - [04:14](https://www.youtube.com/watch?v=u97dyLy_FuE&t=254s) A commodity wood dowel supplies a stiff, replaceable handle/axle instead of printing every component. **Confidence: High.**
  - [05:24](https://www.youtube.com/watch?v=u97dyLy_FuE&t=324s) The roller uses a small chamfered bed-contact ring to reduce first-layer area and production-release problems. **Confidence: High.**
  - [05:50](https://www.youtube.com/watch?v=u97dyLy_FuE&t=350s) Chamfering the bore entrance provides a lead-in for the dowel and reduces assembly sensitivity at the edge. **Confidence: High.**
- **Conditions/exceptions:** Roller profile and stiffness require user testing for pressure/injury risk. The dowel fit needs moisture, wear, splinter, retention, and load tests. Texture depth must preserve cleanability and minimum section.
- **Internal tension:** The video calls the rollers durable and long-lived without reporting load, wear, cleaning, or user-safety results. Crowdfunding preference data would not substitute for mechanical validation.

### 18. Birdhouses

- **Source:** [video](https://www.youtube.com/watch?v=reIXSlL6mKA), 2023-08-05, 10:24.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-10:24.
- **Claims:**
  - [00:50](https://www.youtube.com/watch?v=reIXSlL6mKA&t=50s) Invert a conventional peaked birdhouse and crop the roof ridge into a narrow flat so eaves and entrance build without extensive support. **Confidence: High.**
  - [01:34](https://www.youtube.com/watch?v=reIXSlL6mKA&t=94s) A separate perch adds assembly; alternatives are a chamfered underside or a perch laid flush into the first-layer plane. **Confidence: High.**
  - [02:37](https://www.youtube.com/watch?v=reIXSlL6mKA&t=157s) Curving the rear mounting face lets a house sit against a pole or tree more closely than a flat board. **Confidence: High.**
  - [03:25](https://www.youtube.com/watch?v=reIXSlL6mKA&t=205s) An A-frame version incorporates the perch into the base layer so the part can leave the printer without support removal or perch assembly. **Confidence: High.**
  - [04:30](https://www.youtube.com/watch?v=reIXSlL6mKA&t=270s) A thick printed shell with sparse internal structure is proposed as an insulating alternative to a thin molded shell. **Confidence: Medium** because thermal performance is not measured.
  - [06:36](https://www.youtube.com/watch?v=reIXSlL6mKA&t=396s) Complex texture and an organic mounting surface can camouflage the product while also allowing a deep, thick-walled enclosure. **Confidence: High.**
- **Conditions/exceptions:** A wildlife product requires species-appropriate entrance, drainage, ventilation, clean-out access, overheating, predator protection, non-toxic material, UV/weather resistance, mounting safety, and seasonal sanitation review. Insulation must be calculated/tested, not inferred from thickness alone.
- **Internal tension:** The recommendation to use PLA outdoors with a clear UV coat at [07:33](https://www.youtube.com/watch?v=reIXSlL6mKA&t=453s) lacks heat, coating-toxicity, weathering, and animal-safety evidence. The claim that a top hole will last for years is similarly unsupported.

### 19. Design a Lamp for Mass Production 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=xEjtyA2b5I0), 2023-04-05, 18:58.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-18:58.
- **Claims:**
  - [00:20](https://www.youtube.com/watch?v=xEjtyA2b5I0&t=20s) Separate a universal lamp-base interface from variable shade styling; begin with a simple primary volume so variants share the same electrical core. **Confidence: High.**
  - [03:16](https://www.youtube.com/watch?v=xEjtyA2b5I0&t=196s) A simple open cable slot requires adhesive retention, while a hooked/re-entrant route captures the cable mechanically and removes that secondary operation. **Confidence: High.**
  - [06:16](https://www.youtube.com/watch?v=xEjtyA2b5I0&t=376s) A large conical underside recess reduces broad build-plate contact while preserving the outer mass of the base. **Confidence: High.**
  - [07:36](https://www.youtube.com/watch?v=xEjtyA2b5I0&t=456s) The hooked cable route is described as more tolerant of internal routing than a narrow straight slot. **Confidence: High.**
  - [07:57](https://www.youtube.com/watch?v=xEjtyA2b5I0&t=477s) Round cable-contact edges to avoid cutting insulation and blend locally weak transitions; this is a safety/function reason distinct from merely styling every edge. **Confidence: High.**
  - [10:12](https://www.youtube.com/watch?v=xEjtyA2b5I0&t=612s) Keeping the socket/cable features fixed while suppressing or changing outer fillet/chamfer features produces cylinder, dome, faceted, and pyramidal variants from one base model. **Confidence: High.**
- **Conditions/exceptions:** Lamp products require certified electrical components, strain relief, wire bend radius, heat/flame spacing, insulation, grounding, tip stability, cord-pull testing, shade clearance, and applicable certification. CAD capture must not damage insulation or make servicing unsafe.
- **Internal tension:** The blanket statement to “fillet everything” at [07:57](https://www.youtube.com/watch?v=xEjtyA2b5I0&t=477s) conflicts with the channel's own warning that bed-facing fillets begin horizontally. The useful rule is context-specific rounding, not universal filleting.

### 20. These Free STL's are Better than Tree Supports

- **Source:** [video](https://www.youtube.com/watch?v=YL5lYEXbLDo), 2023-02-04, 8:06.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:06.
- **Claims:**
  - [00:00](https://www.youtube.com/watch?v=YL5lYEXbLDo&t=0s) A small underside island can be missed or poorly cradled by automatic support, allowing a narrow feature to wobble before it reconnects to the body. **Confidence: High.**
  - [01:42](https://www.youtube.com/watch?v=YL5lYEXbLDo&t=102s) A designed “thumbtack” gives a narrow feature a broad supported platform connected through a small breakaway stem. **Confidence: High.**
  - [03:15](https://www.youtube.com/watch?v=YL5lYEXbLDo&t=195s) A spherical tack head can be oriented toward a side feature while maintaining a broad surface for generated support below it. **Confidence: High.**
  - [04:11](https://www.youtube.com/watch?v=YL5lYEXbLDo&t=251s) A multi-spoke/omnidirectional tack reduces precise placement effort and permits selection of a less visible break point. **Confidence: High.**
  - [05:45](https://www.youtube.com/watch?v=YL5lYEXbLDo&t=345s) A comb of narrow breakaway contacts can support a line or several small islands while limiting the supported/scarred area relative to a full interface. **Confidence: High.**
  - [06:40](https://www.youtube.com/watch?v=YL5lYEXbLDo&t=400s) The speaker explicitly says designed tacks are machine- and geometry-dependent and are not always better than ordinary supports. **Confidence: High.**
- **Conditions/exceptions:** The video's 1 mm stem was tied to a 0.4 mm nozzle example and is not a universal dimension. Stem visibility, toolpath generation, platform stability, access for cutters, scar location, break force, fragment capture, and worker handling all require validation.
- **Internal tension:** The title says the STLs are better than tree supports, while the video itself limits them to specific narrow features and admits they may be worse on some machines. They also still rely on generated support beneath their platforms.

### 21. Easiest Way to Eliminate Supports

- **Source:** [video](https://www.youtube.com/watch?v=FMs-VGAu_PQ), 2022-11-29, 4:03.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:03.
- **Claims:**
  - [00:54](https://www.youtube.com/watch?v=FMs-VGAu_PQ&t=54s) A simple fillet under a horizontal ledge still reaches a horizontal tangent at its outer end, so the earliest portion can remain support-sensitive. **Confidence: High.**
  - [01:24](https://www.youtube.com/watch?v=FMs-VGAu_PQ&t=84s) Extending and reshaping the transition so its outer tip also rounds away from horizontal can remove the discrete unsupported lip in the shown geometry. **Confidence: Medium** because the exact compound form is clearer visually than in captions.
  - [02:07](https://www.youtube.com/watch?v=FMs-VGAu_PQ&t=127s) A chamfer provides a constant underside angle between wall and ledge, making support behavior easier to predict than a continuously changing fillet. **Confidence: High.**
  - [02:28](https://www.youtube.com/watch?v=FMs-VGAu_PQ&t=148s) Choose the chamfer slope around geometry and process capacity rather than assuming every projection accepts a standard angle. **Confidence: High.**
- **Conditions/exceptions:** Supported angle depends on layer height, extrusion width, material, cooling, speed, curvature, bridge length, and surface requirement. The video's numerical angle commentary is ambiguous in “steep/shallow” terminology and is not promoted as a portable limit.
- **Internal tension:** The closing claim that chamfers are always better than fillets conflicts with later channel examples where vertical fillets improve stress and toolpaths. It applies only to the specific underside transition being demonstrated.

### 22. 3D Printed Parts as Strong As Molded

- **Source:** [video](https://www.youtube.com/watch?v=p-GuXDxQYkA), 2022-11-08, 5:35.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:35.
- **Claims:**
  - [01:23](https://www.youtube.com/watch?v=p-GuXDxQYkA&t=83s) Directly printing a thin ribbed molded design can put its expected bending failure across layer interfaces and create a stress concentration. **Confidence: High.**
  - [02:52](https://www.youtube.com/watch?v=p-GuXDxQYkA&t=172s) For the shown compression/bending case, redistribute the same material into a broad rounded section rather than preserving molding-driven thin webs. **Confidence: High.**
  - [03:27](https://www.youtube.com/watch?v=p-GuXDxQYkA&t=207s) Moving material farther from the center of bending and smoothing the outer load path is presented as reducing local layer stress while raising section stiffness. **Confidence: Medium** because the model is not analyzed quantitatively.
  - [04:17](https://www.youtube.com/watch?v=p-GuXDxQYkA&t=257s) The comparison intentionally equalizes modeled material mass, illustrating that distribution—not merely adding mass—can improve a direction-specific printed section. **Confidence: Medium** because equal CAD mass does not prove equal strength.
  - [04:30](https://www.youtube.com/watch?v=p-GuXDxQYkA&t=270s) A hollow outer section with infill can be treated as a shell/core structure, but its behavior must be designed rather than copied from a solid molded part. **Confidence: High.**
- **Conditions/exceptions:** Strength depends on load direction, material, interlayer bonding, shell count, infill, defects, temperature, fatigue, notch geometry, and safety factor. Same mass or moment of inertia does not establish equivalent strength, toughness, or life.
- **Internal tension:** The title and narration suggest molded-equivalent or better strength, but no physical test or finite-element result is supplied. The defensible claim is geometry redistribution for a specified load case, not general strength equivalence.

### 23. The Power of Diagonals

- **Source:** [video](https://www.youtube.com/watch?v=8TIhkxQNINY), 2022-10-15, 5:46.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:46.
- **Claims:**
  - [00:47](https://www.youtube.com/watch?v=8TIhkxQNINY&t=47s) Placing an enclosure's display face on the bed removes internal support but risks bed artifacts, corner warp, and difficult automatic release on a customer-facing surface. **Confidence: High.**
  - [01:36](https://www.youtube.com/watch?v=8TIhkxQNINY&t=96s) Standing the box on an unmodified edge protects broad visible faces but creates unsupported internal roofs around the opening. **Confidence: High.**
  - [02:26](https://www.youtube.com/watch?v=8TIhkxQNINY&t=146s) Rotating a square-section enclosure onto a corner converts its horizontal roofs into diagonal layer progressions that the shown profile slices without support. **Confidence: High for the shown geometry/profile.**
  - [03:18](https://www.youtube.com/watch?v=8TIhkxQNINY&t=198s) Add small matching corner chamfers so the chosen diagonal orientation has a deliberate flat contact rather than balancing on a sharp vertex. **Confidence: High.**
  - [04:16](https://www.youtube.com/watch?v=8TIhkxQNINY&t=256s) Keeping that contact small and away from the principal visible faces localizes bed texture and can aid release. **Confidence: High.**
- **Conditions/exceptions:** Diagonal printing increases height, may reduce stability, changes seam and load direction, and may need a fin/raft depending on printer kinematics. Internal spans, apertures, corner radius, material, cooling, and profile still require slice/print validation.
- **Internal tension:** The claim that bed-slinger printers cannot make the part is an unsupported absolute; feasibility depends on acceleration, bed adhesion, height, stabilizers, and machine tuning. “45 degrees means no support” is also geometry/profile-specific.

### 24. Design for 3D Printing: Grip Fins

- **Source:** [video](https://www.youtube.com/watch?v=yzg_NXM-NRs), 2022-06-25, 5:21.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:21.
- **Claims:**
  - [01:30](https://www.youtube.com/watch?v=yzg_NXM-NRs&t=90s) Replace a fully rigid interference wall with discrete spring fins that flex to absorb variation while maintaining contact force. **Confidence: High.**
  - [01:37](https://www.youtube.com/watch?v=yzg_NXM-NRs&t=97s) Orient each fin's bending plane within the layer plane instead of asking the fin to split across layers. **Confidence: High.**
  - [02:20](https://www.youtube.com/watch?v=yzg_NXM-NRs&t=140s) Keep a fin free at its tip and rear clearance; accidentally merging it into the roof of the hole removes the intended compliance. **Confidence: High.**
  - [03:02](https://www.youtube.com/watch?v=yzg_NXM-NRs&t=182s) Start fins above the first-layer plane with a chamfered lead-in so the thin spring roots are not distorted as isolated first-layer details. **Confidence: High.**
  - [03:31](https://www.youtube.com/watch?v=yzg_NXM-NRs&t=211s) The same lead-in centers the mating part before it begins deflecting the fins. **Confidence: High.**
  - [03:56](https://www.youtube.com/watch?v=yzg_NXM-NRs&t=236s) Fin thickness and free length tune compliance, but longer fins can add slop/buckling and thinner fins can reduce fatigue life. **Confidence: High.**
  - [04:18](https://www.youtube.com/watch?v=yzg_NXM-NRs&t=258s) Material choice changes usable fin strain; the video favors PETG/ABS over more brittle PLA for repeated flexing. **Confidence: Medium** because no material/cycle data is shown.
- **Conditions/exceptions:** Fin count, strain, root radius, contact pressure, insertion force, wear, temperature, creep, removal cycles, debris, and mating-surface variation must be tested. The captioned generic tolerance numbers are inconsistent and are not retained as rules.
- **Internal tension:** The video says fins can “always” fit and flex indefinitely before immediately limiting them by fatigue, material, and cycle count. Compliance expands the fit window; it does not guarantee every tolerance or lifetime.

### 25. Best Design Tips for 3D Printing Production

- **Source:** [video](https://www.youtube.com/watch?v=NaQ_Sa1BaqU), 2022-05-09, 6:30.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-06:30.
- **Claims:**
  - [00:31](https://www.youtube.com/watch?v=NaQ_Sa1BaqU&t=31s) Rounding vertical path corners can reduce abrupt direction changes and visible vibration artifacts compared with a sharp 90-degree turn. **Confidence: High.**
  - [01:09](https://www.youtube.com/watch?v=NaQ_Sa1BaqU&t=69s) Rounding a top-to-side transition can distribute the layer transition and local stress rather than terminating a flat roof at a sharp wall. **Confidence: Medium** because the strength benefit is asserted without testing.
  - [02:00](https://www.youtube.com/watch?v=NaQ_Sa1BaqU&t=120s) For some FDM parts, a thick simple outer envelope with sparse interior can take less toolpath/time than thin shells plus many ribs because the latter add perimeter surface. **Confidence: Medium** and geometry/profile-dependent.
  - [03:35](https://www.youtube.com/watch?v=NaQ_Sa1BaqU&t=215s) Transition a projection gradually with a chamfer or suitable curve so each layer remains supported and support-removal labor is avoided. **Confidence: High.**
  - [04:43](https://www.youtube.com/watch?v=NaQ_Sa1BaqU&t=283s) Light colors reveal nozzle residue, staining, and other cosmetic defects more readily, so color choice affects achievable yield and QC criteria. **Confidence: High.**
- **Conditions/exceptions:** Edge rounding must respect orientation: a bed-facing horizontal fillet can worsen overhangs. Envelope efficiency depends on wall count, infill, dimensions, buckling, loads, and print profile. Color does not change allowable defect severity; it changes visibility and possibly material behavior.
- **Internal tension:** “Always fillet everything” and “do not remove material” are overbroad and conflict with other channel guidance on chamfers, minimized bed contact, pockets, and material reduction. The I-beam analogy also conflicts with dismissing all ribbed sections; section design must follow loads and toolpaths.

## Validation summary

- Manifest entries: **25**.
- Video sections: **25**.
- Complete-caption access statements: **25/25**.
- Timestamped extracted claim bullets: **139**.
- Timestamped official-video links (including contradiction/context links): **144**; metadata/duration validation errors: **0**.
- Videos with inaccessible primary-caption evidence: **0**.
- Unique batch-06 source IDs: **25**.
- Overlap with batch-01/batch-02/batch-04 source files: **0**.
- Overlap with assigned batch-03 and batch-05 ID lists: **0**.
- Every extracted claim includes a timestamped official-video link and confidence label.
- Every video section records conditions/exceptions and an internal contradiction/tension assessment.
- Unsupported or ambiguous numeric heuristics promoted as universal guidance: **0**.
- Independent corroboration performed: **none**.
