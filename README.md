# AI Development Templates

Reusable, self-contained instructions for **Codex** and **Claude Code** in solo-developer projects.

## What is included

- `common/`: general feature development, refactoring, architecture reviews, Git, and prompts.
- `languages/`: C++ and Python practices.
- `platforms/`: Arduino, PlatformIO, ESP8266, ESP32 variants, and Raspberry Pi.
- `templates/`: ready-to-copy Arduino/PlatformIO and Raspberry Pi/Python project starter files.

## Start a new project

1. Open the project folder in VS Code.
2. Copy the **contents** of `templates/arduino-platformio/` or `templates/raspberry-pi-python/` into its root (where `platformio.ini` or `pyproject.toml` lives). Do not overwrite existing project documents without reviewing them.
3. Fill in `docs/project.md`, `docs/architecture.md`, `docs/hardware.md` (if applicable), `docs/invariants.md`, and `docs/build-and-test.md`. These are project-specific starter forms.
4. For Arduino, copy the applicable `platforms/esp8266/` or `platforms/esp32/` documents into `docs/platforms/`, and update `AGENTS.md` to point to the chosen one. Remove references to irrelevant variants.
5. Open a **new** Codex or Claude Code session at the project root and ask it to summarize its instructions without changing files.
6. Keep these copied documents under the project's own Git history. Future changes to this template repo do **not** automatically update existing projects.

## Authority and safety

`AGENTS.md` is the common entry point. Claude Code reads `CLAUDE.md`, which imports `AGENTS.md` using `@AGENTS.md`. The detailed policies are ordinary documentation under `docs/` and should be read when relevant; neither tool is assumed to automatically load every linked file. Project-specific correctness and hardware constraints override general style preferences. Actual source code/configuration must be inspected before edits; if it conflicts with documentation, report the discrepancy.

## Template maintenance

Edit the canonical policy under `common/`, `languages/`, or `platforms/`, then intentionally propagate changes to the **self-contained copies** in `templates/`. Run `python tools/check_templates.py` to verify the copies match their canonical sources. Avoid Git submodules and symlinks: copyable projects should work offline.

## Git

This template assumes a solo developer who normally commits directly to the existing branch (often `master`). AI agents must not commit, push, create branches, or rewrite history without permission. See `common/docs/git-workflow.md`.
