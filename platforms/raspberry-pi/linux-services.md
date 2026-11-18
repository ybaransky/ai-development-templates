# Raspberry Pi: Standalone Development and systemd Production

- The **same application entry point** should run manually during development and under `systemd` in production.
- Keep configuration, logging destinations, working directories, and environment differences explicit rather than branching application logic by launch method.
- Use a project-managed Python virtual environment; document interpreter path and dependencies.
- Handle SIGINT (Ctrl+C) and SIGTERM (service stop) for graceful shutdown, releasing GPIO/devices and flushing important state.
- Prefer console logging during development and journald-compatible stdout/stderr in production.
- Use a service unit with explicit `WorkingDirectory`, `ExecStart`, user, and a bounded restart policy; do not assume root is necessary.
- Avoid hardcoded paths, credentials in service files, and accidental tight restart loops.
- Verify start, stop, restart, reboot, and failure recovery on the actual Pi before claiming production readiness.
