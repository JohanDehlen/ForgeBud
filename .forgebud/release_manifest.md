# Release Manifest

## Release

Version: **v0.7.0**

Name: **Coding Standards Manager**

Status: **Documentation Synchronization**

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
* Current Task Manager remains functional.
* Decisions Manager remains functional.
* Dashboard remains functional.
* Project loading remains functional.
* Recent projects remain functional.

---

# Known Issues

None.

---

# Architectural Compliance

Verified.

* Controllers coordinate workflows.
* Services perform persistence and validation.
* Widgets present data only.
* Models contain application state only.
* MainWindow owns UI composition only.

No new architectural patterns were introduced.

---

# Release Notes

This release introduces the Coding Standards Manager, extending ForgeBud's project-memory system with editable coding standards stored in `.forgebud/coding_standards.md`. The implementation follows the same architecture used by the Release Manifest, Current Task, and Decisions managers, ensuring a consistent development model across all managed project documents.

---

# Future Work

Determine the next incomplete roadmap milestone after the documentation synchronization commit and begin the next release from a fresh specification.

---

# Release State

Implementation Complete

Compilation Passed

Runtime Validation Passed

Implementation Pushed

Documentation Synchronization In Progress
