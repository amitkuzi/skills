---
name: visual-manual
description: Create branded visual LEGO/IKEA-style manuals for instructions, installation, assembly, and how-to procedures (הוראות, תהליך התקנה, הרכבה, מדריך), delivering HTML and PDF in Hebrew and English by default. Applies to physical builds and software setup, not requests to edit agent/system instructions.
---

# Visual Manual

Produce a usable visual manual, not a prose outline promising illustrations. Combine original LEGO/IKEA-inspired numbered drawings and short captions with a wide rounded hero, a prominent status/caution card, prerequisite cards, and generous spacing. Do not reproduce LEGO/IKEA logos or imply affiliation. Package version: 1.1.0.

## Language and scope

- Default to **both Hebrew and English**, even when the request uses only one language. Add explicitly requested languages alongside them; an explicit request such as "English only" overrides the default.
- Match every action, quantity, caution, and checkpoint across languages. Keep one shared step ID and diagram rather than separate manuals with drifting numbering.
- Set Hebrew text blocks to `lang="he" dir="rtl"`; English blocks to `lang="en" dir="ltr"`. Keep commands, paths, identifiers, and inline SVG geometry LTR with `dir="ltr"` or `<bdi>` as appropriate. Never mirror a physical assembly merely because its captions are RTL.
- **Hebrew is the right column and English is the left column on desktop and in print, regardless of DOM order.** Use a LTR grid with explicit named areas (`"en he"`) and assign direct children by language. In shared inventory tables, place the English item column to the left of the Hebrew item column. On narrow screens stack Hebrew then English; print restores the two-column layout and shows every requested language. Never hide a language just to fit a page.
- Give each additional language its own correct `lang` and `dir` (for example, Arabic `lang="ar" dir="rtl"`), with the same captions, cautions, and IDs. Expand the template's caption grid or stack blocks to keep every requested language legible.
- A request to explain installation/assembly creates a manual; it does not authorize performing installation, purchasing parts, or modifying a live system.

## Visual style and brand assets

Use this precedence: **explicit user style → established project visual style → user's brandkit**. Discover project instructions/styles and the user's configured brandkit before choosing colors, typography, and marks; a screenshot gives layout inspiration without permission to copy another product's content or identity. Use the user's brandkit by default when no project style is defined.

In Amit Kuzi's workspace the known brandkit is `D:\Development\amitkuzi-brandkit`: read its `README.md`, `colors/palette.json`, `fonts/fonts.css`, and appropriate `logos/*.svg` before authoring. Revalidate this location when available rather than assume it exists on another machine. Embed the selected actual palette, logo SVG, and local WOFF2 font bytes (data URLs) into the standalone HTML when accessible. Preserve required asset notices. Match its font roles: Archivo for English headings, Public Sans for English body, Rubik for Hebrew. The packaged template includes verified palette/logo geometry and font-role fallbacks; it does not bundle the fonts. Load and embed fonts for the actual deliverable. If assets or location cannot be accessed, state exactly what styling used a fallback and do not claim the complete brandkit was applied.

## Build the manual

1. Identify the exact object/product or software version, starting state, and intended finished state from the request and supplied materials. Inspect supplied images/files and authoritative manufacturer or software documentation when available. Ask only for missing details that prevent correct instructions; continue the confirmed portions. Mark unresolved steps visibly in every language and exclude them from the executable sequence until resolved. Never invent screw sizes, torque, dimensions, pinouts, commands, or screenshot evidence.
2. Show a cover with the finished-state drawing and title. List prerequisites, parts with stable IDs (`P1`, `P2`...), quantities, tools (`T1`...), and software requirements. For software-only tasks, replace physical stock with accounts, OS/version, downloads, permissions, and dependencies. Give measured duration/difficulty only when supported; otherwise omit them.
3. Divide the task into numbered panels, **one user action per panel**. Each includes the parts/tools needed, an actual diagram or supplied annotated image, a short matched caption, and the expected result. Carry the visible assembly/setup state forward so users can see what changed.
4. Draw insertion/movement arrows, orientation marks, fastener counts, and a magnified inset when needed. Reuse part IDs and line styles. Make warnings distinguishable by icon and text, never color alone. Include a checkpoint before an irreversible or easily confused operation and a final verification panel. Put troubleshooting next to the relevant checkpoint or in a short final section.
5. For software setup, use equivalent visual panels: a schematic screen or terminal, highlighted control/command, action arrow, and expected screen/output. Label schematic interfaces as illustrations; only call an image a screenshot when actually captured. Distinguish example output from observed output. Use selectable `<pre dir="ltr"><code>` blocks for exact commands and show meaningful success/failure signals. Do not put secrets in artifacts.

## Deliverables

By default, save and show/link **both a standalone HTML manual and an actual PDF exported from that same HTML**, containing the same languages and diagrams. An explicit output choice such as "HTML only" overrides this default. Start from [assets/manual-template.html](assets/manual-template.html) for its card layout, explicit language positioning, print rules, and sample diagram pattern. Replace its clearly marked demonstration content completely with the requested subject; duplicate panels as needed. The demonstration joint is illustrative, not a verified construction method. Draw each panel for the actual action rather than reusing generic icons as the entire illustration.

- Embed all diagrams/styles; no network assets, JavaScript, or additional runtime dependency is needed to read or print the manual.
- Use a responsive screen layout and A4 print CSS. Keep each panel together where it fits; split oversized panels into smaller actions before printing. Use high-contrast lines and legible caption sizes.
- Add an accessible title/description to each SVG and list factual sources or supplied-material provenance with dates/versions when relevant. Any unverified assumptions must stay visible in the finished manual.
- Export PDF with an available browser renderer or suitable HTML-to-PDF tool. Wait for `document.fonts.ready` before export; enable print backgrounds and use the A4 print CSS. Inspect rendered PDF pages for clipped panels, glyphs/RTL, arrows, and **English left / Hebrew right**. If any required renderer/font is unavailable, retain HTML and report the precise limitation and missing PDF as a partial delivery; printable HTML is not an exported PDF. An explicit format override can remove the PDF requirement.
- Open/preview the artifact with available tools. Check every ID and quantity against the inventory, Hebrew/English equivalence, arrow orientation, logical ordering, and final result. Check that all example content is replaced and no panel relies on unavailable external assets. State what was visually inspected versus only structurally checked.

For a small one-step request, keep the manual compact: one visual action panel with its bilingual caption and result is enough. If no file-writing or rendering tools are available, provide the complete standalone HTML source and state that file saving/preview could not be performed.
