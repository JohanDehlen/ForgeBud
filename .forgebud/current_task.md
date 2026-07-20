# Current Task

## Active Release

Version: **v0.9.0**

Milestone: **Milestone 2 — Project Management**

Objective: **Better Project Initialization**

Status: **Release Specification Complete — Inspection Required**

---

# Goal

Improve ForgeBud project initialization so the developer can review and provide project metadata before `.forgebud` project memory is created.

The current workflow initializes projects using automatically generated metadata with fixed defaults. This release will replace that implicit initialization with an explicit initialization form while preserving the existing project service, project-memory documents, recent-project workflow, dashboard, and layered architecture.

After this release, initializing a project will allow the developer to confirm or edit:

* Project name
* Initial version
* Description
* Programming language
* Framework
* Repository location

Initialization must remain safe, cancelable, and non-destructive.

---

# Current Behaviour

The current initialization workflow:

1. Opens a project folder.
2. Enables the Initialize ForgeBud action when the project is not initialized.
3. Creates `ProjectInfo` automatically in `ProjectController`.
4. Uses the folder name as the project name.
5. Uses fixed defaults for version, language, and framework.
6. Calls `ProjectService.initialize()`.
7. Creates `.forgebud/project.json`.
8. Creates missing default project-memory documents.
9. Preserves existing project-memory documents.
10. Reloads the initialized project.

The release must preserve all correct existing behaviour while improving metadata collection and validation.

---

# Required Behaviour

## Initialization Form

Selecting **Initialize ForgeBud** must open a dedicated initialization form.

The form must allow the developer to review and edit:

* Name
* Version
* Description
* Language
* Framework
* Repository

The form must be pre-populated using available project information.

Default values:

* Name: selected project folder name
* Version: `0.1.0`
* Description: empty
* Language: empty
* Framework: empty
* Repository: detected repository path or empty when the selected folder is not a Git repository

The user must be able to:

* Confirm initialization.
* Cancel initialization.
* Edit all displayed metadata before confirmation.

Canceling must leave the project unchanged.

---

# Metadata Validation

Initialization must reject invalid project metadata before writing any files.

Required validation:

* Project name must contain meaningful non-whitespace text.
* Version must contain meaningful non-whitespace text.
* All supplied metadata values must be strings.
* Leading and trailing whitespace must be normalized.
* Empty optional fields must remain valid.
* Invalid metadata must produce a clear user-facing message.
* No `.forgebud` files may be created when validation fails.

Validation belongs in the service layer.

Widgets must not perform project initialization or file access.

---

# Initialization Safety

The release must preserve the existing non-destructive initialization rules.

`ProjectService.initialize()` must:

* Create `.forgebud` when it does not exist.
* Write valid project metadata to `.forgebud/project.json`.
* Create each default project-memory document only when it does not exist.
* Never overwrite an existing project-memory document.
* Preserve existing project summary content.
* Preserve existing current-task content.
* Preserve existing engineering decisions.
* Preserve existing coding standards.
* Preserve all other existing default project-memory documents.
* Reject invalid `ProjectInfo` before writing any files.

The project must not be partially initialized when metadata validation fails.

---

# Architectural Responsibilities

## Model

`ProjectInfo` remains the persistent project metadata model.

It must:

* Contain state only.
* Remain serializable.
* Contain no validation workflow.
* Contain no file access.
* Contain no UI logic.

No new project-information model is required.

---

## Widget

A dedicated initialization dialog will collect project metadata.

The dialog must:

* Display editable project metadata fields.
* Accept initial `ProjectInfo` state.
* Return entered `ProjectInfo` state after confirmation.
* Allow cancellation without side effects.
* Contain no file access.
* Contain no service calls.
* Contain no project initialization workflow.
* Avoid owning persistence or business logic.

The dialog may manage presentation-level concerns such as field layout and button state.

---

## MainWindow

`MainWindow` will own initialization-dialog composition.

It will expose a controller-facing method that:

* Receives initial `ProjectInfo` state.
* Opens the initialization dialog.
* Returns confirmed `ProjectInfo` state.
* Returns no project information when the user cancels.

`MainWindow` must not:

* Validate project metadata as a business rule.
* Write project files.
* Call `ProjectService`.
* Perform project initialization.

---

## Controller

`ProjectController` will coordinate the initialization workflow.

It will:

1. Confirm that a project folder is open.
2. Build initial project-information state from the selected folder and repository state.
3. Ask the window to display the initialization form.
4. Stop without modifying the project when the user cancels.
5. Pass confirmed project information to `ProjectService.initialize()`.
6. Display validation errors returned by the service.
7. Reload the project after successful initialization.
8. Refresh recent projects, dashboard state, and all project-memory managers.
9. Display successful initialization status.

The controller must not perform direct project metadata file I/O.

---

## Services

`ProjectService` will continue to own project initialization and metadata persistence.

It will additionally own:

* Project-information validation.
* Metadata normalization.
* Protection against writing invalid metadata.
* Ensuring validation completes before initialization begins.

`GitService` remains read-only and may be used by the controller to determine repository information.

`FileService` remains responsible for filesystem operations.

---

# Files Added

* `widgets/project_initializer.py`

---

# Files Replaced

* `services/project_service.py`
* `controllers/project_controller.py`
* `main_window.py`

---

# Files Inspected but Not Planned for Replacement

* `models/project_info.py`
* `services/file_service.py`
* `services/git_service.py`
* `widgets/project_panel.py`

These files should remain unchanged unless dependency inspection reveals that the specified workflow cannot be implemented safely through their existing APIs.

Any scope change must be recorded in this release specification before implementation continues.

---

# Files Removed

None.

---

# Implementation Order

1. Re-read the complete `models/project_info.py`.
2. Re-read the complete `services/file_service.py`.
3. Re-read the complete `services/project_service.py`.
4. Re-read every direct caller of `ProjectService.initialize()`.
5. Replace `services/project_service.py`.
6. Compile `models/project_info.py`, `services/file_service.py`, and `services/project_service.py`.
7. Re-read relevant widget conventions.
8. Re-read the complete current `widgets/project_panel.py`.
9. Add `widgets/project_initializer.py`.
10. Compile the new widget and its model dependencies.
11. Re-read the complete `services/git_service.py`.
12. Re-read the complete `controllers/project_controller.py`.
13. Re-read the complete initialization-related `MainWindow` interface.
14. Replace `controllers/project_controller.py`.
15. Compile the controller and its direct dependencies.
16. Re-read the complete `main_window.py`.
17. Re-read the complete `widgets/project_initializer.py`.
18. Replace `main_window.py`.
19. Compile the complete project.
20. Launch ForgeBud.
21. Perform runtime and manual validation.
22. Update release documentation one file at a time.
23. Wait for commit and push.

---

# First Implementation File

The first implementation file to be replaced is:

`services/project_service.py`

It must be re-inspected immediately before generation.

No code may be generated until its complete direct dependencies and all callers of its initialization API have been inspected.

---

# Per-File Validation

After replacing `services/project_service.py`, compile:

```text
python -m py_compile models/project_info.py services/file_service.py services/project_service.py
```

After adding `widgets/project_initializer.py`, compile:

```text
python -m py_compile models/project_info.py widgets/project_initializer.py
```

After replacing `controllers/project_controller.py`, compile:

```text
python -m py_compile controllers/project_controller.py
```

After replacing `main_window.py`, run full compilation:

```text
python -m compileall main.py main_window.py controllers models services widgets
```

Every implementation file must compile before the next implementation file is generated.

---

# Runtime Validation

Launch:

```text
python main.py
```

Confirm that the application starts without an exception.

---

# Manual Validation

Confirm:

* Opening an uninitialized project enables Initialize ForgeBud.
* Selecting Initialize ForgeBud opens the initialization form.
* The project name defaults to the selected folder name.
* The version defaults to `0.1.0`.
* Optional metadata fields may be empty.
* Existing detected repository information is displayed when available.
* All metadata fields can be edited.
* Canceling closes the form without creating `.forgebud`.
* Confirming valid metadata initializes the project.
* Confirmed metadata is written correctly to `.forgebud/project.json`.
* Empty project names are rejected.
* Whitespace-only project names are rejected.
* Empty versions are rejected.
* Whitespace-only versions are rejected.
* Validation failures do not create `.forgebud`.
* Existing project-memory documents are not overwritten.
* Missing default project-memory documents are created.
* Existing project summaries are preserved.
* Existing current-task documents are preserved.
* Existing decisions documents are preserved.
* Existing coding-standards documents are preserved.
* The initialized project reloads automatically.
* The project panel displays the confirmed metadata.
* The dashboard refreshes correctly.
* Project Summary Manager remains functional.
* Current Task Manager remains functional.
* Decisions Manager remains functional.
* Coding Standards Manager remains functional.
* Recent-project workflows remain functional.
* Existing initialized projects continue to open normally.

---

# Completion Criteria

The release is complete when:

* The initialization form collects project metadata.
* Initialization can be canceled safely.
* Invalid metadata is rejected before filesystem changes occur.
* Valid metadata is normalized and persisted.
* Existing project-memory documents are preserved.
* Newly initialized projects receive all missing default documents.
* Project loading and recent-project workflows remain functional.
* All managed project-memory managers remain functional.
* Every changed implementation file compiles.
* Full compilation passes.
* Runtime validation passes.
* Manual validation passes.
* Release documentation is synchronized.
* The release is ready for commit and push.

---

# Documentation Updates After Implementation

Update one file at a time:

1. `.forgebud/PROJECT_STATE.md`
2. `.forgebud/current_task.md`
3. `.forgebud/release_manifest.md`
4. `.forgebud/decisions.md` only if an architectural decision changes

No architectural change is currently planned.

---

# Immediate Next Step

Inspect the complete current versions of:

* `models/project_info.py`
* `services/file_service.py`
* `services/project_service.py`
* Every direct caller of `ProjectService.initialize()`

Then re-inspect `services/project_service.py` immediately before generating its complete replacement.

Generate exactly one implementation file:

`services/project_service.py`
