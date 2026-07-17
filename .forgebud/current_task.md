# Current Task

## Release Specification

Version: v0.2.0

Milestone: Recent Projects

Status: Complete

## Objective

Implement complete Recent Projects support so ForgeBud remembers
recently opened project folders and allows the user to reopen them
from the application UI.

## Requirements

- Persist recent project folders in `config/settings.json`.
- Remove duplicate entries and keep the newest project first.
- Limit the list to 10 entries.
- Ignore nonexistent project folders.
- Update the list when a project is opened or initialized.
- Populate the Recent Projects widget through `ProjectController`.
- Reopen a selected recent project through the existing project-loading
  workflow.
- Preserve the layered architecture:
  - Controllers coordinate.
  - Services perform work.
  - Widgets display data.
  - Models contain state.
  - MainWindow contains no business logic.

## Files Changed

- `services/settings_service.py`
- `controllers/project_controller.py`
- `widgets/project_panel.py`
- `main_window.py`

## Validation

The changed Python files compiled successfully with:

```text
python -m compileall main_window.py controllers\project_controller.py services\settings_service.py widgets\project_panel.py
```

## Next Task

Implement Release Manifest support.
