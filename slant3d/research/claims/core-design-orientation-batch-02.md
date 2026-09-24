# Slant 3D claim extraction: core design and orientation, batch 02

- **Research date:** 2026-09-24
- **Scope:** the next 25 high-signal, definite-relevance videos not covered in batch 01, selected from `relevant-video-candidates-2026-09-24.md`.
- **Purpose:** capture what Slant 3D actually says about CAD geometry, orientation, supports, fits, mechanisms, strength, tolerances, and production preparation.
- **Not done here:** independent engineering corroboration, endorsement, or conversion of the claims into skill rules.

## Method and evidence limits

For every video below, the complete official YouTube English automatic-caption track (`en-orig`) was read from the first caption event through the end of the video. Official YouTube metadata supplied the title, publication date, duration, and URL. Caption files were used transiently and are not reproduced in this document.

Claims are paraphrased rather than quoted. Each claim links to the point in the official video where it is stated. “Confidence” means confidence that the paraphrase accurately reflects the accessible video evidence, **not** confidence that the engineering claim is true.

Confidence scale:

- **High:** clear spoken claim with an unambiguous timestamp.
- **Medium:** clear general claim whose scope depends on the shown geometry, process, or material.
- **Low:** important numerical or causal claim is ambiguous or internally inconsistent in the accessible caption evidence.

The following evidence was inaccessible or deliberately excluded:

- No manually authored English caption track was published for these 25 videos; only official YouTube automatic captions were accessible.
- Fine on-screen CAD dimensions, labels, test-gauge readings, and geometry details that were not spoken are not captured here.
- Audio was not separately human-audited. Ambiguous automatic-caption numbers and unit conversions were not promoted into rules.
- Comments, descriptions, linked downloads, sponsor/service pages, and third-party sources were not used as engineering evidence.
- No video in this batch was inaccessible; all 25 had full-length automatic-caption coverage.

## Batch manifest

| # | Video | Date | Duration | Primary topics |
|---:|---|---:|---:|---|
| 1 | [We Made a Better LEGO (For 3D Printing)](https://www.youtube.com/watch?v=7SY4Vd8Gb80) | 2026-08-07 | 17:26 | friction fit, compliant studs, molded-to-FDM redesign |
| 2 | [We Made a Knob for SmarterEveryDay to Print Millions](https://www.youtube.com/watch?v=F3ViXSLH_ZM) | 2026-07-31 | 12:50 | part consolidation, inserts, captive nuts, first layer |
| 3 | [Stop Gluing Magnets Into Your 3D Prints](https://www.youtube.com/watch?v=BwUzOJ8B_H0) | 2026-07-17 | 12:04 | magnet retention, creep, assembly, polarity |
| 4 | [How to Design Text for Mass Production 3D Printing](https://www.youtube.com/watch?v=upf9ixYtDG4) | 2026-04-10 | 18:13 | text placement, feature resolution, contrast, multicolor |
| 5 | [We Redesigned This Viral 3D Printed Koozie](https://www.youtube.com/watch?v=cbtVDk3R6XI) | 2026-01-30 | 9:35 | layer-aware flexures, part consolidation, fatigue |
| 6 | [We Redesigned This YouTuber’s Product — Evariste](https://www.youtube.com/watch?v=vkMYsbhfVbg) | 2026-01-23 | 11:02 | uniform orientation, connectors, support fins |
| 7 | [Design Unbreakable Pins with Perfect Tolerances](https://www.youtube.com/watch?v=uMA-Wt-z_BU) | 2025-08-15 | 7:30 | vertical pins, lead-ins, compliant fits, reinforcement |
| 8 | [The Easiest Way to Instantly 10x Your Print Quality](https://www.youtube.com/watch?v=scv4am8kbqs) | 2025-07-04 | 4:37 | texture, color/material, cosmetic robustness |
| 9 | [How a Pro Designs a Cube for 3D Printing](https://www.youtube.com/watch?v=3VUQd_Tl5x0) | 2025-06-21 | 5:49 | diagonal orientation, edge treatment, support fins |
| 10 | [Learn 15 Print-in-Place Mechanisms in 15 Minutes](https://www.youtube.com/watch?v=AAKsl8zW-Ds) | 2025-05-03 | 17:21 | living hinges, springs, print-in-place axles, orientation |
| 11 | [Stop Needing Slicers](https://www.youtube.com/watch?v=vWKBcGFmX3Y) | 2025-04-26 | 14:29 | CAD-encoded support/strength, warp, texture, tolerance |
| 12 | [Top 4 Springs You Can Design with 3D Printing](https://www.youtube.com/watch?v=wpriGP45Unw) | 2024-10-22 | 7:11 | flat springs, leaf springs, spirals, layer direction |
| 13 | [Design Perfect Scoops for Mass Production 3D Printing](https://www.youtube.com/watch?v=aih9ctXS0uU) | 2024-09-03 | 8:15 | orientation, chamfers, support-free handles |
| 14 | [Reinforce Your Side Loops for Durable 3D Printed Parts](https://www.youtube.com/watch?v=m1HG1nBTD0E) | 2024-08-10 | 2:44 | loops, pullout, ribs, fillets |
| 15 | [Designing a Tape Dispenser for Mass Production 3D Printing](https://www.youtube.com/watch?v=B6r8m93MNGQ) | 2024-01-13 | 6:05 | orientation, designed supports, texture, consolidation |
| 16 | [From 10% to 100%: Infill Compression Strength](https://www.youtube.com/watch?v=-LHQtlxYQII) | 2023-10-17 | 7:40 | compression test, infill density, failure modes |
| 17 | [3D Printing Basics: Understanding and Managing Support Material](https://www.youtube.com/watch?v=WYQbxIVLz6Y) | 2023-06-23 | 7:52 | support avoidance, chamfers, designed support |
| 18 | [Design Stronger 3D Printed Handles for Mass Production 3D Printing](https://www.youtube.com/watch?v=lae6pyQQhrs) | 2023-06-21 | 5:16 | handle orientation, screw reinforcement, texture |
| 19 | [Cavities Don't Help: Design for Mass Production 3D Printing](https://www.youtube.com/watch?v=AURCtaRrUGM) | 2023-06-15 | 6:43 | cavities, surface area, hidden reinforcement |
| 20 | [CAD vs Slicer. What to rely on when mass producing a part with 3D Printing.](https://www.youtube.com/watch?v=rszX16LFW3U) | 2023-05-10 | 3:13 | CAD authority, slicer portability, handoff |
| 21 | [5 Living Hinges for Mass Production 3D Printing](https://www.youtube.com/watch?v=TiEyFle6lTM) | 2023-04-26 | 6:05 | living hinges, flexure distribution, axle orientation |
| 22 | [Stop Tall Prints From Falling Over](https://www.youtube.com/watch?v=3Acks3Wzjjo) | 2023-04-04 | 3:55 | tall thin parts, support combs, witness marks |
| 23 | [Design Custom Electrical Enclosures for Mass Production 3D Printing](https://www.youtube.com/watch?v=9ERY20MRJPo) | 2023-03-31 | 11:59 | standoffs, ribs, PCB seats, enclosure orientation |
| 24 | [Stop Using Brims, Do This Instead](https://www.youtube.com/watch?v=MCcFMDv_4eo) | 2023-01-14 | 4:32 | warping, mouse ears, CAD brims, post-processing |
| 25 | [How to Design 3D Printed Parts for Auto Ejection](https://www.youtube.com/watch?v=SZwXREFoWKA) | 2022-10-22 | 6:52 | bed contact, ejection, underside pockets |

## Extracted claims

### 1. We Made a Better LEGO (For 3D Printing)

- **Source:** [video](https://www.youtube.com/watch?v=7SY4Vd8Gb80), 2026-08-07, 17:26.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-17:26.
- **Claims:**
  - [02:03](https://www.youtube.com/watch?v=7SY4Vd8Gb80&t=123s) The molded brick uses small internal ribs to localize its friction-fit contact instead of pressing an entire wall against the studs. **Confidence: High.**
  - [03:32](https://www.youtube.com/watch?v=7SY4Vd8Gb80&t=212s) Localized ribs are said to wear and comply more consistently than a broad flat contact, while a center rib shortens the unsupported wall span and evens the grip across studs. **Confidence: Medium** because the force equalization is explained, not experimentally shown.
  - [06:24](https://www.youtube.com/watch?v=7SY4Vd8Gb80&t=384s) A direct FDM copy of the molded geometry is rejected: the video adds a bottom chamfer, rounds vertical edges, and removes very fine molded ribs that exceed the intended process tolerance. **Confidence: High.**
  - [07:34](https://www.youtube.com/watch?v=7SY4Vd8Gb80&t=454s) Because printed stud and layer ridges can bind, the redesign combines studs into larger teardrop forms and adds compliant grip fins whose travel absorbs dimensional variation. **Confidence: High.**
  - [09:13](https://www.youtube.com/watch?v=7SY4Vd8Gb80&t=553s) The fins are relieved underneath so they can flex; the body around their roots must provide enough interlayer area to resist the constant spring load. **Confidence: High.**
- **Conditions/exceptions:** The redesign changes the classic stud geometry and depends on compliant-fin material behavior, root strength, and available space. Compatibility and durability claims are shown as a design demonstration, not a controlled lifecycle test.
- **Internal tension:** The video says the compliant interface will not wear out ([10:05](https://www.youtube.com/watch?v=7SY4Vd8Gb80&t=605s)), despite earlier explaining that polymer contacts wear and without addressing long-term creep or fatigue.

### 2. We Made a Knob for SmarterEveryDay to Print Millions

- **Source:** [video](https://www.youtube.com/watch?v=F3ViXSLH_ZM), 2026-07-31, 12:50.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-12:50.
- **Claims:**
  - [01:13](https://www.youtube.com/watch?v=F3ViXSLH_ZM&t=73s) Injection-molded knobs use thin walls and open cavities to control shrink; the FDM redesign instead uses an enclosed, infill-supported volume. **Confidence: High.**
  - [03:10](https://www.youtube.com/watch?v=F3ViXSLH_ZM&t=190s) For its upside-down print orientation, the knob receives a bottom-edge chamfer to isolate first-layer expansion, and optional surface texture to make finish variation less visible. **Confidence: High.**
  - [04:37](https://www.youtube.com/watch?v=F3ViXSLH_ZM&t=277s) Printed plastic threads are considered vulnerable to stripping/wear in this heavy-use knob, so the video recommends a metal insert for this application. **Confidence: High.**
  - [05:02](https://www.youtube.com/watch?v=F3ViXSLH_ZM&t=302s) Pausing the print to embed hardware is rejected for production because it idles the machine; heat-set inserts or post-print side-loaded hardware preserve continuous printing. **Confidence: High.**
  - [06:31](https://www.youtube.com/watch?v=F3ViXSLH_ZM&t=391s) A side slot can capture a commodity hex nut, with a small interference feature retaining it after insertion. **Confidence: High.**
- **Conditions/exceptions:** The split-body captive-nut option adds assembly and is explicitly said to be excessive for a simple knob ([07:28](https://www.youtube.com/watch?v=F3ViXSLH_ZM&t=448s)). Insert choice depends on load, tooling, supply, access, and desired exterior appearance.
- **Internal contradictions:** None material observed. The later production-rate/economic claims are outside this geometry extraction and were not treated as design rules.

### 3. Stop Gluing Magnets Into Your 3D Prints

- **Source:** [video](https://www.youtube.com/watch?v=BwUzOJ8B_H0), 2026-07-17, 12:04.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-12:04.
- **Claims:**
  - [00:40](https://www.youtube.com/watch?v=BwUzOJ8B_H0&t=40s) Glue adds contamination and workmanship risk; a simple rigid press fit can also loosen because the surrounding polymer may creep under sustained interference. **Confidence: High.**
  - [01:32](https://www.youtube.com/watch?v=BwUzOJ8B_H0&t=92s) A long cylindrical magnet provides more sidewall engagement and a lead-in for pressing than a thin disc, trading easier retention for potentially higher component cost. **Confidence: High.**
  - [02:25](https://www.youtube.com/watch?v=BwUzOJ8B_H0&t=145s) Pausing a printer to encapsulate a magnet is presented as a production bottleneck and can interact badly with ferrous toolhead parts; post-print side insertion avoids the pause. **Confidence: High.**
  - [04:04](https://www.youtube.com/watch?v=BwUzOJ8B_H0&t=244s) An over-center side slot lets a disc pop past a retaining lip into an unstressed cavity, preserving exposed metal contact without depending on continuous radial interference. **Confidence: High.**
  - [08:24](https://www.youtube.com/watch?v=BwUzOJ8B_H0&t=504s) A spherical magnet in a larger retained cavity can rotate to align its poles; pairing one magnet with a steel ball or screw head can remove mating-polarity assembly errors. **Confidence: High.**
- **Conditions/exceptions:** A covered side slot introduces a plastic gap that weakens and changes the feel of the magnetic closure ([03:04](https://www.youtube.com/watch?v=BwUzOJ8B_H0&t=184s)). Exposed opposing magnets may need angular offset to avoid collision ([04:53](https://www.youtube.com/watch?v=BwUzOJ8B_H0&t=293s)). Press-fit retention still depends on magnet geometry, material, cavity accuracy, and tooling.
- **Internal tension:** The video repeatedly says over-center magnets will “never” escape ([07:08](https://www.youtube.com/watch?v=BwUzOJ8B_H0&t=428s)); no pullout, impact, thermal, or lifecycle evidence is presented to justify the absolute.

### 4. How to Design Text for Mass Production 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=upf9ixYtDG4), 2026-04-10, 18:13.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-18:13.
- **Claims:**
  - [02:16](https://www.youtube.com/watch?v=upf9ixYtDG4&t=136s) Text must be designed relative to the extrusion tool and layer height; the demonstration uses a common nozzle/layer setup and warns against strokes thinner than the process can resolve. **Confidence: High.**
  - [03:52](https://www.youtube.com/watch?v=upf9ixYtDG4&t=232s) Top-surface text is considered highly sensitive to flow, material, and isolated islands; if unavoidable, the video favors large block lettering and engraving over many raised islands. **Confidence: High.**
  - [06:35](https://www.youtube.com/watch?v=upf9ixYtDG4&t=395s) Bottom text complicates the first layer and can hide a failure until the print finishes; keep the first layer simple and avoid deep pockets or disconnected letter islands. **Confidence: High.**
  - [10:40](https://www.youtube.com/watch?v=upf9ixYtDG4&t=640s) Sidewall text is preferred because vertical resolution follows layer height; shallow engraving avoids the sag and overhangs caused by strongly raised lettering. **Confidence: High.**
  - [15:41](https://www.youtube.com/watch?v=upf9ixYtDG4&t=941s) For production color contrast, the video suggests textured recesses or a separately printed text plate/insert instead of forcing the entire body through a multi-material process. **Confidence: High.**
- **Conditions/exceptions:** Visibility depends on color, lighting, material, font, tool width, and layer height. The spoken numerical depths and minimum text sizes are examples for the stated setup, not validated universal limits.
- **Internal tension:** Text is described as effectively free ([00:19](https://www.youtube.com/watch?v=upf9ixYtDG4&t=19s)), but the video later acknowledges extra tool motion, islands, rejection risk, and substantial multi-color cost. “Free” therefore means no separate marking operation when geometry remains manufacturable.

### 5. We Redesigned This Viral 3D Printed Koozie

- **Source:** [video](https://www.youtube.com/watch?v=cbtVDk3R6XI), 2026-01-30, 9:35.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-09:35.
- **Claims:**
  - [01:21](https://www.youtube.com/watch?v=cbtVDk3R6XI&t=81s) Three separately printed body pieces create production/assembly coordination that the redesign removes by consolidating the body into one print. **Confidence: High.**
  - [02:26](https://www.youtube.com/watch?v=cbtVDk3R6XI&t=146s) The original retaining tabs flex across layer interfaces; the surrounding ring and curved tab length limit their strain but do not eliminate fatigue. **Confidence: High.**
  - [03:42](https://www.youtube.com/watch?v=cbtVDk3R6XI&t=222s) The redesign turns the flexures so bending occurs within the layer plane and gives the fins a shared supported base. **Confidence: High.**
  - [04:45](https://www.youtube.com/watch?v=cbtVDk3R6XI&t=285s) Fin stiffness can then be tuned geometrically while keeping the feature support-free and avoiding separate post-processing. **Confidence: Medium** because the relationship is demonstrated qualitatively, not measured.
  - [06:01](https://www.youtube.com/watch?v=cbtVDk3R6XI&t=361s) Retaining the tube as printed geometry supports size variants and integrated markings without changing a stock-tube supply and assembly process. **Confidence: High.**
- **Conditions/exceptions:** The benefit assumes a material with adequate cyclic behavior, roots sized for the load, and a build orientation matching the shown flex direction. Part consolidation can lengthen a print and turn a local defect into a whole-part reject; the video does not quantify that tradeoff.
- **Internal tension:** The speaker first says the original tabs will eventually fail, then says the redesigned fins will last “forever” ([07:34](https://www.youtube.com/watch?v=cbtVDk3R6XI&t=454s)); the same segment also concedes life remains limited by the material.

### 6. We Redesigned This YouTuber’s Product — Evariste

- **Source:** [video](https://www.youtube.com/watch?v=vkMYsbhfVbg), 2026-01-23, 11:02.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-11:02.
- **Claims:**
  - [00:17](https://www.youtube.com/watch?v=vkMYsbhfVbg&t=17s) The original marble-run pieces combine steep overhangs, small hooks, and material-sensitive surface artifacts, producing inconsistent fit and appearance. **Confidence: High.**
  - [02:50](https://www.youtube.com/watch?v=vkMYsbhfVbg&t=170s) Giving different pieces different bed orientations made their visible layer texture inconsistent, motivating a common side/slanted orientation for the family. **Confidence: High.**
  - [04:07](https://www.youtube.com/watch?v=vkMYsbhfVbg&t=247s) Isolated hook geometry is replaced by a blended connector region because adding supporting material costs less than reprinting a failed part. **Confidence: High.**
  - [05:31](https://www.youtube.com/watch?v=vkMYsbhfVbg&t=331s) Small compressible loops and mating catches achieved the required removable snap after rigid tongue/slot attempts proved either too strong or too weak. **Confidence: High.**
  - [06:23](https://www.youtube.com/watch?v=vkMYsbhfVbg&t=383s) Chamfering the lower connector edges and adding sacrificial, interwoven support fins enabled the chosen slanted orientation without slicer-generated supports. **Confidence: High.**
- **Conditions/exceptions:** The solution is specific to mirrored, child-operable, repeatedly detachable track pieces. The support fins leave break-off witnesses and still require manual removal. Material change from PETG to PLA is an application-specific recommendation, not a universal preference.
- **Internal tension:** The video describes the result as needing “zero support” ([08:19](https://www.youtube.com/watch?v=vkMYsbhfVbg&t=499s)) while also showing CAD-designed sacrificial support fins; the intended meaning is zero slicer-generated support.

### 7. Design Unbreakable Pins with Perfect Tolerances

- **Source:** [video](https://www.youtube.com/watch?v=uMA-Wt-z_BU), 2025-08-15, 7:30.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-07:30.
- **Claims:**
  - [00:34](https://www.youtube.com/watch?v=uMA-Wt-z_BU&t=34s) Add a lead-in to the receiving hole, clearance around the pin, a rounded pin tip, and a fillet at the pin root instead of mating two sharp equal-size cylinders. **Confidence: High.**
  - [02:18](https://www.youtube.com/watch?v=uMA-Wt-z_BU&t=138s) Make a pin only as long as required because excess height increases its lever arm and root stress. **Confidence: High.**
  - [02:54](https://www.youtube.com/watch?v=uMA-Wt-z_BU&t=174s) A cross-shaped pin puts more printed material along principal bending directions than a thin circular shell and can also provide compliant contact. **Confidence: Medium** because strength depends on load direction and slicing.
  - [03:48](https://www.youtube.com/watch?v=uMA-Wt-z_BU&t=228s) A shallow taper lets the tip enter with generous clearance and brings the interface into contact progressively rather than demanding one exact diameter everywhere. **Confidence: High.**
  - [05:18](https://www.youtube.com/watch?v=uMA-Wt-z_BU&t=318s) Corrugating the pin perimeter and using hidden microfeatures is proposed to provoke extra perimeters and make the pin locally near-solid without raising global infill. **Confidence: Medium** because the result is slicer dependent.
- **Conditions/exceptions:** The spoken clearance examples vary with material shrink and machine accuracy and must not be treated as universal. A cross or corrugated pin changes contact area and may not suit sealing, bearing, or precision-locating functions.
- **Internal tension:** The title and conclusion promise “perfect” fit across any material and settings ([06:13](https://www.youtube.com/watch?v=uMA-Wt-z_BU&t=373s)), while the video earlier says clearance must be tuned for shrink ([00:57](https://www.youtube.com/watch?v=uMA-Wt-z_BU&t=57s)).

### 8. The Easiest Way to Instantly 10x Your Print Quality

- **Source:** [video](https://www.youtube.com/watch?v=scv4am8kbqs), 2025-07-04, 4:37.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:37.
- **Claims:**
  - [00:23](https://www.youtube.com/watch?v=scv4am8kbqs&t=23s) Cosmetic robustness depends on both geometry and material; broad glossy planar faces expose shrink, infill telegraphing, seams, fingerprints, and other process variation. **Confidence: High.**
  - [01:47](https://www.youtube.com/watch?v=scv4am8kbqs&t=107s) A modeled or process-applied texture breaks up a broad reflection and masks small surface artifacts while creating a more deliberate tactile finish. **Confidence: High.**
  - [02:14](https://www.youtube.com/watch?v=scv4am8kbqs&t=134s) Textures may be modeled in CAD, applied by a mesh-texturing tool, or generated by a slicer; the video treats these as alternatives with different portability/control. **Confidence: High.**
  - [02:48](https://www.youtube.com/watch?v=scv4am8kbqs&t=168s) Matte material can improve perceived finish, but the video warns that the demonstrated matte formulation sacrifices strength relative to glossy material. **Confidence: Medium** because this is formulation dependent.
- **Conditions/exceptions:** The color/material observations are not universal to every polymer or formulation. Texture may alter dimensions, friction, cleanability, print time, and mating surfaces; none are evaluated here.
- **Internal tension:** The title promises a tenfold quality improvement, but no quality metric or controlled comparison is supplied. The useful evidence is the qualitative masking/finish rationale, not the multiplier.

### 9. How a Pro Designs a Cube for 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=3VUQd_Tl5x0), 2025-06-21, 5:49.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:49.
- **Claims:**
  - [00:39](https://www.youtube.com/watch?v=3VUQd_Tl5x0&t=39s) Round vertical edges to soften abrupt nozzle-direction changes, and chamfer the bottom edge to protect the nominal cube from first-layer expansion. **Confidence: High.**
  - [02:08](https://www.youtube.com/watch?v=3VUQd_Tl5x0&t=128s) To make all major faces share a more similar finish, the advanced example rotates the cube onto a chamfered diagonal instead of placing one full face on the bed. **Confidence: High.**
  - [02:51](https://www.youtube.com/watch?v=3VUQd_Tl5x0&t=171s) CAD-designed fins are merged to the cube so it is rigidly located during the diagonal print; ordinary removable support is said to leave the part less precisely constrained. **Confidence: High.**
  - [03:26](https://www.youtube.com/watch?v=3VUQd_Tl5x0&t=206s) Move sacrificial connections away from tactile outer corners and onto faces where their witness marks can be cut flush or visually hidden. **Confidence: High.**
  - [04:49](https://www.youtube.com/watch?v=3VUQd_Tl5x0&t=289s) A subtle exterior noise texture is used to mask both layer direction and support-removal witnesses. **Confidence: High.**
- **Conditions/exceptions:** Diagonal printing reduces bed contact and therefore needs stabilization. Designed support creates a removal step and witness marks; it is not automatically preferable when a bed face is acceptable.
- **Internal contradictions:** None material observed. The term “perfect cube” is aesthetic/production rhetoric rather than a metrology result.

### 10. Learn 15 Print-in-Place Mechanisms in 15 Minutes

- **Source:** [video](https://www.youtube.com/watch?v=AAKsl8zW-Ds), 2025-05-03, 17:21.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-17:21. This is a multi-topic compilation whose chapters substantially overlap earlier mechanism videos.
- **Claims:**
  - [00:20](https://www.youtube.com/watch?v=AAKsl8zW-Ds&t=20s) A thin living hinge concentrates cyclic strain and eventually wears; flexible materials and printing the hinge on its side can make it workable, but fatigue remains a design constraint. **Confidence: High.**
  - [01:14](https://www.youtube.com/watch?v=AAKsl8zW-Ds&t=74s) Circular or grooved flexures distribute motion over a larger path, exchanging compactness/range for lower strain at any one location and an inherent spring return. **Confidence: High.**
  - [03:50](https://www.youtube.com/watch?v=AAKsl8zW-Ds&t=230s) A print-in-place hinge around a captured axle avoids assembly; vertical printing improves axle roundness/motion while horizontal printing improves load path through the layers but can make the axle rougher/oval. **Confidence: High.**
  - [06:17](https://www.youtube.com/watch?v=AAKsl8zW-Ds&t=377s) Flat patterned springs should use rounded turns to reduce stress concentration; stiffness is tuned by path geometry, thickness, and the amount of flexing material. **Confidence: High.**
  - [12:01](https://www.youtube.com/watch?v=AAKsl8zW-Ds&t=721s) For pin-and-loop hinges, place the central pin within the layer plane when strength is primary; conical captured pivots provide alternatives for vertical part orientations. **Confidence: High.**
- **Conditions/exceptions:** Mechanism choice depends on travel, force, fatigue life, package space, desired smoothness, material, clearance, and print orientation. The count/title is a rapid catalogue, not validation of service life.
- **Internal tension:** The video calls living hinges poor engineering because they wear, while also presenting several useful printed living-hinge variants. The resolved position is conditional use, not a blanket prohibition.

### 11. Stop Needing Slicers

- **Source:** [video](https://www.youtube.com/watch?v=vWKBcGFmX3Y), 2025-04-26, 14:29.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-14:29.
- **Claims:**
  - [02:12](https://www.youtube.com/watch?v=vWKBcGFmX3Y&t=132s) For outsourced production, avoid autogenerated support where possible; remove overhangs, change orientation, fill unnecessary cavities, or encode only necessary support in CAD. **Confidence: High.**
  - [03:50](https://www.youtube.com/watch?v=vWKBcGFmX3Y&t=230s) Encode local reinforcement with geometry/microfeatures and enlarge the load-bearing envelope instead of relying on a special global infill or wall profile. **Confidence: High.**
  - [05:44](https://www.youtube.com/watch?v=vWKBcGFmX3Y&t=344s) Round vertical exterior corners to reduce abrupt direction-change artifacts, and chamfer first-layer edges to decouple the nominal outline from initial-layer spread. **Confidence: High.**
  - [07:26](https://www.youtube.com/watch?v=vWKBcGFmX3Y&t=446s) Place removable CAD mouse ears at warp-prone corners, or design a brim/raft into complex arrays, so adhesion intent travels with the model. **Confidence: High.**
  - [11:01](https://www.youtube.com/watch?v=vWKBcGFmX3Y&t=661s) Give mating parts as much clearance as function allows, then use compliant fins, wedges, threads, or progressive chamfers to create a tight perceived fit without depending on one exact gap. **Confidence: High.**
- **Conditions/exceptions:** The examples still depend on ordinary slicer interpretation, material shrink, layer height, and extrusion width. Numerical brim/raft and texture examples are setup-specific and were not promoted into universal values.
- **Internal tension:** The promise that any machine/material/settings can reproduce the part ([00:08](https://www.youtube.com/watch?v=vWKBcGFmX3Y&t=8s)) is stronger than the mechanisms described; the practical principle is reduced sensitivity, not process independence.

### 12. Top 4 Springs You Can Design with 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=wpriGP45Unw), 2024-10-22, 7:11.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-07:11.
- **Claims:**
  - [00:17](https://www.youtube.com/watch?v=wpriGP45Unw&t=17s) A conventional helical coil is discouraged because vertical printing loads layer interfaces and sideways printing no longer produces the same continuous coil behavior. **Confidence: High.**
  - [00:47](https://www.youtube.com/watch?v=wpriGP45Unw&t=47s) For extension behavior, the video flattens the spring path into a planar repeating curve so it can be printed as continuous in-plane geometry. **Confidence: High.**
  - [01:11](https://www.youtube.com/watch?v=wpriGP45Unw&t=71s) Round every turn in a patterned spring; square internal corners concentrate stress at the points expected to flex. **Confidence: High.**
  - [03:32](https://www.youtube.com/watch?v=wpriGP45Unw&t=212s) Leaf springs can guide translation and damp motion, but their response is sensitive to band thickness and should be oriented so working stress stays in the printed plane. **Confidence: High.**
  - [05:07](https://www.youtube.com/watch?v=wpriGP45Unw&t=307s) Planar spiral springs compactly store rotational energy; thickness, number/length of turns, and out-of-plane depth tune their response. **Confidence: High.**
- **Conditions/exceptions:** Printed springs are material- and fatigue-sensitive and are not asserted to match metal springs. The one spoken minimum thickness is an example, not a portable design rule.
- **Internal tension:** The narration alternates between “coil” and “spiral” for the final planar spring, which could be confused with the helical coil rejected at the start. Geometry, not terminology, resolves the distinction.

### 13. Design Perfect Scoops for Mass Production 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=aih9ctXS0uU), 2024-09-03, 8:15.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:15.
- **Claims:**
  - [00:40](https://www.youtube.com/watch?v=aih9ctXS0uU&t=40s) A molded-style scoop printed bowl-down leaves its raised handle unsupported; simply copying that geometry produces rough support interfaces and waste. **Confidence: High.**
  - [01:27](https://www.youtube.com/watch?v=aih9ctXS0uU&t=87s) When printing the scoop inverted, a domed fillet still approaches horizontal at its crown; a straight chamfer produces a consistently supported staircase. **Confidence: High.**
  - [03:35](https://www.youtube.com/watch?v=aih9ctXS0uU&t=215s) A print-native alternative keeps the bowl upright and moves the handle to the bottom/bed side, eliminating support and also keeping the user’s hand farther from the contents. **Confidence: High.**
  - [04:52](https://www.youtube.com/watch?v=aih9ctXS0uU&t=292s) If a high handle is ergonomically required, extend it down as a broad slab or chamfered rise so every layer is supported rather than suspending a thin bar. **Confidence: High.**
  - [05:42](https://www.youtube.com/watch?v=aih9ctXS0uU&t=342s) Minimize unnecessary bed contact by trimming the handle footprint and growing it upward with a chamfer, reducing first-layer exposure while retaining support-free geometry. **Confidence: High.**
- **Conditions/exceptions:** Internal volume must be preserved if the bottom profile changes. Food-contact safety, cleaning, material certification, dimensional accuracy, and wear are not evaluated.
- **Internal contradictions:** None material observed. The repeated fixed chamfer-size recommendation is presented categorically but remains process- and geometry-dependent.

### 14. Reinforce Your Side Loops for Durable 3D Printed Parts

- **Source:** [video](https://www.youtube.com/watch?v=m1HG1nBTD0E), 2024-08-10, 2:44.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-02:44.
- **Claims:**
  - [00:08](https://www.youtube.com/watch?v=m1HG1nBTD0E&t=8s) A thin wire-like side loop presents little material across the pullout path and can snap under force or impact. **Confidence: High.**
  - [00:38](https://www.youtube.com/watch?v=m1HG1nBTD0E&t=38s) Replace the wire form with a broad side plate containing a hole, using as much surrounding material as the product envelope permits. **Confidence: High.**
  - [01:06](https://www.youtube.com/watch?v=m1HG1nBTD0E&t=66s) Add an exterior rib or T-like flange along the likely pullout path to place material at the stress concentration. **Confidence: High.**
  - [01:31](https://www.youtube.com/watch?v=m1HG1nBTD0E&t=91s) Angle upward-facing transitions, fillet roots, and enlarge the attachment region so reinforcement does not create new support-demanding overhangs. **Confidence: High.**
- **Conditions/exceptions:** Reinforcement direction must follow the actual load path, and thickening may conflict with clearance, flexibility, mass, or appearance. The video offers no load tests or sizing equations.
- **Internal contradictions:** None material observed.

### 15. Designing a Tape Dispenser for Mass Production 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=B6r8m93MNGQ), 2024-01-13, 6:05.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-06:05.
- **Claims:**
  - [00:56](https://www.youtube.com/watch?v=B6r8m93MNGQ&t=56s) Angling the body creates the functional cutting edge and allows the serrations to be modeled as a simpler straight extrusion while visually indicating the action point. **Confidence: High.**
  - [01:43](https://www.youtube.com/watch?v=B6r8m93MNGQ&t=103s) Chamfer exterior/bed edges and consolidate the housing so the dispenser prints as one body rather than multiple shells, ballast, and an attached blade. **Confidence: High.**
  - [02:14](https://www.youtube.com/watch?v=B6r8m93MNGQ&t=134s) The demonstrated body is printed upside down so the bed forms the sharp serrated face; internal channels are built into the same print. **Confidence: High.**
  - [03:49](https://www.youtube.com/watch?v=B6r8m93MNGQ&t=229s) The spool is printed horizontally for spoke strength, with one side cropped flat to create a bed surface without changing its rotational function. **Confidence: High.**
  - [04:31](https://www.youtube.com/watch?v=B6r8m93MNGQ&t=271s) Small pointed CAD towers support only the necessary overhangs and are designed for simple snap-off/tumbling rather than broad slicer support. **Confidence: High.**
- **Conditions/exceptions:** Bed-formed cutting teeth depend on bed condition and first-layer control. The roller’s flat is acceptable only because its mating geometry tolerates it. Higher infill is deliberately used for mass/heft, so this is not a minimum-material example.
- **Internal tension:** The body is described as having no assembly, but the separate roller still has to be installed. The narrower claim is substantial part-count reduction.

### 16. From 10% to 100%: Infill Compression Strength

- **Source:** [video](https://www.youtube.com/watch?v=-LHQtlxYQII), 2023-10-17, 7:40.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-07:40.
- **Claims:**
  - [00:14](https://www.youtube.com/watch?v=-LHQtlxYQII&t=14s) The demonstration compresses equal-size PLA cubes with one grid-infill pattern/orientation while increasing nominal infill in fixed steps. **Confidence: High.**
  - [01:04](https://www.youtube.com/watch?v=-LHQtlxYQII&t=64s) Low-density specimens first buckle and crush their internal grid; denser specimens carry more load before a sudden diagonal or catastrophic failure. **Confidence: High.**
  - [04:07](https://www.youtube.com/watch?v=-LHQtlxYQII&t=247s) The test instrument reaches its measurement ceiling before the higher-density sequence is fully characterized, so the upper specimens cannot be quantitatively ranked from the shown gauge. **Confidence: High.**
  - [05:34](https://www.youtube.com/watch?v=-LHQtlxYQII&t=334s) The fully solid specimen is described as crushing more like bulk plastic, rather than following the same grid-buckling failure path. **Confidence: High.**
- **Conditions/exceptions:** Results apply to the shown cube, PLA formulation, grid pattern, print orientation, wall setup, and compression direction. The video does not report replicate counts, scatter, mass-normalized performance, or uncertainty. Automatic captions disagree with themselves about some force values and conversions, so no numeric strength rule is extracted.
- **Internal tension:** The speaker says strength rises dramatically at high infill ([06:14](https://www.youtube.com/watch?v=-LHQtlxYQII&t=374s)) but also concludes there is little practical difference beyond a high threshold ([07:05](https://www.youtube.com/watch?v=-LHQtlxYQII&t=425s)); the saturated gauge cannot resolve that claim.

### 17. 3D Printing Basics: Understanding and Managing Support Material

- **Source:** [video](https://www.youtube.com/watch?v=WYQbxIVLz6Y), 2023-06-23, 7:52.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-07:52.
- **Claims:**
  - [00:12](https://www.youtube.com/watch?v=WYQbxIVLz6Y&t=12s) Support increases material, rejection, and post-processing, especially when a human must remove it; production design should first try to eliminate it. **Confidence: High.**
  - [02:25](https://www.youtube.com/watch?v=WYQbxIVLz6Y&t=145s) A fillet can shorten a bridge but eventually becomes horizontal, so a long underside transition may still need support. **Confidence: High.**
  - [03:17](https://www.youtube.com/watch?v=WYQbxIVLz6Y&t=197s) A chamfer keeps a constant buildable slope and is preferred when it satisfies the function and appearance. **Confidence: High.**
  - [04:31](https://www.youtube.com/watch?v=WYQbxIVLz6Y&t=271s) If the cavity has no functional purpose, fill it and let sparse infill occupy the interior rather than creating extra exterior surfaces and support. **Confidence: High.**
  - [05:24](https://www.youtube.com/watch?v=WYQbxIVLz6Y&t=324s) When support is unavoidable, put minimal hollow/pointed supports at known locations in CAD so placement and break-off behavior travel with the model. **Confidence: High.**
- **Conditions/exceptions:** Chamfers change internal/external volume and may not meet every functional profile. Designed supports still require removal and must be sized for the tool/material; the video explicitly treats no support as the ideal.
- **Internal contradictions:** None material observed. The fixed-angle language is simplified and should not be read as a universal overhang limit.

### 18. Design Stronger 3D Printed Handles for Mass Production 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=lae6pyQQhrs), 2023-06-21, 5:16.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:16.
- **Claims:**
  - [00:52](https://www.youtube.com/watch?v=lae6pyQQhrs&t=52s) A handle copied from bent/stamped material does not automatically have suitable FDM load paths; the process should determine the attachment geometry. **Confidence: High.**
  - [01:11](https://www.youtube.com/watch?v=lae6pyQQhrs&t=71s) Chamfered ribs around screw holes add material without creating support-heavy undersides, and rounded outer edges improve touch. **Confidence: High.**
  - [01:54](https://www.youtube.com/watch?v=lae6pyQQhrs&t=114s) Print the bar on its side so its primary tensile/bending load runs along the layer paths rather than peeling stacked layers apart. **Confidence: High.**
  - [02:09](https://www.youtube.com/watch?v=lae6pyQQhrs&t=129s) Instead of retaining molded-style voids and ribs, fill the volume around countersunk fasteners to create a broad monolithic load-transfer region. **Confidence: High.**
  - [03:04](https://www.youtube.com/watch?v=lae6pyQQhrs&t=184s) Texture on the grip surface can increase friction and visual differentiation without requiring a secondary grip component. **Confidence: High.**
- **Conditions/exceptions:** The shown hanging demonstration is not a standardized strength test. Fastener size, countersink depth, anisotropy, creep, torque, and substrate capacity still govern the real assembly.
- **Internal tension:** The video frames ribs as both an acceptable first solution and an obsolete molding-era form. Its final preference is filled volume where packaging permits, not that ribs never work.

### 19. Cavities Don't Help: Design for Mass Production 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=AURCtaRrUGM), 2023-06-15, 6:43.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-06:43.
- **Claims:**
  - [00:47](https://www.youtube.com/watch?v=AURCtaRrUGM&t=47s) Visible cavities inherited from molding can increase FDM toolpath surface/perimeter length rather than save material; a closed envelope with sparse infill may be cheaper and stronger. **Confidence: High.**
  - [01:52](https://www.youtube.com/watch?v=AURCtaRrUGM&t=112s) Additional exposed internal surfaces create more opportunities for stringing, cosmetic defects, and rejection, whereas hidden infill errors do not affect the exterior. **Confidence: High.**
  - [03:20](https://www.youtube.com/watch?v=AURCtaRrUGM&t=200s) Internal cavities/microgeometry can be useful when intentionally provoking denser perimeters in a local structural zone. **Confidence: High.**
  - [04:13](https://www.youtube.com/watch?v=AURCtaRrUGM&t=253s) Keep those reinforcement cavities enclosed by an exterior skin so they do not collect debris, disrupt the first layer, or expose stringing. **Confidence: High.**
  - [05:23](https://www.youtube.com/watch?v=AURCtaRrUGM&t=323s) The recommendation is to use cavities as internal structural controls, not as a reflexive visual/material-removal device. **Confidence: High.**
- **Conditions/exceptions:** Functional flow paths, weight targets, acoustics, ventilation, drainage, access, heat transfer, or true hollow-shell requirements can justify cavities. Whether a cavity saves material/time depends on slicer paths and geometry.
- **Internal tension:** The title says cavities do not help, while the latter half recommends hidden cavities for local reinforcement. The actual rule is purpose-dependent use.

### 20. CAD vs Slicer. What to rely on when mass producing a part with 3D Printing.

- **Source:** [video](https://www.youtube.com/watch?v=rszX16LFW3U), 2023-05-10, 3:13.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-03:13.
- **Claims:**
  - [00:23](https://www.youtube.com/watch?v=rszX16LFW3U&t=23s) Put product-defining features in CAD wherever practical so the designer, not a particular manufacturing profile, controls intent. **Confidence: High.**
  - [00:49](https://www.youtube.com/watch?v=rszX16LFW3U&t=49s) The video distinguishes design authority from process planning: the manufacturer still slices and adjusts tool motion, analogous to a toolmaker translating a part into tooling. **Confidence: High.**
  - [01:23](https://www.youtube.com/watch?v=rszX16LFW3U&t=83s) Candidate CAD-owned features include texture, adhesion aids, assisting geometry, and—where feasible—support placement. **Confidence: High.**
  - [02:03](https://www.youtube.com/watch?v=rszX16LFW3U&t=123s) Reducing dependence on local slicer modifiers makes a model easier to upload, re-manufacture, and revise without recreating a hidden recipe. **Confidence: High.**
- **Conditions/exceptions:** The video does not argue that slicers are unnecessary; machine-safe speeds, extrusion, temperatures, and other process settings remain manufacturing responsibilities. CAD-encoded microfeatures can themselves depend on slicer behavior.
- **Internal tension:** “Everything possible” in CAD is an ownership principle, not literal slicer agnosticism; the narration acknowledges the manufacturer must change slicing/tool motion ([00:51](https://www.youtube.com/watch?v=rszX16LFW3U&t=51s)).

### 21. 5 Living Hinges for Mass Production 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=TiEyFle6lTM), 2023-04-26, 6:05.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-06:05.
- **Claims:**
  - [00:22](https://www.youtube.com/watch?v=TiEyFle6lTM&t=22s) A thin conventional living hinge concentrates cyclic strain and has limited travel/life; flexible materials and side orientation can make it usable but do not remove fatigue. **Confidence: High.**
  - [01:16](https://www.youtube.com/watch?v=TiEyFle6lTM&t=76s) A circular flexure spreads deformation over a larger region and provides a spring return, at the cost of protrusion and reduced range. **Confidence: High.**
  - [02:20](https://www.youtube.com/watch?v=TiEyFle6lTM&t=140s) Repeating small spring segments or woodworking-style slats distributes the total rotation so no single ligament must bend as far. **Confidence: High.**
  - [03:48](https://www.youtube.com/watch?v=TiEyFle6lTM&t=228s) A captured print-in-place axle replaces material flex with relative rotation and removes assembly hardware. **Confidence: High.**
  - [04:10](https://www.youtube.com/watch?v=TiEyFle6lTM&t=250s) Vertical axle orientation improves roundness and smooth motion but places torsional load across layers; horizontal orientation strengthens the axle through the layer plane but can produce rougher/oval motion. **Confidence: High.**
- **Conditions/exceptions:** Hinge choice must follow required angle, cycle life, load, space, cost, material, and allowable rejection. A print-in-place hinge requires sufficient clearance and overhang control around the captive interface.
- **Internal tension:** The speaker calls living hinges fundamentally poor engineering, yet describes several legitimate applications. This is a warning about fatigue concentration, not a categorical ban.

### 22. Stop Tall Prints From Falling Over

- **Source:** [video](https://www.youtube.com/watch?v=3Acks3Wzjjo), 2023-04-04, 3:55.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-03:55.
- **Claims:**
  - [00:00](https://www.youtube.com/watch?v=3Acks3Wzjjo&t=0s) Tall, thin parts can wobble and show Z-banding, especially when the bed moves, while ordinary support needs a separation gap and may not stabilize a vertical plate. **Confidence: High.**
  - [00:38](https://www.youtube.com/watch?v=3Acks3Wzjjo&t=38s) A support comb consists of a wide-base vertical post and small horizontal fingers merged into the target at selected heights. **Confidence: High.**
  - [01:23](https://www.youtube.com/watch?v=3Acks3Wzjjo&t=83s) Position the comb close to the part, contour its fingers against the surface, then overlap them slightly so they become deliberate sacrificial connections rather than free gaps. **Confidence: High.**
  - [02:35](https://www.youtube.com/watch?v=3Acks3Wzjjo&t=155s) After printing, clip the fingers; the method trades a few controlled witness marks for improved stability and a preferred upright surface orientation. **Confidence: High.**
- **Conditions/exceptions:** Finger/post sizes are examples for the demonstrated process, not universal minima. The comb adds material, print time, removal labor, and surface witnesses; reorientation or a stiffer machine may be preferable.
- **Internal tension:** The closing describes the comb as working “without support” ([03:20](https://www.youtube.com/watch?v=3Acks3Wzjjo&t=200s)), though it is itself sacrificial designed support. The intended contrast is slicer support versus CAD-designed stabilizers.

### 23. Design Custom Electrical Enclosures for Mass Production 3D Printing

- **Source:** [video](https://www.youtube.com/watch?v=9ERY20MRJPo), 2023-03-31, 11:59.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-11:59.
- **Claims:**
  - [01:06](https://www.youtube.com/watch?v=9ERY20MRJPo&t=66s) Make PCB standoffs as broad as component/solder clearance allows so technician torque does not act on a thin isolated post. **Confidence: High.**
  - [02:04](https://www.youtube.com/watch?v=9ERY20MRJPo&t=124s) Blend standoff roots with chamfers rather than underside fillets so the reinforcement remains support-free in more enclosure orientations. **Confidence: High.**
  - [03:15](https://www.youtube.com/watch?v=9ERY20MRJPo&t=195s) Ribs can connect standoffs to the floor or wall, but they should expose enough surface/load path and use chamfered transitions rather than unsupported roofs. **Confidence: High.**
  - [06:06](https://www.youtube.com/watch?v=9ERY20MRJPo&t=366s) An alternative is a broad custom PCB seat with reliefs for solder leads, which supports the board and acts as a locating feature without fragile individual posts. **Confidence: High.**
  - [08:22](https://www.youtube.com/watch?v=9ERY20MRJPo&t=502s) Minimize customer-visible bed faces and large bed contact by placing the enclosure on a symmetric chamfered edge; orient ribs/standoffs so they build upward without generated support. **Confidence: High.**
- **Conditions/exceptions:** PCB keep-outs, lead heights, connector access, heat, electrical clearance, ESD/fire requirements, insert selection, and service access must control the geometry. A full PCB seat requires a thicker wall and more customization.
- **Internal tension:** Early narration says chamfered standoffs permit any orientation ([02:20](https://www.youtube.com/watch?v=9ERY20MRJPo&t=140s)), while the slicing section shows orientation remains crucial for ribs, center of gravity, bed contact, and visible finish.

### 24. Stop Using Brims, Do This Instead

- **Source:** [video](https://www.youtube.com/watch?v=MCcFMDv_4eo), 2023-01-14, 4:32.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:32.
- **Claims:**
  - [00:18](https://www.youtube.com/watch?v=MCcFMDv_4eo&t=18s) Sharp first-layer corners can be dragged by the nozzle or lift under shrink stress; the risk grows with dense or high-warp parts. **Confidence: High.**
  - [01:04](https://www.youtube.com/watch?v=MCcFMDv_4eo&t=64s) A full slicer brim treats the entire perimeter and therefore adds more removal/cleanup than is needed when only a few corners are vulnerable. **Confidence: High.**
  - [01:41](https://www.youtube.com/watch?v=MCcFMDv_4eo&t=101s) CAD mouse ears place round adhesion pads only at sharp corners, reducing both corner drag and local peel stress. **Confidence: High.**
  - [02:42](https://www.youtube.com/watch?v=MCcFMDv_4eo&t=162s) Connect the pad through a narrow sacrificial sprue so it can be clipped at one controlled point rather than trimmed around two corner edges. **Confidence: High.**
  - [03:02](https://www.youtube.com/watch?v=MCcFMDv_4eo&t=182s) Keep the pad close to the corner because a long thin connector can stretch and allow the part to lift despite the adhered pad. **Confidence: High.**
- **Conditions/exceptions:** Pad thickness and size must match layer height, material shrink, and expected force. A full brim may still be appropriate for broad edge lifting, and any ear/sprue adds post-processing.
- **Internal contradictions:** None material observed. The title is categorical, but the narration acknowledges conventional brims can work ([01:12](https://www.youtube.com/watch?v=MCcFMDv_4eo&t=72s)).

### 25. How to Design 3D Printed Parts for Auto Ejection

- **Source:** [video](https://www.youtube.com/watch?v=SZwXREFoWKA), 2022-10-22, 6:52.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-06:52.
- **Claims:**
  - [00:39](https://www.youtube.com/watch?v=SZwXREFoWKA&t=39s) A broad flat first layer adheres well but can resist automated removal; auto-ejection design should reduce bed-contact area while preserving stability. **Confidence: High.**
  - [01:15](https://www.youtube.com/watch?v=SZwXREFoWKA&t=75s) A large exterior chamfer can reduce contact but may distort the product appearance and introduce steep early overhangs, so it is not the preferred universal solution. **Confidence: High.**
  - [01:51](https://www.youtube.com/watch?v=SZwXREFoWKA&t=111s) A shallow underside inset turns the initial face into a perimeter ring, making release easier while leaving the exterior silhouette unchanged. **Confidence: High.**
  - [03:45](https://www.youtube.com/watch?v=SZwXREFoWKA&t=225s) Extending the inset into a smoothly domed underside creates an intentional-looking cavity that grows without internal support and avoids a visibly mismatched single-layer patch. **Confidence: High.**
  - [05:38](https://www.youtube.com/watch?v=SZwXREFoWKA&t=338s) The dome transitions from a small contact ring into the full body, reducing adhesion without adding a separate ejection feature or post-process. **Confidence: High.**
- **Conditions/exceptions:** Ejection depends on bed material, release method, part temperature, material, center of mass, contact width, and machine mechanics. Reducing contact too far can cause adhesion failure during printing; underside cavities may be unacceptable for sealing, cleaning, or flatness.
- **Internal tension:** The video says the dome can be bridged without support while also describing it as a gradual dome; actual behavior depends on radius, layer height, extrusion, and material, none of which are bounded.

## Validation summary

- Manifest entries: **25**.
- Video sections: **25**.
- Full-caption access statements: **25/25**.
- Videos with inaccessible primary caption evidence: **0**.
- Every extracted claim includes a timestamped official-video link.
- Every section records conditions/exceptions and internal contradiction, tension, or an explicit “none observed” statement.
- Numerical rules from ambiguous captions: **0 promoted**. Setup-specific numbers were either omitted, described only as examples, or explicitly caveated.
- Independent corroboration performed: **none**.
