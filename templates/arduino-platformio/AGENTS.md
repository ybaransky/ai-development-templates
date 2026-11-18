# Project Instructions — Codex and Claude Code

This file is the shared entry point. Read relevant documents under `docs/` **before** editing. Do not assume linked documents are automatically loaded.

## Working rules
- Inspect existing code, build configuration, tests, and `git status` before changing anything.
- Follow `docs/feature-development.md` for new work and `docs/refactoring.md` for cleanup.
- For a requested architecture review, follow `docs/architecture-review.md` and **do not edit files**.
- Follow `docs/git-workflow.md`: do not commit, push, branch, or discard changes without permission.
- Project-specific invariants, hardware constraints, and actual configuration take precedence over general style preferences.
- If source and docs disagree, report the discrepancy instead of silently reconciling them.
- Do not flash devices, deploy services, or change live configuration without explicit approval.
- After changes, report tests actually run, unverified behavior, and any remaining risks.

## Documentation to consult
- `docs/project.md`: what this application does and its environment.
- `docs/architecture.md`: modules, ownership, and data flow.
- `docs/invariants.md`: behavior and contracts that must be preserved.
- `docs/build-and-test.md`: exact local commands and target verification.
- `docs/coding-standards.md`: language-specific rules.
- `docs/platforms/`: applicable platform rules.

## Refactoring defaults
- Before adding features, look for reusable existing mechanisms and avoid redundant state.
- Prefer simplicity over speculative abstraction; fewer functions is not an end in itself.
- Propose a plan and wait for approval for structural or critical changes.

## Arduino / PlatformIO
- Read `docs/arduino-framework.md`, `docs/platformio.md`, and the **selected** `docs/platforms/` guidelines.
- Read `platformio.ini` before choosing build/test commands.
- Preserve GPIO and boot requirements; never change pin mappings without approval.
