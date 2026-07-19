# Release Manifest

## Release

Version: **v0.8.0**

Name: **Project Summary**

Status: **Ready for Commit**

---

# Goal

Introduce managed Project Summary support so ForgeBud can create, load, display, edit, and persist concise project summaries stored in `.forgebud/project_summary.md`, while preserving the existing layered architecture and all current functionality.

---

# Files Added

* `models/project_summary.py`
* `services/project_summary_service.py`
* `widgets/project_summary_manager.py`

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

## Compilation

* Project Summary model compiled successfully.
* Project Summary service compiled successfully.
* Updated Project Service compiled successfully.
* Project Summary widget compiled successfully.
* Updated Project Controller compiled successfully.
* Updated MainWindow compiled successfully.
* Full project compilation passed.

## Runtime Validation

Verified successfully:

* Application starts without exceptions.
* Project Summary Manager appears correctly.
* The project-memory workspace displays four managers in a 2×2 grid.
* No project loaded results in a cleared and disabled Project Summary editor.
* Uninitialized projects also display a cleared and disabled editor.
* Initialized projects without `project_summary.md` load valid empty editable state.
* Saving creates `project_summary.md`.
* Saved project summaries reload correctly.
* Newly initialized projects receive a starter project-summary document.
* Existing project-summary documents are preserved.
* Current Task Manager continues to function.
* Decisions Manager continues to function.
* Coding Standards Manager continues to function.
* Dashboard remains functional.
* Recent-project support remains functional.
* Project initialization remains functional.

---

# Architectural Compliance

Verified.

* Controllers coordinate workflows.
* Services perform validation and persistence.
* Widgets display state and emit signals.
* Models contain state only.
* MainWindow owns UI composition only.

The new 2×2 project-memory layout is a user-interface improvement only and does not introduce a new architectural pattern.

---

# Release Notes

This release expands ForgeBud's managed project-memory system by introducing Project Summary support.

Projects can now maintain an editable Markdown summary describing their purpose, technology, intended users, current state, and important context. The summary is stored in `.forgebud/project_summary.md`, is created automatically for new projects, and is safely supported for existing projects that do not yet contain the document.

The project-memory workspace has also been reorganized into a 2×2 grid, allowing all four project-memory managers to remain comfortably usable.

---

# Known Issues

None.

---

# Release State

Implementation Complete

Compilation Passed

Runtime Validation Passed

Documentation Synchronized

Ready for Commit

Ready for Push

---

# Next Step

Commit the completed v0.8.0 release and push it to GitHub.

After the repository is synchronized, inspect `.forgebud/ROADMAP.md` to determine the next incomplete roadmap milestone before beginning v0.9.0.
