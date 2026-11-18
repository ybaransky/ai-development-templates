# Embedded C++ Coding Standards

- Follow the project's existing naming, formatting, and language-standard settings.
- Prefer simple composition, explicit ownership, and concrete dependencies when there is only one implementation; interfaces/virtual dispatch require a concrete benefit.
- Use `constexpr`, `enum class`, `const`, references, and fixed-size storage where they improve safety and clarity.
- Avoid unnecessary dynamic allocation in hot paths, unbounded recursion, and large stack temporaries on constrained targets.
- Avoid `String` churn in tight loops on small MCUs; prefer bounded buffers where appropriate.
- Keep hardware-independent algorithms separable and host-testable where reasonable.
- Keep ISRs short and follow target-specific synchronization/atomicity requirements; `volatile` is not a general concurrency primitive.
- Favor readable functions and coherent modules; do not mechanically split functions or add wrappers merely to satisfy style rules.
- Document non-obvious rationale, hardware constraints, and intentional deviations from standard conventions.
- Review warnings and binary/resource impact; avoid hiding warnings without understanding them.
