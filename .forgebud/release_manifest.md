# Release Manifest

## Current Release

### Version

v0.3.0

### Goal

Implement backend Release Manifest support.

### Files Added

- `models/release_manifest.py`
- `services/release_manifest_service.py`

### Files Changed

None.

### Files Removed

None.

### Tests

The release files compiled successfully with:

```text
python -m compileall models\release_manifest.py services\release_manifest_service.py
```

The full project also compiled successfully with:

```text
python -m compileall main.py main_window.py controllers models services widgets
```

### Release Notes

- Release manifest data is represented by a serializable model.
- Manifest data is stored as JSON at
  `.forgebud/release_manifest.json`.
- The service validates the manifest structure before saving.
- Loading reports invalid JSON and invalid manifest structures.
- The backend has no UI dependency and is ready for future release
  automation.

### Known Issues

None recorded.

### Future Work

- Add controller workflows for creating and updating releases.
- Add release manifest UI after the backend workflow is defined.
- Implement Project Dashboard improvements.

## Previous Release

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
