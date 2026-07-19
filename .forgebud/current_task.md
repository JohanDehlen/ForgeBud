# Current Task

## Active Release

Version: **v0.7.0**

Milestone: **Coding Standards Manager**

Status: **Specification Complete**

---

# Goal

Implement a Coding Standards Manager that allows ForgeBud to create, load, display, edit, and save project-specific coding standards stored in:

`.forgebud/coding_standards.md`

The release must preserve all existing functionality and remain consistent with ForgeBud's layered architecture.

---

# Requirements

* Create a dedicated coding-standards state model.
* Create a dedicated coding-standards persistence service.
* Create a presentation-only Coding Standards Manager widget.
* Load coding standards when an initialized project is opened.
* Save coding standards through ProjectController.
* Create `.forgebud/coding_standards.md` during project initialization.
* Disable coding-standards editing when no initialized project is open.
* Enable editing when an initialized project is open.
* Preserve Current Task Manager functionality.
* Preserve Decisions Manager functionality.
* Preserve the Project Dashboard.
* Preserve recent-project and initialization workflows.
* Do not place persistence or business logic in widgets or MainWindow.

---

# Planned Files Added

* `models/coding_standards.py`
* `services/coding_standards_service.py`
* `widgets/coding_standards_manager.py`

---

# Planned Files Replaced

* `services/project_service.py`
* `controllers/project_controller.py`
* `main_window.py`

---

# Planned Files Removed

None.

---

# Architecture

## Model

`CodingStandards` contains coding-standards state only.

The model must:

* Remain serializable.
* Contain no UI code.
* Contain no file access.
* Contain no service dependencies.

## Service

`CodingStandardsService` owns:

* Coding-standards path construction.
* Markdown loading.
* State validation.
* Markdown normalization.
* Markdown saving.

## Widget

`CodingStandardsManagerWidget`:

* Displays editable Markdown.
* Emits save requests.
* Does not access services.
* Does not read or write files.

## Controller

`ProjectController`:

* Coordinates coding-standards loading.
* Coordinates coding-standards saving.
* Controls enabled and disabled UI state.
* Does not perform file I/O directly.

## MainWindow

`MainWindow`:

* Owns widget composition.
* Connects widget signals.
* Forwards model state between the controller and widget.
* Contains no project business logic.

## Project Initialization

`ProjectService` creates a default `.forgebud/coding_standards.md` document for newly initialized projects without overwriting an existing document.

---

# Default Coding Standards Document

Newly initialized projects should receive a useful starter document containing sections for:

* General principles
* Language and framework conventions
* Naming
* Type hints
* Functions and classes
* Error handling
* Documentation
* Testing
* Dependencies
* Project-specific rules

The document must remain editable and project-owned.

---

# Implementation Order

1. Add `models/coding_standards.py`.
2. Compile the new model.
3. Add `services/coding_standards_service.py`.
4. Compile the model and service.
5. Replace `services/project_service.py`.
6. Compile the project service and dependencies.
7. Add `widgets/coding_standards_manager.py`.
8. Compile the model, services, and widget.
9. Replace `controllers/project_controller.py`.
10. Compile the controller and dependencies.
11. Replace `main_window.py`.
12. Compile the complete application.
13. Launch the application and perform manual validation.
14. Update release documentation.

---

# Validation

Each generated implementation file must compile before proceeding to the next file.

Final compilation:

```text
python -m compileall main.py main_window.py controllers models services widgets
```

Runtime validation:

```text
python main.py
```

Manual validation must confirm:

* ForgeBud launches without an exception.
* Existing initialized projects without `coding_standards.md` load with empty coding-standards state.
* Newly initialized projects receive `.forgebud/coding_standards.md`.
* Existing coding-standards documents are not overwritten during initialization.
* Coding standards load correctly.
* Coding standards save correctly.
* Editing is disabled for uninitialized projects.
* Current Task Manager remains functional.
* Decisions Manager remains functional.
* Dashboard and recent-project workflows remain functional.

---

# Completion Criteria

The release is complete when:

* All planned files have been generated one at a time.
* Each implementation file compiles before proceeding.
* The complete application compiles.
* Runtime validation passes.
* Coding standards load and save successfully.
* New project initialization creates the document safely.
* Existing functionality remains intact.
* Project-memory release documents are updated.
* The release is ready for commit and push.

---

# Immediate Next Step

Inspect all existing model conventions and generate one new complete file:

`models/coding_standards.py`
