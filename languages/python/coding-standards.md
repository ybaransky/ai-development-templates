# Python Coding Standards

- Follow existing project conventions and the configured Python version.
- Prefer clear modules/functions; introduce classes for meaningful state, lifecycle, or polymorphism, not for decoration.
- Use type hints at important boundaries and dataclasses when they simplify structured data.
- Keep side effects (GPIO, filesystem, network, database) behind narrow boundaries so logic can be tested independently.
- Use context managers for resources; close handles and hardware resources reliably.
- Avoid hidden mutable module state, broad exception suppression, and unbounded retries.
- Use explicit timeouts for I/O. Never block an asyncio event loop with synchronous slow work.
- Prefer standard-library tools when sufficient; manage dependencies in the project's declared environment.
- Log actionable failures without leaking credentials. Preserve behavior during refactoring.
