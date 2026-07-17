# Release Manifest

## Version

v0.2.0

## Goal

Implement complete Recent Projects support.

## Files Added

None.

## Files Changed

- `services/settings_service.py`
- `controllers/project_controller.py`
- `widgets/project_panel.py`
- `main_window.py`

## Files Removed

None.

## Tests

The release files compiled successfully with:

```text
python -m compileall main_window.py controllers\project_controller.py services\settings_service.py widgets\project_panel.py
```

## Release Notes

- Recent project folders are stored in `config/settings.json`.
- Duplicate folders are removed and the newest folder is listed first.
- The recent-project list is limited to 10 valid project folders.
- Nonexistent project folders are excluded from the list.
- Selecting a recent project opens it through `ProjectController`.

## Known Issues

None recorded.

## Future Work

- Implement Release Manifest support in the ForgeBud application.
- Add Project Dashboard improvements.
- Add Current Task Manager support.
