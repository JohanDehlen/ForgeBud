# ForgeBud Architectural Decisions

## Controller Architecture

Status: Accepted

Controllers coordinate application workflow.

Controllers do not contain business logic.

Business logic belongs in services.

Widgets never communicate directly with services.

---

## Widget Responsibilities

Status: Accepted

Widgets display data.

Widgets emit signals.

Widgets do not modify persistent project state.

---

## Models

Status: Accepted

Models represent application state.

Models contain no UI code.

Models remain serializable.

---

## Services

Status: Accepted

Services perform all business logic.

Services perform file I/O.

Services may be reused by multiple controllers.

---

## MainWindow

Status: Accepted

MainWindow is responsible only for application composition.

MainWindow delegates project lifecycle operations to
ProjectController.

MainWindow contains no project business logic.

---

## Release Manifest Backend

Status: Accepted

Release manifest data is stored as JSON at
`.forgebud/release_manifest.json`.

`ReleaseManifest` represents persistent release state and remains free
of service and UI dependencies.

`ReleaseManifestService` owns manifest validation, JSON loading, and
JSON saving.

An invalid manifest is rejected before it is written to disk.

The backend does not create an empty manifest during project
initialization because a valid release requires explicit version, goal,
and validation status.

---

## Project Dashboard State

Status: Accepted

`ProjectDashboard` composes ProjectInfo, ProjectContext, and
ReleaseManifest state for presentation.

ProjectController coordinates the existing services needed to build
dashboard state.

ProjectDashboardWidget only displays the supplied dashboard model.

MainWindow owns dashboard widget composition and forwards dashboard
state from the controller.

---

## Development Policy

Status: Accepted

Generate complete replacement files only.

Never generate snippets.

Never generate partial patches.

Every release must compile before proceeding.

Repository documents under `.forgebud/` are the source of truth.
