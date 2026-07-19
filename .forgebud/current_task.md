# Current Task

## Active Release

Version: **v0.8.0**

Milestone: **Project Summary**

Status: **Specification Complete**

---

# Goal

Implement managed project-summary support so ForgeBud can create, load, display, edit, and save a concise description of an initialized software project.

The project summary will be stored in:

`.forgebud/project_summary.md`

The summary should help a developer or AI quickly understand:

* Why the project exists.
* What the project does.
* Who or what it is intended for.
* Which technologies it uses.
* Its current development state.
* Important constraints or context.

The release must preserve all existing functionality and follow ForgeBud's layered architecture.

---

# Requirements

* Create a dedicated project-summary state model.
* Create a dedicated project-summary persistence service.
* Create a presentation-only Project Summary Manager widget.
* Load the project summary when an initialized project is opened.
* Save the project summary through `ProjectController`.
* Create `.forgebud/project_summary.md` during new project initialization.
* Never overwrite an existing project-summary document during initialization.
* Treat an absent summary document in an existing project as valid empty state.
* Disable project-summary editing when no initialized project is open.
* Enable project-summary editing when an initialized project is open.
* Preserve all existing project-memory managers and application workflows.
* Keep persistence and business logic out of widgets and `MainWindow`.

---

# Persistent Document

## Path

`.forgebud/project_summary.md`

## Format

UTF-8 Markdown.

## Ownership

The summary belongs to the project.

ForgeBud may provide a starter document during initialization, but the content remains editable and project-owned.

---

# Planned Files Added

* `models/project_summary.py`
* `services/project_summary_service.py`
* `widgets/project_summary_manager.py`

---

# Planned Files Replaced

* `services/project_service.py`
* `controllers/project_controller.py`
* `main_window.py`

---

# Planned Files Removed

None.

---

# Model

## `ProjectSummary`

The model represents persistent project-summary state.

State:

* `markdown: str`

Convenience behavior:

* `is_empty` returns whether the document contains meaningful text.

The model must:

* Remain serializable.
* Contain state only.
* Contain no file access.
* Contain no UI code.
* Contain no service dependencies.
* Contain no workflow logic.

---

# Service

## `ProjectSummaryService`

The service owns:

* Project-summary path construction.
* Markdown loading.
* Model validation.
* Markdown normalization.
* Markdown saving.

Expected behavior:

* `load()` returns empty `ProjectSummary` state when the file does not exist.
* `save()` validates the supplied model before writing.
* Saved non-empty Markdown ends with exactly one trailing newline.
* Empty Markdown may be persisted as an empty document.
* The service uses `FileService` for file access.

The service must not access widgets or controllers.

---

# Widget

## `ProjectSummaryManagerWidget`

The widget displays and edits project-summary Markdown.

The widget must:

* Use a plain-text Markdown editor.
* Display a clear Project Summary heading.
* Provide a Save Project Summary action.
* Emit the current Markdown through a signal.
* Provide explicit methods to set and clear state.
* Provide explicit methods to enable and disable editing.
* Start cleared and disabled.
* Contain no file access.
* Contain no service calls.
* Contain no project workflow logic.

---

# Controller

## `ProjectController`

The controller will coordinate:

* Loading project-summary state.
* Saving project-summary state.
* Refreshing the summary when a project is opened.
* Refreshing the summary after project initialization.
* Clearing and disabling the summary for uninitialized projects.
* Enabling editing for initialized projects.
* Displaying validation failures through the window interface.
* Displaying save status messages.

The controller must use `ProjectSummaryService` for persistence.

The controller must not perform direct project-summary file I/O.

---

# MainWindow

`MainWindow` will:

* Create `ProjectSummaryManagerWidget`.
* Add it to the project-memory workspace.
* Connect its save signal to `ProjectController.save_project_summary`.
* Forward `ProjectSummary` state from the controller to the widget.
* Expose controller-facing methods for:

  * setting the summary,
  * clearing the summary,
  * enabling editing,
  * disabling editing.

`MainWindow` must contain no project-summary business logic.

---

# Project Initialization

`ProjectService` will add `project_summary.md` to its default project-memory documents.

Initialization behavior:

* Create the file only when it does not exist.
* Never replace an existing summary.
* Preserve all existing initialization behavior.
* Use a useful starter Markdown document.

---

# Default Project Summary Document

Newly initialized projects should receive:

```markdown
# Project Summary

## Purpose

Describe why this project exists.

## What It Does

Describe the primary functionality of the project.

## Intended Users

Describe who or what the project is designed for.

## Technology

Document the primary language, framework, platform, and important dependencies.

## Current State

Describe the project's present development state.

## Important Context

Record constraints, assumptions, or background information needed to understand the project.
```

This document remains editable and project-owned.

---

# Existing Project Compatibility

Existing initialized projects may not contain:

`.forgebud/project_summary.md`

This is valid.

For those projects:

* Loading returns empty project-summary state.
* The editor is enabled because the project is initialized.
* Saving creates the missing document.
* No migration step is required.
* No unrelated project-memory document is changed.

---

# UI Composition

The project-memory area currently contains:

* Current Task Manager
* Decisions Manager
* Coding Standards Manager

Project Summary Manager must be added without removing or disabling existing managers.

The exact layout must be chosen after inspecting the complete current `main_window.py`.

The layout should remain usable at the existing window size and should avoid making editors unreasonably narrow.

---

# Validation

## Per-file validation

Each implementation file must compile before moving to the next file.

## Full compilation

```text
python -m compileall main.py main_window.py controllers models services widgets
```

## Runtime validation

```text
python main.py
```

## Manual validation

Confirm:

* ForgeBud opens without an exception.
* Project Summary Manager appears.
* No project open results in a cleared and disabled editor.
* An uninitialized project results in a cleared and disabled editor.
* An initialized project without `project_summary.md` loads empty editable state.
* Saving creates `project_summary.md`.
* Existing project-summary content loads correctly.
* Edited content saves correctly.
* Reopening the project restores saved content.
* New project initialization creates the starter summary.
* Existing summary content is not overwritten.
* Current Task Manager still works.
* Decisions Manager still works.
* Coding Standards Manager still works.
* Dashboard still works.
* Recent-project workflows still work.
* Project initialization still works.

---

# Implementation Order

1. Inspect all existing model conventions.
2. Add `models/project_summary.py`.
3. Compile the model.
4. Inspect all persistence-service dependencies.
5. Add `services/project_summary_service.py`.
6. Compile the model and service.
7. Re-read the complete `services/project_service.py`.
8. Replace `services/project_service.py`.
9. Compile the project service and dependencies.
10. Inspect all relevant widget conventions.
11. Add `widgets/project_summary_manager.py`.
12. Compile the model, services, and widget.
13. Re-read the complete `controllers/project_controller.py` and direct dependencies.
14. Replace `controllers/project_controller.py`.
15. Compile the controller and dependencies.
16. Re-read the complete `main_window.py` and direct widget APIs.
17. Replace `main_window.py`.
18. Compile the complete project.
19. Launch ForgeBud.
20. Perform manual validation.
21. Update project-memory release documents one file at a time.
22. Wait for commit and push.

---

# Completion Criteria

The release is complete when:

* All planned implementation files are generated one at a time.
* Every implementation file compiles before proceeding.
* Full compilation passes.
* Runtime validation passes.
* Project-summary loading works.
* Project-summary saving works.
* New initialization creates the starter document.
* Existing summary documents are preserved.
* Existing projects without a summary remain supported.
* All previous functionality remains operational.
* Project-memory documents are synchronized.
* The release is ready for commit and push.

---

# Immediate Next Step

Inspect the complete existing model implementations and generate exactly one new file:

`models/project_summary.py`
