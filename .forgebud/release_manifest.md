# Release Manifest

## Release

Version: **v0.7.0**

Name: **Coding Standards Manager**

Status: **Complete**

---

# Goal

Add persistent management of project-specific coding standards stored in `.forgebud/coding_standards.md` while preserving ForgeBud's layered architecture and all existing functionality.

---

# Files Added

* `models/coding_standards.py`
* `services/coding_standards_service.py`
* `widgets/coding_standards_manager.py`

---

# Files Modified

* `services/project_service.py`
* `controllers/project_controller.py`
* `main_window.py`
* `.forgebud/PROJECT_STATE.md`
* `.forgebud/current_task.md`
* `.forgebud/release_manifest.md`

---

# Files Removed

None.

---

# Validation

Compilation:

* Passed

Application Startup:

* Passed

Manual Validation:

* Coding Standards Manager loads correctly.
* Coding standards save correctly.
* Coding standards reload correctly.
* Existing projects without `coding_standards.md` remain supported.
* Newly initialized projects receive a default coding-standards document.
* Existing coding-standards documents are preserved.
* Editing remains disabled for uninitialized projects.
* Current Task Manager remains functional.
* Decisions Manager remains functional.
* Dashboard remains functional.
* Project loading remains functional.
* Recent projects remain functional.
* Project initialization remains functional.

---

# Known Issues

None.

---

# Architectural Compliance

Verified.

* Controllers coordinate workflows.
* Services perform persistence and validation.
* Widgets display data and emit user actions.
* Models contain application state only.
* MainWindow owns UI composition and delegates work.

No new architectural patterns were introduced.

`.forgebud/decisions.md` therefore remains unchanged.

---

# Release Notes

This release introduces the Coding Standards Manager, extending ForgeBud's project-memory system with editable project-specific coding standards stored in `.forgebud/coding_standards.md`.

The release adds a dedicated coding-standards model, persistence service, and manager widget. Loading and saving are coordinated through `ProjectController`, while `MainWindow` owns widget composition and signal wiring.

Newly initialized projects receive a default coding-standards document. Existing coding-standards documents are preserved, and projects that do not yet contain the document remain supported.

The implementation follows the same layered architecture used by the Release Manifest, Current Task, and Decisions managers.

---

# Future Work

The next incomplete objective under Milestone 2 — Project Management is:

**Project Summary**

The next release must begin with a complete release specification before implementation starts.

---

# Release State

Implementation Complete

Compilation Passed

Runtime Validation Passed

Implementation Committed and Pushed

Documentation Synchronization Complete

Release Complete
