# Python Testing

- Use the test framework already present; prefer `pytest` when starting fresh.
- Keep pure logic testable on a developer machine without Raspberry Pi hardware.
- Use fakes/mocks for GPIO, clock, network, and filesystem boundaries; do not over-mock core logic.
- Test normal paths, invalid inputs, timeouts, shutdown, and recovery.
- Run configured lint/type checks when present; do not invent project commands.
- Separate host tests from on-device integration tests and report which were actually run.
