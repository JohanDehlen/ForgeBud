from __future__ import annotations

from pathlib import Path
from typing import Protocol

from models.project_dashboard import ProjectDashboard
from models.project_info import ProjectInfo
from services.context_service import ContextService
from services.git_service import GitService
from services.project_service import ProjectService
from services.release_manifest_service import (
    ReleaseManifestService,
)
from services.settings_service import SettingsService


class ProjectWindow(Protocol):
    """
    Defines the UI operations required by ProjectController.
    """

    def show_status(self, message: str) -> None:
        """
        Display an application status message.
        """

    def select_project_folder(self) -> str:
        """
        Ask the user to select a project folder.
        """

    def show_information(self, title: str, message: str) -> None:
        """
        Display an informational message dialog.
        """

    def set_project(self, info: ProjectInfo) -> None:
        """
        Display project metadata.
        """

    def clear_project(self) -> None:
        """
        Clear displayed project metadata.
        """

    def set_repository_status(self, text: str) -> None:
        """
        Display the repository status.
        """

    def set_project_dashboard(
        self,
        dashboard: ProjectDashboard,
    ) -> None:
        """
        Display project dashboard state.
        """

    def enable_initialize(self) -> None:
        """
        Enable project initialization.
        """

    def disable_initialize(self) -> None:
        """
        Disable project initialization.
        """

    def set_recent_projects(
        self,
        project_paths: list[str],
    ) -> None:
        """
        Display recent project folders.
        """


class ProjectController:
    """
    Coordinates project selection, loading, initialization,
    dashboard state, and recent-project presentation.
    """

    def __init__(self, window: ProjectWindow) -> None:
        self._window = window
        self._project_path: Path | None = None

    def open_project(self) -> None:
        """
        Ask the user to select and load a project folder.
        """
        folder = self._window.select_project_folder()

        if not folder:
            return

        self.load_project(folder)

    def open_recent_project(self, folder: str) -> None:
        """
        Load a project selected from the recent-projects list.
        """
        if not Path(folder).is_dir():
            self.refresh_recent_projects()
            return

        self.load_project(folder)

    def load_project(self, folder: str | Path) -> None:
        """
        Load project, repository, and dashboard information.
        """
        project_path = Path(folder)

        if not project_path.is_dir():
            return

        self._project_path = project_path
        SettingsService.add_recent_project(self._project_path)
        self.refresh_recent_projects()

        self._window.show_status(
            f"Opened project: {self._project_path.name}"
        )
        self._update_repository_status()

        if ProjectService.is_initialized(self._project_path):
            self._load_initialized_project()
        else:
            self._show_uninitialized_project()

        self.refresh_project_dashboard()

    def initialize_project(self) -> None:
        """
        Initialize the currently opened project for ForgeBud.
        """
        if self._project_path is None:
            self._window.show_information(
                "No Project",
                "Please open a project first.",
            )
            return

        ProjectService.initialize(
            self._project_path,
            self._create_project_info(),
        )

        SettingsService.add_recent_project(self._project_path)
        self.refresh_recent_projects()
        self.load_project(self._project_path)

        self._window.show_information(
            "ForgeBud",
            "Project initialized successfully.",
        )
        self._window.show_status(
            "Project initialized successfully."
        )

    def refresh_recent_projects(self) -> None:
        """
        Load valid recent projects and display them through the UI.
        """
        self._window.set_recent_projects(
            SettingsService.get_recent_projects()
        )

    def refresh_project_dashboard(self) -> None:
        """
        Build and display the current project dashboard state.
        """
        if self._project_path is None:
            self._window.set_project_dashboard(
                ProjectDashboard()
            )
            return

        is_initialized = ProjectService.is_initialized(
            self._project_path
        )

        project_info = ProjectInfo()

        if is_initialized:
            project_info = ProjectService.load(
                self._project_path
            )

        dashboard = ProjectDashboard(
            project_info=project_info,
            project_context=ContextService.build(
                str(self._project_path)
            ),
            release_manifest=ReleaseManifestService.load(
                self._project_path
            ),
            is_initialized=is_initialized,
        )

        self._window.set_project_dashboard(dashboard)

    def _update_repository_status(self) -> None:
        """
        Load and display the current Git repository status.
        """
        if not GitService.is_repository(self._project_path):
            self._window.set_repository_status(
                "Not a Git repository"
            )
            return

        branch = GitService.current_branch(self._project_path)

        self._window.set_repository_status(
            f"Git Repository ({branch})"
        )

    def _load_initialized_project(self) -> None:
        """
        Load metadata for an initialized ForgeBud project.
        """
        info = ProjectService.load(self._project_path)

        self._window.set_project(info)
        self._window.disable_initialize()
        self._window.show_status("ForgeBud project loaded.")

    def _show_uninitialized_project(self) -> None:
        """
        Display the state of a project that is not initialized.
        """
        self._window.clear_project()
        self._window.set_repository_status(
            "Project not initialized"
        )
        self._window.enable_initialize()
        self._window.show_status(
            "Project ready for initialization."
        )

    def _create_project_info(self) -> ProjectInfo:
        """
        Create initial metadata for the current project.
        """
        return ProjectInfo(
            name=self._project_path.name,
            version="0.1.0",
            description="",
            language="Python",
            framework="Unknown",
        )