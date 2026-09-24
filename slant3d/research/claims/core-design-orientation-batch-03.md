# Slant 3D claim extraction: core design and orientation, batch 03

- **Research date:** 2026-09-24
- **Scope:** 25 additional high-signal, definite-relevance videos selected from `relevant-video-candidates-2026-09-24.md` after excluding every video in batch 01 and the 25 supplied batch-02 IDs.
- **Selection preference:** focused design tutorials with reusable CAD, orientation, support, fit, mechanism, and production-preparation guidance were prioritized over podcasts, compilations, and broad product showcases.
- **Purpose:** preserve what Slant 3D actually says before reconciling it with independent engineering sources.
- **Not done here:** endorsement, independent validation, or automatic conversion of these claims into skill rules.

## Method and evidence limits

For every video below, the complete official YouTube English automatic-caption track (`en-orig`) was read from its first caption event through its final caption event. Official YouTube metadata supplied the title, publication date, duration, and URL. Caption files were used transiently and are not reproduced in this document.

Claims are paraphrased. Each claim links to the point where the spoken explanation begins. “Confidence” measures confidence that the paraphrase accurately represents the accessible video evidence; it does **not** measure whether the engineering claim is correct.

- **High:** clear spoken claim with an unambiguous timestamp.
- **Medium:** clear general claim whose useful scope depends on geometry, process, material, or unshown tests.
- **Low:** a numerical or causal claim is important but ambiguous or not adequately supported in the accessible evidence.

Evidence cautions:

- No manually authored English captions were published for these 25 videos; only official automatic captions were accessible.
- Fine on-screen dimensions, CAD labels, test results, and geometry not spoken aloud are outside this extraction.
- Audio was not separately human-audited. Ambiguous decimals and units in automatic captions were not promoted into numerical rules.
- Sponsor/service claims, cost claims, and claims of universality were not treated as engineering validation.
- No video in this batch was inaccessible; all 25 had caption coverage from 00:00 to within the final seconds of the listed duration.

## Batch manifest

| # | Video | Date | Duration | Primary topics |
|---:|---|---:|---:|---|
| 1 | [6 Rafts You Have Never Seen! \| Design for Additive Manufacturing](https://www.youtube.com/watch?v=4LTkVb6rP84) | 2026-06-12 | 15:44 | CAD rafts, adhesion, kits, inspection |
| 2 | [Holes That Won't Break \| Design for 3D Printing](https://www.youtube.com/watch?v=UfJIMn4nvsA) | 2025-10-27 | 6:11 | side holes, local reinforcement, microfeatures |
| 3 | [Hacking the IKEA SKADIS Pegboard \| Design for 3D Printing](https://www.youtube.com/watch?v=EoIlALcMJB8) | 2025-10-18 | 10:58 | hooks, orientation, designed support, compliant mounts |
| 4 | [Design Compliant Lids for Perfect Tolerance Every Time \| Design for 3D Printing: Lids: Vol. 2](https://www.youtube.com/watch?v=IZKh6lo9SP4) | 2025-08-28 | 6:17 | compliant fits, grip fins, internal latches |
| 5 | [10 Ways to Hide Layer Lines \| Design 3D Printed Textures](https://www.youtube.com/watch?v=pUabxkiJAdE) | 2025-07-18 | 8:19 | texture, file complexity, grip, appearance |
| 6 | [STOP Filling Your Build Plate \| Design for 3D Printing](https://www.youtube.com/watch?v=ZpmiK0aY9VM) | 2025-05-09 | 8:46 | batching, CAD rafts, inspection, labeling |
| 7 | [3D Print Better Fan Blades Without Wasting Filament \| Design for 3D Printing](https://www.youtube.com/watch?v=SWOnmWCi6bY) | 2025-03-22 | 4:11 | fan orientation, designed support, outer rings |
| 8 | [How-to Design Print in Place Hinges \| Design for Mass Production 3D Printing](https://www.youtube.com/watch?v=BWsUk1xSSn4) | 2025-02-08 | 8:22 | living hinges, pin axes, cone hinges, orientation |
| 9 | [We 3D Printed a Screwdriver Case for Linus Tech Tips \| LTT Precision Multi-bit Screwdriver](https://www.youtube.com/watch?v=-Ryo2uWkC4I) | 2024-12-14 | 10:16 | enclosure orientation, print-in-place hinge, retention |
| 10 | [Design Stronger Vase Mode Prints Using This Secret Technique \| 3D Printed Blocks](https://www.youtube.com/watch?v=mHRQkreuuDA) | 2024-11-23 | 8:11 | vase-mode geometry, folds, continuous paths, safety |
| 11 | [This Box Keeps Out Water Without a Seal \| Design for Mass Production 3D Printing](https://www.youtube.com/watch?v=prMUfQ9y7Rk) | 2024-11-19 | 4:29 | drainage labyrinth, enclosure geometry |
| 12 | [Water-Resistant Vents for Industrial Applications \| Design for Mass Production 3D Printing](https://www.youtube.com/watch?v=bO39lWkaspA) | 2024-11-02 | 9:55 | offset slats, drainage, orientation, ribs |
| 13 | [We Made Tinker Toys for Adults \| 3D Printed Extrusion Brackets](https://www.youtube.com/watch?v=csUGcIPNNkk) | 2024-10-31 | 8:06 | diagonal orientation, clamps, horizontal screws |
| 14 | [STOP Using Brims. CAD is So Much Better \| Stop Using Slicer Settings](https://www.youtube.com/watch?v=4GxZXxNraY0) | 2024-09-14 | 9:47 | CAD brims, first-layer paths, mouse ears |
| 15 | [Stable Feet Designs for Your 3D Printed Products](https://www.youtube.com/watch?v=hSP9CkqhZSQ) | 2024-09-07 | 5:04 | feet, overhangs, side orientation, inserts |
| 16 | [Design Rafts in CAD \| Stop Using Slicer Settings](https://www.youtube.com/watch?v=7KVh19WpOcc) | 2024-08-17 | 8:03 | CAD rafts, breakaway ties, warp paths |
| 17 | [You're Designing Parts Too Thin \| Designing for Mass Production 3D Printing](https://www.youtube.com/watch?v=as84ZBjdmxU) | 2024-08-01 | 4:13 | thick shells, blended joints, hollow structures |
| 18 | [Types of Lids \| Design for Mass Production 3D Printing](https://www.youtube.com/watch?v=7YAylxQFe3k) | 2024-07-13 | 5:50 | friction lids, threads, quarter-turn lids |
| 19 | [Print in Place Latch Mechanism \| Design for Mass Production 3D Printing](https://www.youtube.com/watch?v=4wRKmcWXEkw) | 2024-07-02 | 7:09 | print-in-place latch, spring direction, designed support |
| 20 | [Mounted Enclosure Boxes \| Design for Mass Production 3D Printing](https://www.youtube.com/watch?v=lGnpz8q4STw) | 2024-06-27 | 4:59 | enclosure orientation, straps, rail mounts, lugs |
| 21 | [3x Part Strength Without Slicer Settings \| Design for Mass Production 3D Printing](https://www.youtube.com/watch?v=Lq-SoGgKOcQ) | 2024-05-25 | 4:06 | hidden microfeatures, perimeter induction, test claim |
| 22 | [Stop Snapping Your Snap Fits \| Design for Mass Production 3D Printing](https://www.youtube.com/watch?v=_y8Yvu1FQIE) | 2024-05-16 | 5:05 | snap orientation, overhang treatment, support |
| 23 | [Secrets to Better 3D Printed Domes \| Design for Mass Production 3D Printing](https://www.youtube.com/watch?v=udEeJjzEQZI) | 2024-04-23 | 4:17 | dome interiors, overhangs, designed support |
| 24 | [Connect 3D Printed Parts \| Design for Mass Production 3D Printing](https://www.youtube.com/watch?v=djm5tCFn9S0) | 2024-03-19 | 4:30 | pegs, slots, clips, joining |
| 25 | [Simplify Assembly with Glue Slots \| Design for Mass Production 3D Printing](https://www.youtube.com/watch?v=qV1xXXbzM4Y) | 2024-03-02 | 4:03 | adhesive keys, relief volume, glue channels |

## Extracted claims

### 1. 6 Rafts You Have Never Seen!

- **Source:** [video](https://www.youtube.com/watch?v=4LTkVb6rP84), 2026-06-12, 15:44.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-15:40.
- **Claims:**
  - [00:23](https://www.youtube.com/watch?v=4LTkVb6rP84&t=23s) A modeled raft must balance enough rigidity to resist bowing with enough separation to peel away without damaging the part. **Confidence: High.**
  - [01:15](https://www.youtube.com/watch?v=4LTkVb6rP84&t=75s) Round a raft's outer corners to reduce peel-up points; tune the part-to-raft gap rather than treating one clearance as universal. **Confidence: High.**
  - [03:09](https://www.youtube.com/watch?v=4LTkVb6rP84&t=189s) Removing most central contact and retaining contact near the perimeter can hold warp-prone edges while making the raft easier to peel. **Confidence: High.**
  - [06:06](https://www.youtube.com/watch?v=4LTkVb6rP84&t=366s) Small sacrificial ties at critical corners can physically connect the model to the raft when a pure air gap is unreliable. **Confidence: High.**
  - [09:46](https://www.youtube.com/watch?v=4LTkVb6rP84&t=586s) A shared raft can act like a sprue card for a kit, retaining small companion parts beside the main component. **Confidence: High.**
  - [12:29](https://www.youtube.com/watch?v=4LTkVb6rP84&t=749s) Labels and part outlines modeled into the raft can communicate assembly order and reveal a missing item during inspection. **Confidence: High.**
- **Conditions/exceptions:** The underside finish is explicitly described as a tradeoff; raft clearance, tie size, and raft thickness depend on material, layer height, and desired removal force. The video's numerical gaps and “universal” nozzle/material claims require external validation and are not adopted here.
- **Internal tension:** The presentation calls the modeled raft universally portable, while repeatedly advising clearance experiments for material-dependent adhesion.

### 2. Holes That Won't Break

- **Source:** [video](https://www.youtube.com/watch?v=UfJIMn4nvsA), 2025-10-27, 6:11.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-06:12.
- **Claims:**
  - [00:42](https://www.youtube.com/watch?v=UfJIMn4nvsA&t=42s) For a wall-mounted part whose holes tend to split between layers, the video frames increased interlayer contact area around the hole as the main design objective. **Confidence: High.**
  - [00:51](https://www.youtube.com/watch?v=UfJIMn4nvsA&t=51s) A modeled thread can add local path length/material around a hole, but its pointed profile can also introduce stress concentrations. **Confidence: High.**
  - [01:47](https://www.youtube.com/watch?v=UfJIMn4nvsA&t=107s) Local rings, bosses, or directional struts can reinforce the hole without thickening the entire part. **Confidence: High.**
  - [03:26](https://www.youtube.com/watch?v=UfJIMn4nvsA&t=206s) Thin hidden annular cuts are proposed to make ordinary slicing generate additional perimeters around the hole. **Confidence: High.**
  - [04:13](https://www.youtube.com/watch?v=UfJIMn4nvsA&t=253s) The hidden cuts should run with the intended layers rather than perforate the whole region into a detachable sleeve. **Confidence: Medium** because behavior depends on mesh repair and perimeter generation.
- **Conditions/exceptions:** Exact cut width and count are process dependent. Local reinforcement does not replace orienting the load path or checking fastener torque, bearing stress, and base-material creep.
- **Internal tension:** Threads are introduced as reinforcement and immediately acknowledged as possible crack initiators; the useful rule is local path/material control, not “always add threads.”

### 3. Hacking the IKEA SKADIS Pegboard

- **Source:** [video](https://www.youtube.com/watch?v=EoIlALcMJB8), 2025-10-18, 10:58.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-10:59.
- **Claims:**
  - [00:36](https://www.youtube.com/watch?v=EoIlALcMJB8&t=36s) Printing a hook sideways places it in the layer plane, but creates support and tolerance problems under the hook. **Confidence: High.**
  - [01:12](https://www.youtube.com/watch?v=EoIlALcMJB8&t=72s) A designed support can be placed only where the hook needs it and connected so a long support cannot topple independently. **Confidence: High.**
  - [02:10](https://www.youtube.com/watch?v=EoIlALcMJB8&t=130s) Moving hooks flush with a print face removes their underside support requirement; shortening the engagement lip can also reduce leverage and breakage. **Confidence: High.**
  - [04:55](https://www.youtube.com/watch?v=EoIlALcMJB8&t=295s) A chamfered compliant snap can replace the traditional hook and grow without a horizontal underside. **Confidence: High.**
  - [06:23](https://www.youtube.com/watch?v=EoIlALcMJB8&t=383s) A single-loop snap with a root extending into an internal relief cavity gains flexural length and distributes strain better than a short exposed tab. **Confidence: High.**
- **Conditions/exceptions:** Thin compliant overhangs remain sensitive to material, color, cooling, and feature thickness. The video offers a metal hook as the alternative when plastic strength is insufficient.
- **Internal tension:** The video makes categorical durability claims for the loop while also warning that its very thin overhanging section may sag; both geometry and process must be checked.

### 4. Design Compliant Lids for Perfect Tolerance Every Time

- **Source:** [video](https://www.youtube.com/watch?v=IZKh6lo9SP4), 2025-08-28, 6:17.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-06:16.
- **Claims:**
  - [01:07](https://www.youtube.com/watch?v=IZKh6lo9SP4&t=67s) Reduce continuous wall-to-wall contact with reliefs or discrete contact nubs so layer ridges and shrink variation do not bind across the full perimeter. **Confidence: High.**
  - [01:50](https://www.youtube.com/watch?v=IZKh6lo9SP4&t=110s) Put compliant side springs in the build plane so they flex within layers rather than opening a layer interface. **Confidence: High.**
  - [02:54](https://www.youtube.com/watch?v=IZKh6lo9SP4&t=174s) Grip fins can make the relaxed lid larger than the opening while using fin compliance to accommodate dimensional variation. **Confidence: High.**
  - [03:23](https://www.youtube.com/watch?v=IZKh6lo9SP4&t=203s) Relieve each fin at its base so it can actually deflect; fin length and thickness tune fit stiffness. **Confidence: High.**
  - [04:08](https://www.youtube.com/watch?v=IZKh6lo9SP4&t=248s) A longer-travel internal spring-and-latch can provide positive detents, but its internal bridge must be designed to avoid sag that jams the mechanism. **Confidence: High.**
- **Conditions/exceptions:** Clearances, relief height, spring travel, creep, and fatigue must be validated for the selected material and printer. “Perfect every time” is a design aim, not demonstrated cross-platform qualification.
- **Internal tension:** The video describes solid fits as insufficiently tolerant, yet still presents a solid tapered fit as useful for permanent closures; required removability changes the recommendation.

### 5. 10 Ways to Hide Layer Lines

- **Source:** [video](https://www.youtube.com/watch?v=pUabxkiJAdE), 2025-07-18, 8:19.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:17.
- **Claims:**
  - [00:01](https://www.youtube.com/watch?v=pUabxkiJAdE&t=1s) A simple knurled pattern can add grip and visual contrast while remaining relatively easy to model and tessellate. **Confidence: High.**
  - [03:38](https://www.youtube.com/watch?v=pUabxkiJAdE&t=218s) Diagonal texture lines at multiple heights visually compete with horizontal layer lines and can obscure apparent print orientation. **Confidence: High.**
  - [04:30](https://www.youtube.com/watch?v=pUabxkiJAdE&t=270s) Dense continuous curves can greatly increase mesh size and tool motion even when the repeated source sketch is simple. **Confidence: High.**
  - [06:31](https://www.youtube.com/watch?v=pUabxkiJAdE&t=391s) Adding versus subtracting the same hemispherical pattern produces different tactile behavior: rounded raised bumps versus sharper recessed-edge peaks. **Confidence: High.**
  - [06:51](https://www.youtube.com/watch?v=pUabxkiJAdE&t=411s) Texture should be selected for the desired customer interaction—appearance, grip, softness, drainage, or brand identity—not merely to conceal layer lines. **Confidence: High.**
- **Conditions/exceptions:** Texture may slow printing, enlarge meshes, create dirt traps, reduce dimensional control, or weaken a thin wall. The video provides visual demonstrations, not measured abrasion, hygiene, or grip tests.
- **Internal contradictions:** None material observed.

### 6. STOP Filling Your Build Plate

- **Source:** [video](https://www.youtube.com/watch?v=ZpmiK0aY9VM), 2025-05-09, 8:46.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:47.
- **Claims:**
  - [01:13](https://www.youtube.com/watch?v=ZpmiK0aY9VM&t=73s) Independent parts spread across a bed create a cascading-failure risk when one loose or failed part collides with its neighbors. **Confidence: High.**
  - [02:32](https://www.youtube.com/watch?v=ZpmiK0aY9VM&t=152s) A loose pile of many parts, especially mixed sizes, is difficult to compare economically with the expected set during visual inspection. **Confidence: High.**
  - [03:38](https://www.youtube.com/watch?v=ZpmiK0aY9VM&t=218s) A common modeled raft can retain a multi-part kit as one inspectable unit rather than as unrelated loose objects. **Confidence: High.**
  - [05:20](https://www.youtube.com/watch?v=ZpmiK0aY9VM&t=320s) The video proposes a thin, solid raft and a tuned one-layer-scale separation, while explicitly recommending test prints because removal force varies. **Confidence: Medium** because the automatic captions make the exact decimal values ambiguous.
  - [06:36](https://www.youtube.com/watch?v=ZpmiK0aY9VM&t=396s) Text, QR codes, numbering, and component outlines on the raft can serve as packaging-like instructions and missing-part indicators. **Confidence: High.**
- **Conditions/exceptions:** Batching increases coupled risk and is only justified when set integrity or machine-attendance savings outweigh it. A raft can itself warp, alter bottom finish, or make all parts fail together.
- **Internal tension:** The video first warns that coupling parts spreads failures, then recommends a raft that couples them. Its intended distinction is uncontrolled collision propagation versus a deliberately constrained, inspectable set.

### 7. 3D Print Better Fan Blades Without Wasting Filament

- **Source:** [video](https://www.youtube.com/watch?v=SWOnmWCi6bY), 2025-03-22, 4:11.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:10.
- **Claims:**
  - [00:21](https://www.youtube.com/watch?v=SWOnmWCi6bY&t=21s) Orient a radial fan/propeller flat so its blades and hub are formed by continuous in-plane layers rather than stacked weak blade roots. **Confidence: High.**
  - [01:04](https://www.youtube.com/watch?v=SWOnmWCi6bY&t=64s) Where blade pitch creates unavoidable undersides, use minimal designed breakaway supports instead of broad generated support. **Confidence: High.**
  - [01:49](https://www.youtube.com/watch?v=SWOnmWCi6bY&t=109s) An outer ring can stabilize blade tips and act as permanent support for steep blades, trading added mass and aerodynamic obstruction for stiffness and easier production. **Confidence: High.**
  - [02:39](https://www.youtube.com/watch?v=SWOnmWCi6bY&t=159s) Additive manufacture permits blade-edge and turbulence-control features that would be constrained by mold release, but their aerodynamic effect must be designed and tested. **Confidence: Medium** because no airflow, noise, balance, or fatigue measurements are shown.
- **Conditions/exceptions:** High-speed rotating parts are safety critical; the video does not qualify balance, overspeed containment, fatigue life, temperature, or impact behavior. Do not treat this as permission to print an untested high-speed rotor.
- **Internal tension:** The claim that the ring can remain thin conflicts with the need for stiffness, balance, and containment; those requirements need analysis per fan.

### 8. How-to Design Print in Place Hinges

- **Source:** [video](https://www.youtube.com/watch?v=BWsUk1xSSn4), 2025-02-08, 8:22.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:18.
- **Claims:**
  - [00:14](https://www.youtube.com/watch?v=BWsUk1xSSn4&t=14s) A flat compliant hinge must lie on the bed and its usable bend depends strongly on material; short PLA flexures can kink or snap, while longer flexures reduce strain. **Confidence: High.**
  - [01:30](https://www.youtube.com/watch?v=BWsUk1xSSn4&t=90s) Alternating slots can distribute a tight bend across multiple twisting ligaments rather than one short fold line. **Confidence: High.**
  - [02:12](https://www.youtube.com/watch?v=BWsUk1xSSn4&t=132s) For a loop-and-pin hinge, align the pin axis and load-bearing loop paths with the layers and make the loops sufficiently substantial. **Confidence: High.**
  - [03:14](https://www.youtube.com/watch?v=BWsUk1xSSn4&t=194s) A tapered/conical captive pivot can print vertically without side travel, but its upright root remains vulnerable to interlayer fracture. **Confidence: High.**
  - [05:57](https://www.youtube.com/watch?v=BWsUk1xSSn4&t=357s) Printing complementary conical pivots on their side can remove the critical overhang and place the pivot geometry in a stronger layer orientation. **Confidence: High.**
- **Conditions/exceptions:** Hinge clearances, friction, creep, fatigue, and material strain limits require testing. “Print-in-place” does not guarantee free movement after cooling or repeated cycles.
- **Internal tension:** The video calls the double-cone form effectively unbreakable, then documents overhang/fusing problems and recommends alternate geometry/orientation; the categorical durability language is not accepted.

### 9. We 3D Printed a Screwdriver Case for Linus Tech Tips

- **Source:** [video](https://www.youtube.com/watch?v=-Ryo2uWkC4I), 2024-12-14, 10:16.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-10:14.
- **Claims:**
  - [02:33](https://www.youtube.com/watch?v=-Ryo2uWkC4I&t=153s) Case orientation is a tradeoff: printing flat can expose a premium bed texture, while a diagonal production orientation may use bed area more efficiently and equalize visible surfaces. **Confidence: High.**
  - [03:38](https://www.youtube.com/watch?v=-Ryo2uWkC4I&t=218s) A case and hinge can be printed as one mechanism, removing a dowel and assembly step when the hinge clearance and orientation are designed accordingly. **Confidence: High.**
  - [04:28](https://www.youtube.com/watch?v=-Ryo2uWkC4I&t=268s) Pyramidal grooves in screw trays can passively settle loose fasteners into rows, using geometry to improve handling without another component. **Confidence: High.**
  - [05:55](https://www.youtube.com/watch?v=-Ryo2uWkC4I&t=355s) Chamfers on bed-facing case and hinge edges are preferred to underside fillets to create supported, crisp first-layer transitions. **Confidence: High.**
  - [08:45](https://www.youtube.com/watch?v=-Ryo2uWkC4I&t=525s) A shared leaf spring behind a row of bit holes can maintain contact across dimensional variation better than relying on every rigid hole to have a perfect diameter. **Confidence: High.**
- **Conditions/exceptions:** The case is a concept demonstration, not a controlled comparison with the commercial product. The video notes that compliant latches may wear and that magnets or a metal hinge pin can be preferable despite added assembly.
- **Internal tension:** Claims of superior hinge durability are explicitly untested in the video; the speaker says a comparative tensile test would still be needed.

### 10. Design Stronger Vase Mode Prints Using This Secret Technique

- **Source:** [video](https://www.youtube.com/watch?v=mHRQkreuuDA), 2024-11-23, 8:11.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:08.
- **Claims:**
  - [01:34](https://www.youtube.com/watch?v=mHRQkreuuDA&t=94s) Vase mode follows one continuous outer contour, offering low mass and fast production but little inherent resistance when the contour is a simple smooth shell. **Confidence: High.**
  - [02:00](https://www.youtube.com/watch?v=mHRQkreuuDA&t=120s) Folds, angles, corrugations, and re-entrant depth can stiffen a single-wall shell by making multiple planes interact. **Confidence: High.**
  - [02:39](https://www.youtube.com/watch?v=mHRQkreuuDA&t=159s) Orienting the prismatic block on its side makes the intended cross-section the repeated continuous path. **Confidence: High.**
  - [03:06](https://www.youtube.com/watch?v=mHRQkreuuDA&t=186s) A narrow slot through an otherwise closing wall can preserve one uninterrupted vase-mode contour instead of forcing a fragile top closure. **Confidence: High.**
- **Conditions/exceptions:** Single-wall stiffness is geometry and material dependent. The video explicitly says a child product needs separate material choice, bite/chunk-detachment testing, and safety qualification; PLA demonstration parts are not proof of suitability.
- **Internal tension:** The video describes the form as structural, then shows a demonstrator cracking/peeling and proposes TPU for safety. The concept is promising, not qualified.

### 11. This Box Keeps Out Water Without a Seal

- **Source:** [video](https://www.youtube.com/watch?v=prMUfQ9y7Rk), 2024-11-19, 4:29.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:27.
- **Claims:**
  - [01:43](https://www.youtube.com/watch?v=prMUfQ9y7Rk&t=103s) A lid can admit rain through its outer seam yet redirect it backward into a protected labyrinth channel rather than toward the enclosure interior. **Confidence: High.**
  - [02:05](https://www.youtube.com/watch?v=prMUfQ9y7Rk&t=125s) Give the collected water a continuous downhill channel and explicit bottom egress points so it leaves the enclosure. **Confidence: High.**
  - [02:13](https://www.youtube.com/watch?v=prMUfQ9y7Rk&t=133s) The approach is water-shedding, not pressure-tight: sufficiently high pressure or flow can overwhelm the drain channel. **Confidence: High.**
  - [03:45](https://www.youtube.com/watch?v=prMUfQ9y7Rk&t=225s) Additive undercuts can consolidate the drainage labyrinth into the enclosure/lid geometry and avoid a separately installed gasket. **Confidence: High.**
- **Conditions/exceptions:** No IP rating, immersion test, pressure test, condensation analysis, capillary analysis, or aging test is shown. Gasketless drainage is not equivalent to waterproof sealing.
- **Internal tension:** The opening calls the box “waterproof,” while the body states water enters the seam and high pressure can defeat the channel. The defensible description is rain-resistant or water-shedding under specified orientation and flow.

### 12. Water-Resistant Vents for Industrial Applications

- **Source:** [video](https://www.youtube.com/watch?v=bO39lWkaspA), 2024-11-02, 9:55.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-09:53.
- **Claims:**
  - [01:03](https://www.youtube.com/watch?v=bO39lWkaspA&t=63s) A Tesla-valve path may resist water, but it is bulky and adds airflow drag/turbulence, so it is presented as viable rather than preferred. **Confidence: High.**
  - [02:54](https://www.youtube.com/watch?v=bO39lWkaspA&t=174s) Multiple offset slat layers can remove a direct line of sight: droplets strike successive barriers while air follows a turning path. **Confidence: High.**
  - [03:29](https://www.youtube.com/watch?v=bO39lWkaspA&t=209s) Barriers must lead to a bottom drain; otherwise blocked water accumulates and eventually reaches the protected side. **Confidence: High.**
  - [04:14](https://www.youtube.com/watch?v=bO39lWkaspA&t=254s) A top drain becomes an ingress shortcut, so a gravity-drained vent is directional and its installed orientation must be controlled. **Confidence: High.**
  - [05:41](https://www.youtube.com/watch?v=bO39lWkaspA&t=341s) Add thin ribs to limit long bridges and support slats, but align them so they do not obstruct the intended drainage/air path. **Confidence: High.**
  - [06:34](https://www.youtube.com/watch?v=bO39lWkaspA&t=394s) Reorienting the vent can place deposited paths along the slats for better strength, trading away some ejection/packing advantages. **Confidence: High.**
- **Conditions/exceptions:** Slat count, spacing, thickness, pressure drop, fan performance, drainage rate, wind-driven rain, contamination, and cleaning need application-specific tests. No ingress-protection rating is established.
- **Internal tension:** The video calls the offset-slat concept nearly foolproof, then acknowledges prolonged/high-pressure water and orientation can defeat it.

### 13. We Made Tinker Toys for Adults

- **Source:** [video](https://www.youtube.com/watch?v=csUGcIPNNkk), 2024-10-31, 8:06.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:05.
- **Claims:**
  - [01:56](https://www.youtube.com/watch?v=csUGcIPNNkk&t=116s) Truncating a three-way bracket's corner creates a diagonal bed face so successive layers form closed loops around all three extrusion sockets. **Confidence: High.**
  - [04:04](https://www.youtube.com/watch?v=csUGcIPNNkk&t=244s) A thick shell separated by low-density internal structure is proposed for a clamp, placing more material away from the neutral axis without molding-style hollow cavities. **Confidence: Medium** because no load test is shown.
  - [04:36](https://www.youtube.com/watch?v=csUGcIPNNkk&t=276s) Print a loaded screw/bolt horizontally, cropping a flat on its round profile if needed, so tensile load does not pull stacked layers apart. **Confidence: High.**
  - [05:39](https://www.youtube.com/watch?v=csUGcIPNNkk&t=339s) A teardrop or flattened roof over a horizontal threaded hole avoids the unsupported circular crown while retaining useful side threads. **Confidence: High.**
  - [06:46](https://www.youtube.com/watch?v=csUGcIPNNkk&t=406s) T-slot joiners are also oriented diagonally so the load-bearing paths loop around the joint rather than split on one flat layer plane. **Confidence: High.**
- **Conditions/exceptions:** Clamp torque, thread stripping, sustained load, extrusion fit, creep, and safety factors are not quantified. Cropping a screw changes engagement and concentricity and must be acceptable for the application.
- **Internal tension:** The speaker calls diagonal/slanted prints categorically stronger; actual best orientation depends on the specific load components and failure modes.

### 14. STOP Using Brims. CAD is So Much Better

- **Source:** [video](https://www.youtube.com/watch?v=4GxZXxNraY0), 2024-09-14, 9:47.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-09:46.
- **Claims:**
  - [01:53](https://www.youtube.com/watch?v=4GxZXxNraY0&t=113s) Keep a modeled brim thin enough to be unambiguously sacrificial rather than a permanent feature; the captioned decimal is ambiguous, so no universal thickness is extracted. **Confidence: High for the principle; Low for the number.**
  - [02:35](https://www.youtube.com/watch?v=4GxZXxNraY0&t=155s) Prefer a circular or rounded brim footprint because sharp first-layer corners create peel-up points. **Confidence: High.**
  - [03:41](https://www.youtube.com/watch?v=4GxZXxNraY0&t=221s) A brim modeled as part of the first-layer geometry can create a more continuous toolpath than an automatically appended set of perimeter loops. **Confidence: Medium** because exact path generation remains slicer dependent.
  - [05:49](https://www.youtube.com/watch?v=4GxZXxNraY0&t=349s) Recess the brim contact behind a bottom chamfer so residual material does not enlarge the functional envelope and the chamfer provides a removal guide/break line. **Confidence: High.**
  - [07:28](https://www.youtube.com/watch?v=4GxZXxNraY0&t=448s) Use localized circular “mouse ears” only at tendrils or warp-prone corners when a full brim would add unnecessary removal work. **Confidence: High.**
- **Conditions/exceptions:** First-layer path, line width, layer height, material shrink, and removal tools matter. A CAD brim cannot be assumed to remain one layer under every process profile.
- **Internal tension:** The video rejects slicer dependence while relying on expected slicer interpretation of thin modeled geometry and optional concentric paths.

### 15. Stable Feet Designs for Your 3D Printed Products

- **Source:** [video](https://www.youtube.com/watch?v=hSP9CkqhZSQ), 2024-09-07, 5:04.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:03.
- **Claims:**
  - [01:02](https://www.youtube.com/watch?v=hSP9CkqhZSQ&t=62s) Feet on the functional bottom often require the product to print on a side or diagonal; printing feet-down would suspend the whole base and demand support. **Confidence: High.**
  - [01:46](https://www.youtube.com/watch?v=hSP9CkqhZSQ&t=106s) Chamfer the underside of side-facing feet so they grow without support instead of starting as horizontal shelves. **Confidence: High.**
  - [02:18](https://www.youtube.com/watch?v=hSP9CkqhZSQ&t=138s) Blend and round long rectangular feet to remove sharp overhanging corners and abrupt path/retraction points. **Confidence: High.**
  - [03:25](https://www.youtube.com/watch?v=hSP9CkqhZSQ&t=205s) Recessed pockets locate adhesive rubber feet, provide lateral support, and hide placement variation better than bonding pads to an unconstrained flat wall. **Confidence: High.**
- **Conditions/exceptions:** Printed feet provide standoff but may be slippery; high-friction pads add assembly and are not compatible with every print-on-demand workflow. Orientation must also respect the rest of the product's load and finish requirements.
- **Internal contradictions:** None material observed.

### 16. Design Rafts in CAD

- **Source:** [video](https://www.youtube.com/watch?v=7KVh19WpOcc), 2024-08-17, 8:03.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-08:03.
- **Claims:**
  - [02:51](https://www.youtube.com/watch?v=7KVh19WpOcc&t=171s) Start raft separation near the intended layer scale, then tune it for adhesion and release rather than relying on a named slicer parameter. **Confidence: High; exact captioned decimal excluded.**
  - [03:05](https://www.youtube.com/watch?v=7KVh19WpOcc&t=185s) Round raft edges—or use a circular raft—to remove first-layer corner peel points. **Confidence: High.**
  - [03:38](https://www.youtube.com/watch?v=7KVh19WpOcc&t=218s) Small breakaway struts under critical edges can prevent the model peeling from the raft when gap-only adhesion is insufficient. **Confidence: High.**
  - [04:36](https://www.youtube.com/watch?v=7KVh19WpOcc&t=276s) Shallow underside reliefs can interrupt long first-layer raster lines, reducing continuous shrink paths while leaving perimeter adhesion. **Confidence: Medium** because the claimed warp reduction is not tested here.
  - [05:17](https://www.youtube.com/watch?v=7KVh19WpOcc&t=317s) Cross or segmented relief patterns can break up shrink paths in multiple raster directions; pattern choice still depends on actual generated paths. **Confidence: Medium.**
- **Conditions/exceptions:** Later “hemisphere/Velcro” dimensions are ambiguous in captions and depend on supplier cooperation, so they are not extracted as numerical guidance. A thick raft can itself consume material, change cooling, and warp.
- **Internal tension:** The video seeks slicer independence but several mechanisms only work if the slicer preserves thin reliefs and predicts a particular first-layer path.

### 17. You're Designing Parts Too Thin

- **Source:** [video](https://www.youtube.com/watch?v=as84ZBjdmxU), 2024-08-01, 4:13.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:11.
- **Claims:**
  - [00:59](https://www.youtube.com/watch?v=as84ZBjdmxU&t=59s) Blend a thin plate into a perpendicular wall with a broad chamfer, loft, or similar transition to increase load-transfer area. **Confidence: High.**
  - [01:22](https://www.youtube.com/watch?v=as84ZBjdmxU&t=82s) Round vertical edges and blend abrupt corners to reduce stress concentrations and unstable corner toolpaths. **Confidence: High.**
  - [01:44](https://www.youtube.com/watch?v=as84ZBjdmxU&t=104s) A larger hollow shell can move material away from the neutral axis and create beam-like stiffness without being a solid block. **Confidence: Medium** because cost and strength depend on generated walls/infill.
  - [02:02](https://www.youtube.com/watch?v=as84ZBjdmxU&t=122s) For some structural brackets, begin from the allowed solid envelope and remove functional clearances rather than copying thin molded ribs into FDM. **Confidence: High.**
- **Conditions/exceptions:** “Chunkier” is not a universal objective; mass, print time, thermal stress, resonance, access, and local load paths still constrain the envelope. Internal structure cannot be assumed without controlling or verifying slicing.
- **Internal tension:** The video says extra thickness does not increase cost, then relies on hollow/infill behavior that is itself controlled by manufacturing settings.

### 18. Types of Lids

- **Source:** [video](https://www.youtube.com/watch?v=7YAylxQFe3k), 2024-07-13, 5:50.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:47.
- **Claims:**
  - [00:06](https://www.youtube.com/watch?v=7YAylxQFe3k&t=6s) Chamfer first-layer lid edges and round vertical corners to improve repeatability on small closure parts. **Confidence: High.**
  - [00:54](https://www.youtube.com/watch?v=7YAylxQFe3k&t=54s) Give a friction lid or plug a shallow taper/lead-in so engagement starts easily and tightness rises progressively. **Confidence: High.**
  - [01:41](https://www.youtube.com/watch?v=7YAylxQFe3k&t=101s) Reduce continuous contact with ripples or discrete contact regions when layer ridges make a full cylindrical interference fit bind. **Confidence: High.**
  - [02:27](https://www.youtube.com/watch?v=7YAylxQFe3k&t=147s) Use a self-supporting thread profile, with sloped rather than flat undersides, when both mating thread forms can be designed together. **Confidence: High.**
  - [03:21](https://www.youtube.com/watch?v=7YAylxQFe3k&t=201s) A quarter-turn nub-and-channel closure can give faster, more positive engagement than long threads; slope or detent the channel if tightening/locking is required. **Confidence: High.**
  - [04:00](https://www.youtube.com/watch?v=7YAylxQFe3k&t=240s) Chamfer channel roofs and nubs to avoid horizontal overhangs, especially on curved walls. **Confidence: High.**
- **Conditions/exceptions:** Taper, clearance, thread profile, detent force, wear, and creep are application dependent. The video's angle/depth numbers are not adopted as universal limits.
- **Internal contradictions:** None material observed.

### 19. Print in Place Latch Mechanism

- **Source:** [video](https://www.youtube.com/watch?v=4wRKmcWXEkw), 2024-07-02, 7:09.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-07:06.
- **Claims:**
  - [02:15](https://www.youtube.com/watch?v=4wRKmcWXEkw&t=135s) Print the latch body on its long edge to support ejection/packing and keep the internal slider in a favorable plane. **Confidence: High for the presented geometry.**
  - [02:37](https://www.youtube.com/watch?v=4wRKmcWXEkw&t=157s) Rotate the spring pattern so its flex occurs in the layer plane imposed by that body orientation; tune stiffness through ligament thickness and path length. **Confidence: High.**
  - [03:27](https://www.youtube.com/watch?v=4wRKmcWXEkw&t=207s) Chamfer the moving tongue and the internal roof so they build to a ridge instead of creating broad sagging surfaces that can fuse the mechanism. **Confidence: High.**
  - [03:57](https://www.youtube.com/watch?v=4wRKmcWXEkw&t=237s) Add a local collar around screw holes when fastener insertion could split the housing. **Confidence: High.**
  - [04:38](https://www.youtube.com/watch?v=4wRKmcWXEkw&t=278s) Where an internal opening still needs support, model a labeled breakaway block at known clearances and with an accessible removal path. **Confidence: High.**
- **Conditions/exceptions:** Internal clearances, bridge sag, debris, spring fatigue, wear, and removal access require prototypes. The captioned support-gap decimals are not reliable enough to extract.
- **Internal tension:** The video presents the printed mechanism as eliminating assembly, but its designed support still adds a manual removal step.

### 20. Mounted Enclosure Boxes

- **Source:** [video](https://www.youtube.com/watch?v=lGnpz8q4STw), 2024-06-27, 4:59.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:59.
- **Claims:**
  - [00:11](https://www.youtube.com/watch?v=lGnpz8q4STw&t=11s) Prepare an enclosure to print on an edge/diagonal with a real chamfered bed face and a designed stabilizing rib rather than defaulting to its largest face. **Confidence: High.**
  - [01:05](https://www.youtube.com/watch?v=lGnpz8q4STw&t=65s) Align a belt/strap slot so deposited paths form continuous loops around the slot instead of allowing strap load to peel layers apart. **Confidence: High.**
  - [01:37](https://www.youtube.com/watch?v=lGnpz8q4STw&t=97s) Integrate DIN-rail or extrusion interfaces into the housing when that removes separate brackets and assembly. **Confidence: High.**
  - [02:24](https://www.youtube.com/watch?v=lGnpz8q4STw&t=144s) Locally thicken screw-hole regions to reduce breakout and fatigue without thickening every enclosure wall. **Confidence: High.**
  - [03:44](https://www.youtube.com/watch?v=lGnpz8q4STw&t=224s) Prefer a mounting lug that grows from and blends into the enclosure body over a thin planar tab cantilevered from the wall. **Confidence: High.**
- **Conditions/exceptions:** Final orientation must reconcile mount loads, lid/interface tolerances, surface finish, drainage, and assembly access. Integrated mounts can make a whole enclosure scrap if one interface is wrong.
- **Internal contradictions:** None material observed.

### 21. 3x Part Strength Without Slicer Settings

- **Source:** [video](https://www.youtube.com/watch?v=Lq-SoGgKOcQ), 2024-05-25, 4:06.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:03.
- **Claims:**
  - [00:28](https://www.youtube.com/watch?v=Lq-SoGgKOcQ&t=28s) For a bending rod, adding material to outer walls is mechanically more useful than placing the same material near the neutral axis. **Confidence: High.**
  - [01:14](https://www.youtube.com/watch?v=Lq-SoGgKOcQ&t=74s) Very small longitudinal holes, slots, or ripples near the perimeter are proposed as CAD features that induce extra perimeter paths in selected outer regions. **Confidence: High.**
  - [02:09](https://www.youtube.com/watch?v=Lq-SoGgKOcQ&t=129s) Microfeatures must be detectable by the manufacturing pipeline yet narrow enough that adjacent deposited walls fuse; otherwise they can create a separated sleeve and weaken the rod. **Confidence: High for the principle; Low for the captioned width.**
  - [02:47](https://www.youtube.com/watch?v=Lq-SoGgKOcQ&t=167s) The video reports its ribbed specimen at roughly three times the strength of a baseline thin-wall cylinder. **Confidence: Medium that this is the stated result; Low as general evidence** because test method, sample count, data, and failure statistics are not presented here.
- **Conditions/exceptions:** The technique depends on tessellation, mesh repair, feature resolution, extrusion width, wall generation, fusion, and load direction. A solid or explicitly shelled geometry may be more predictable.
- **Internal tension:** The goal is slicer independence, but the mechanism deliberately depends on a slicer detecting and converting sub-wall geometry into specific perimeter paths.

### 22. Stop Snapping Your Snap Fits

- **Source:** [video](https://www.youtube.com/watch?v=_y8Yvu1FQIE), 2024-05-16, 5:05.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-05:01.
- **Claims:**
  - [00:19](https://www.youtube.com/watch?v=_y8Yvu1FQIE&t=19s) Upright clips on a ring can snap where their roots cross stacked layer planes. **Confidence: High.**
  - [01:36](https://www.youtube.com/watch?v=_y8Yvu1FQIE&t=96s) Tilting the ring places more of each clip within the layer plane while avoiding a fully supported sideways print. **Confidence: High.**
  - [02:11](https://www.youtube.com/watch?v=_y8Yvu1FQIE&t=131s) Round/chamfer downward clip edges and add a true bed flat so the chosen diagonal orientation has supported starts and stable contact. **Confidence: High.**
  - [02:52](https://www.youtube.com/watch?v=_y8Yvu1FQIE&t=172s) If clip strength is critical, rotate the ring sideways and position clips diagonally around it so no critical clip lies at the top/bottom weak plane. **Confidence: High.**
  - [03:34](https://www.youtube.com/watch?v=_y8Yvu1FQIE&t=214s) Sideways orientation may create an internal roof; use designed interior support and move lower clips into bed contact where possible. **Confidence: High.**
- **Conditions/exceptions:** Diagonal or sideways orientation can add brims, supports, rough back edges, and packing cost. Clip strain, travel, root radius, fatigue, and material remain separate requirements.
- **Internal tension:** Reinforcing upright clips with large chamfers improves root strength but reduces their independent compliance, shifting flex into the ring.

### 23. Secrets to Better 3D Printed Domes

- **Source:** [video](https://www.youtube.com/watch?v=udEeJjzEQZI), 2024-04-23, 4:17.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:18.
- **Claims:**
  - [00:35](https://www.youtube.com/watch?v=udEeJjzEQZI&t=35s) Pulling a dome toward an egg/pointed profile reduces the nearly horizontal internal crown that otherwise prints into open space. **Confidence: High.**
  - [01:01](https://www.youtube.com/watch?v=udEeJjzEQZI&t=61s) Preserve a hemispherical exterior while changing the nonfunctional interior to a conical/self-supporting roof when constant wall thickness is unnecessary. **Confidence: High.**
  - [02:08](https://www.youtube.com/watch?v=udEeJjzEQZI&t=128s) If both inner and outer spherical surfaces are required, use a minimal designed “mushroom” support with a broad cap and narrow accessible stem. **Confidence: High.**
  - [02:13](https://www.youtube.com/watch?v=udEeJjzEQZI&t=133s) Tune the support gap by experiment; the stated nominal half-millimeter-scale gap is geometry/process specific. **Confidence: Medium.**
  - [03:00](https://www.youtube.com/watch?v=udEeJjzEQZI&t=180s) When generated support is unavoidable on a large dome, flatten a small internal crown to give it a defined contact/release region. **Confidence: High.**
- **Conditions/exceptions:** A pointed interior changes internal volume and wall thickness; a support introduces witness marks and removal access. Large domes also need buckling and thermal-warp checks.
- **Internal tension:** The video strongly criticizes generated supports, then recommends them for large domes where they may use less material; the correct choice is geometry and scale dependent.

### 24. Connect 3D Printed Parts

- **Source:** [video](https://www.youtube.com/watch?v=djm5tCFn9S0), 2024-03-19, 4:30.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:31.
- **Claims:**
  - [00:28](https://www.youtube.com/watch?v=djm5tCFn9S0&t=28s) Replace a horizontal round peg/hole with a diamond-oriented square pair to avoid a sagging circular roof and let the peg print with continuous longitudinal layers. **Confidence: High.**
  - [01:06](https://www.youtube.com/watch?v=djm5tCFn9S0&t=66s) For a low-profile edge joint, use a broad slab-and-slot with a tapered/rounded lead-in so the fit tightens progressively. **Confidence: High.**
  - [02:05](https://www.youtube.com/watch?v=djm5tCFn9S0&t=125s) A separate symmetric S-shaped connector can pull two mirrored slots together and resist a gap more positively than friction pegs. **Confidence: High.**
  - [02:47](https://www.youtube.com/watch?v=djm5tCFn9S0&t=167s) A double-sided C/snap connector is quicker and more intuitive to assemble but is more tolerance- and fatigue-sensitive because it must flex during insertion. **Confidence: High.**
- **Conditions/exceptions:** Separate connectors add inventory and assembly. Fits require actual clearance tests, and a square/diamond peg does not automatically solve pullout, shear, wear, or alignment.
- **Internal contradictions:** None material observed.

### 25. Simplify Assembly with Glue Slots

- **Source:** [video](https://www.youtube.com/watch?v=qV1xXXbzM4Y), 2024-03-02, 4:03.
- **Access/coverage:** official `en-orig` automatic captions, complete 00:00-04:05.
- **Claims:**
  - [01:00](https://www.youtube.com/watch?v=qV1xXXbzM4Y&t=60s) Reverse-tapered microcavities let cured adhesive form mechanical keys inside the part instead of relying only on surface adhesion. **Confidence: High.**
  - [01:23](https://www.youtube.com/watch?v=qV1xXXbzM4Y&t=83s) Relief volume gives excess adhesive somewhere to flow so bond-line thickness does not unintentionally hold mating faces apart. **Confidence: High.**
  - [01:48](https://www.youtube.com/watch?v=qV1xXXbzM4Y&t=108s) Patterned glue regions can encode where and how much adhesive an assembler should apply, reducing process ambiguity. **Confidence: High.**
  - [02:47](https://www.youtube.com/watch?v=qV1xXXbzM4Y&t=167s) An internal distribution channel with an external injection port can deliver adhesive after parts are already located and clamped. **Confidence: High.**
- **Conditions/exceptions:** Adhesive chemistry, wetting, cure shrink, venting, surface preparation, nozzle access, squeeze-out, serviceability, and inspection remain application specific. Undercuts can trap uncured material or contamination.
- **Internal contradictions:** None material observed.

## Cross-video tensions to carry into synthesis

- **“Slicer agnostic” versus slicer-induced geometry:** the channel often rejects slicer-specific settings while using thin cuts that rely on ordinary slicers to generate specific perimeters. These techniques require verification across representative slicers and profiles.
- **Universality versus tuning:** rafts, brims, snap fits, supports, and compliant lids are described as portable, but the same videos repeatedly advise material- and process-specific gap/geometry experiments.
- **Chunky shells versus settings independence:** thick hollow forms gain much of their efficiency from walls/infill, which still depend on a manufacturing profile unless the internal structure is explicitly modeled.
- **Waterproof versus water-shedding:** the box and vent geometries manage rain and spray through labyrinths and drainage; neither video establishes pressure-tightness or an IP rating.
- **Strength claims versus evidence:** many examples explain plausible load-path improvements, but only one video in this batch mentions a comparative strength result, without enough test detail to generalize it.
- **Designed support versus zero post-processing:** designed support improves predictability but still consumes material, leaves witness marks, and requires accessible removal.

## Validation counts

- Manifest entries: **25**.
- Unique video IDs: **25**.
- Extracted video sections: **25**.
- Accessible full official automatic-caption tracks: **25/25**.
- Inaccessible videos: **0**.
- Videos with a conditions/exceptions statement: **25/25**.
- Videos with an internal tension/contradiction statement: **25/25**.
- Timestamped claim bullets: **120**.
- Ambiguous automatic-caption numbers promoted as universal rules: **0**.
- Full transcripts retained in the project: **0**.

## Batch boundary

This file completes claim extraction for the 25 manifest IDs only. It intentionally does not duplicate batch 01 or the supplied batch-02 exclusion list, and it does not imply that the remaining definite/probable Slant 3D candidates have been analyzed.
