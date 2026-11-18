# Embedded C++ Coding Standards

## General Coding Standards

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

## Code Documentation

Code must be understandable and maintainable by someone who did not originally write it.

### Classes and Structures — Mandatory

- **Every C++ `class` and `struct` declaration MUST have a preceding comment** explaining its responsibility and how it fulfills that responsibility.
- This applies to public and private classes, nested classes, and structures used solely to hold data.
- Document ownership, lifecycle, dependencies, and important invariants where applicable.
- Do not omit documentation merely because the class or structure appears simple.

### Member Variables — Mandatory

- **Every class member variable MUST have a comment** explaining its purpose, role, or the state it maintains.
- Prefer same-line comments when practical.
- Apply the same requirement to data members of `struct` types.
- Document units, valid ranges, ownership, and concurrency requirements when relevant.
- Comments must convey useful information rather than merely repeat the variable name.

### Functions and Methods

- Document functions whose behavior or contract is not immediately obvious.
- Explain parameters, return values, error conditions, and side effects when relevant.
- Document timing requirements, blocking behavior, and hardware assumptions.
- Use meaningful function names so trivial functions do not require redundant comments.
- Prefer explaining why an algorithm or implementation choice exists rather than narrating individual statements.

### Embedded Hardware Documentation

- Document GPIO assignments, peripheral dependencies, and electrical constraints.
- Explain interrupt requirements, timing assumptions, and watchdog considerations.
- Document memory ownership, buffer sizes, and resource limitations when important.
- Explain hardware workarounds and why they are necessary.
- Identify operations that must remain nonblocking.

### Documentation During Refactoring

- Preserve useful documentation when reorganizing code.
- Update comments whenever implementation details or behavior change.
- Remove or correct outdated comments.
- Never remove comments solely to reduce line count.
- Apply mandatory class, struct, and member documentation requirements to newly written code and declarations modified during refactoring.
- Do not perform unrelated documentation-only changes unless explicitly requested.
- Update relevant project documentation under `docs/` when architecture, interfaces, or invariants change.

### Comment Style

- Use `//` for short explanations.
- Use Doxygen-compatible `/** ... */` comments for complex public APIs when structured documentation is useful.
- Keep comments concise, accurate, and consistent with existing project conventions.