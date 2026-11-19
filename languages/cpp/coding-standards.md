# Embedded C++ Coding Standards

## General

- Follow the project's existing naming, formatting, and language-standard settings. Where the project has no established convention, use the Naming & Style rules below.
- Use `constexpr`, `enum class`, `const`, references, and fixed-size storage where they improve safety and clarity.
- Avoid unnecessary dynamic allocation in hot paths, unbounded recursion, and large stack temporaries on constrained targets.
- Avoid `String` churn in tight loops on small MCUs; prefer bounded buffers where appropriate.
- Keep hardware-independent algorithms separable and host-testable where reasonable.
- Keep ISRs short and follow target-specific synchronization/atomicity requirements; `volatile` is not a general concurrency primitive.
- Favor readable functions and coherent modules; do not mechanically split functions or add wrappers merely to satisfy style rules.
- Document non-obvious rationale, hardware constraints, and intentional deviations from standard conventions.
- Review warnings and binary/resource impact; avoid hiding warnings without understanding them.

## Design

- Apply SOLID principles, except that dependency inversion does not require an interface per class (see next bullet). Deviate from SOLID only with user approval, stating the pros and cons.
- Depend on concrete types. Introduce interfaces/virtual dispatch only when there is a real second implementation or a concrete testing benefit.
- **Use constructor injection of concrete types**, not interfaces.
- Objects own their state. A class that is really a façade over file-static globals is not injectable no matter how it is passed around.
- Favor composition over inheritance, and make ownership explicit.
- Separate concerns into layers (hardware drivers, domain logic, I/O and UI) with clear module boundaries and minimal coupling between them.
- Avoid leaky abstractions; prefer explicit behavior over implicit behavior.
- Do not use singletons. Create each long-lived object once in `main`/`setup()` and inject it where needed. Framework-provided globals such as `Serial` and `Wire` are exempt.
- Within a file, prefer classes. Across files, prefer functions for module boundaries.

## Naming & Style

- Follow Google naming conventions: `PascalCase` types, `camelCase` functions and locals, and `kPascalCase` constants and enum values. Reserve `ALL_CAPS` for macros and established hardware pin identifiers.
- **Class member variables use an `m_` prefix followed by camelCase** — a deliberate departure from Google's trailing underscore. Public fields of plain data structs take no prefix; they are the struct's interface, not its hidden state.
- Do **not** use a leading underscore: `_` followed by an uppercase letter is reserved everywhere, any leading underscore is reserved at global scope, and the ESP8266 core already defines `_min`/`_max` as function-like macros.
- Avoid deep nesting; use early returns and guard clauses.
- In compound `if` conditions, parenthesize each comparison explicitly — `if ((a == b) && (c < d))` — never rely on operator precedence.

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
