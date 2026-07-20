# Release Manifest

## Release

Version: **v0.9.0**

Name: **Better Project Initialization**

Status: **Ready for Commit**

---

# Goal

Replace the one-click initialization workflow with a guided initialization dialog that collects project metadata before creating the ForgeBud project, while preserving the existing layered architecture and all current functionality.

---

# Files Added

- `widgets/project_initializer.py`

---

# Files Modified

- `services/project_service.py`
- `controllers/project_controller.py`
- `main_window.py`

---

# Files Updated During Release Documentation

- `.forgebud/PROJECT_STATE.md`
- `.forgebud/current_task.md`
- `.forgebud/release_manifest.md`

---

# Files Removed

None.

---

# Validation

## Compilation

- Project Service compiled successfully.
- Project Controller compiled successfully.
- MainWindow compiled successfully.
- Project Initializer dialog compiled successfully.
- Full project compilation passed.

## Runtime Validation

Verified successfully:

- Application starts without exceptions.
- Initialization dialog opens correctly.
- Project metadata is pre-populated.
- Description, language, framework, and version are editable.
- Repository path is detected correctly.
- Successful initialization creates `.forgebud`.
- Project metadata is saved correctly.
- Project reloads automatically after initialization.
- Dashboard displays updated project metadata.
- Project panel displays updated project metadata.
- Project-memory documents are created correctly.
- Existing project-memory documents remain protected.

## Cancellation

Verified successfully:

- Cancel closes the dialog.
- No `.forgebud` directory is created.
- No project files are written.

## Validation

Verified successfully:

- Blank project names rejected.
- Whitespace-only project names rejected.
- Blank versions rejected.
- Whitespace-only versions rejected.
- Invalid submissions create no project files.

---

# Architectural Compliance

Verified.

- Controllers coordinate workflows.
- Services validate, normalize, and persist data.
- Widgets collect and display presentation state.
- Models contain state only.
- MainWindow owns UI composition and dialog presentation.

---

# Release Notes

This release significantly improves the ForgeBud initialization experience.

Instead of immediately creating project files, ForgeBud now presents a dedicated initialization dialog where developers can review and complete project metadata before initialization begins.

Project metadata is validated and normalized before any filesystem changes occur. Initialization can be safely cancelled without creating a `.forgebud` directory, and invalid metadata is rejected before project files are written.

Successful initialization automatically reloads the project and refreshes the dashboard and all project-memory managers.

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

Commit the completed v0.9.0 release and push it to GitHub.

After the repository is synchronized, re-read every document in `.forgebud`, inspect the roadmap, determine the next incomplete milestone, and create the next release specification before implementation begins.