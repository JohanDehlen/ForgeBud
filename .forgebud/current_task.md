# Current Task

## Active Release

Version: **v0.8.0**

Milestone: **Project Summary**

Status: **Release Specification Required**

---

# Summary

The v0.7.0 Coding Standards Manager release is complete.

Implementation, compilation, runtime validation, and project-memory documentation synchronization have been completed.

The next incomplete objective under Milestone 2 — Project Management is the Project Summary feature.

No v0.8.0 implementation may begin until a complete release specification has been created and all required implementation dependencies have been inspected.

---

# Previous Release

Version: **v0.7.0**

Name: **Coding Standards Manager**

Status: **Complete**

Completed work:

* Added the `CodingStandards` model.
* Added `CodingStandardsService`.
* Added `CodingStandardsManagerWidget`.
* Added coding-standards loading through `ProjectController`.
* Added coding-standards saving through `ProjectController`.
* Added Coding Standards Manager composition to `MainWindow`.
* Added default coding-standards creation during project initialization.
* Preserved existing coding-standards documents during initialization.
* Preserved existing project workflows.
* Passed full compilation.
* Passed runtime validation.
* Committed and pushed the implementation.
* Completed release documentation synchronization.

---

# Current Objective

Define the v0.8.0 Project Summary release.

The release must establish how ForgeBud represents, loads, displays, edits, and persists a concise project summary without violating the existing layered architecture.

The specification must determine:

* The persistent project-memory file used for the summary.
* The project-summary model and state fields.
* The service responsible for loading and saving the summary.
* The widget responsible for displaying and editing the summary.
* `ProjectController` coordination responsibilities.
* `MainWindow` composition and signal wiring.
* Project initialization behaviour.
* Behaviour for existing projects without a project-summary document.
* Validation requirements.
* The exact files to add, replace, or remove.

---

# Architectural Requirements

The release must preserve these responsibilities:

* Controllers coordinate workflows.
* Services perform business logic, validation, and persistence.
* Widgets display data and emit signals.
* Models contain application state only.
* MainWindow owns UI composition and delegates work.

Widgets must not access files or services directly.

MainWindow must not contain project-summary business logic.

Existing project-memory managers and all current workflows must remain functional.

---

# Required Inspection

Before generating implementation code, inspect the complete contents of every implementation file required by the Project Summary change.

At minimum, inspect the existing patterns used by:

* Current Task Manager
* Decisions Manager
* Coding Standards Manager
* Project initialization
* `ProjectController`
* `MainWindow`

Additional dependencies must be inspected when identified.

No code may be guessed from filenames, earlier versions, or incomplete search results.

---

# Development Sequence

1. Create the complete v0.8.0 release specification.
2. Inspect all implementation dependencies.
3. Determine the first implementation file.
4. Generate one complete replacement or new implementation file.
5. Compile the project.
6. Wait for compilation confirmation.
7. Continue one implementation file at a time.
8. Run full compilation and runtime validation.
9. Synchronize project-memory documents one file at a time.
10. Wait for the developer to commit and push.

---

# Immediate Next Step

Replace:

`.forgebud/PROJECT_STATE.md`
