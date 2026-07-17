# Release Manifest

## Current Release

### Version

v0.4.0

### Goal

Implement an extensible Project Dashboard.

### Files Added

- `models/project_dashboard.py`
- `widgets/project_dashboard.py`

### Files Changed

- `controllers/project_controller.py`
- `main_window.py`

### Files Removed

None.

### Tests

The full project compiled successfully with:

```text
python -m compileall main.py main_window.py controllers models services widgets
```

### Release Notes

- Project metadata, Git context, and release metadata are combined in
  a dedicated dashboard state model.
- ProjectDashboardWidget displays dashboard state without using
  services or persistent storage.
- ProjectController coordinates dashboard state loading through the
  existing services.
- MainWindow composes the dashboard and forwards state to its widget.

### Known Issues

None recorded.

### Future Work

- Add refresh controls when dashboard update actions are introduced.
- Extend dashboard state with future project metadata and status
  features.
- Implement Current Task Manager support.

## Previous Release

### Version

v0.3.0

### Goal

Implement backend Release Manifest support.

### Files Added

- `models/release_manifest.py`
- `services/release_manifest_service.py`

### Validation

```text
python -m compileall models\release_manifest.py services\release_manifest_service.py
```

## Earlier Release

### Version

v0.2.0

### Goal

Implement complete Recent Projects support.

### Files Changed

- `services/settings_service.py`
- `controllers/project_controller.py`
- `widgets/project_panel.py`
- `main_window.py`

### Validation

```text
python -m compileall main_window.py controllers\project_controller.py services\settings_service.py widgets\project_panel.py
```
