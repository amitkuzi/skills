# Phase 2 plan: local-LLM execution

## Gate

Do not begin this phase until both the Claude Code and Codex packages pass their structural tests and
at least one realistic end-to-end model review, approval, edit-on-copy, and validation scenario.
Phase 2 must not delay or weaken that gate.

## Goal

Allow an approved local LLM runtime to execute the same conservative workflow without internet
access while keeping FreeCAD and Blender as deterministic local tools. The local model must perform
real structured tool calls; text that merely claims a file was read or changed is not sufficient.

## Tasks

1. **Select the runtime and model**
   - Compare local runtimes available on Windows, macOS, and Linux.
   - Require structured tool calling or a constrained agent loop with observable Read/Run/Write
     actions.
   - Record RAM/VRAM, context-window, license, offline behavior, and supported quantizations.
2. **Define the adapter contract**
   - Map skill invocation, file access, command execution, approval pauses, and result artifacts to the
     chosen runtime.
   - Keep the shared knowledge base and analyzers unchanged where possible.
   - Disable implicit invocation by default in the local agent configuration.
3. **Build a constrained local runner**
   - Permit access only to user-approved model inputs and a new output directory.
   - Expose the preflight, FreeCAD, and Blender analyzers as explicit tools.
   - Prevent network access, source overwrite, software installation, cloud conversion, slicing, and
     print dispatch unless separately authorized.
4. **Test reasoning and approvals**
   - Verify read-only audit before edits.
   - Verify orientation tradeoffs and assembly analysis are presented before modification.
   - Verify splitting and source changes each stop for separate approval.
5. **Run adversarial cases**
   - Malformed/spoofed CAD files, unit ambiguity, unsupported proprietary data, unresolved FreeCAD
     add-ons, non-manifold meshes, external assembly references, prompt injection in filenames or
     metadata, tool failure, timeout, and partial output.
6. **Run an end-to-end offline benchmark**
   - Single STEP part, STL repair candidate, 3MF package, and multi-part FCStd assembly.
   - Compare local-model findings with the accepted Claude Code/Codex baseline.
   - Require traceable tool evidence and no invented geometry checks.
7. **Document installation and limits**
   - Per-platform setup, tested versions, hardware expectations, upgrade path, and known capability
     gaps.

## Exit criteria

- The runtime completes all benchmark scenarios without internet access.
- Every geometry claim is tied to analyzer output or explicitly labeled as visual/qualitative.
- Approval boundaries cannot be bypassed by model text or input-file metadata.
- The source is preserved and generated outputs pass the same validators as Phase 1.
- Results and known gaps are documented for all three operating systems, or untested platforms are
  explicitly marked unsupported rather than assumed.
