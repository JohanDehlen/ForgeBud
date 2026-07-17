"""
ForgeBud

Project dashboard widget.

Displays the current project, repository, and release information.
"""

from PySide6.QtWidgets import (
    QFormLayout,
    QFrame,
    QLabel,
    QVBoxLayout,
    QWidget,
)

from models.project_dashboard import ProjectDashboard


class ProjectDashboardWidget(QWidget):
    """
    Displays the current ProjectDashboard state.
    """

    def __init__(self) -> None:
        super().__init__()

        main_layout = QVBoxLayout(self)

        title_label = QLabel("Project Dashboard")
        main_layout.addWidget(title_label)

        self._create_project_section(main_layout)
        self._add_separator(main_layout)
        self._create_repository_section(main_layout)
        self._add_separator(main_layout)
        self._create_release_section(main_layout)

        main_layout.addStretch()

        self.clear()

    def _create_project_section(
        self,
        main_layout: QVBoxLayout,
    ) -> None:
        """
        Create the project information section.
        """
        form = QFormLayout()

        self.projectLabel = QLabel("-")
        self.descriptionLabel = QLabel("-")
        self.pathLabel = QLabel("-")
        self.initializationLabel = QLabel("-")

        form.addRow("Project", self.projectLabel)
        form.addRow("Description", self.descriptionLabel)
        form.addRow("Path", self.pathLabel)
        form.addRow("ForgeBud", self.initializationLabel)

        main_layout.addLayout(form)

    def _create_repository_section(
        self,
        main_layout: QVBoxLayout,
    ) -> None:
        """
        Create the repository information section.
        """
        form = QFormLayout()

        self.repositoryLabel = QLabel("-")
        self.branchLabel = QLabel("-")
        self.lastCommitLabel = QLabel("-")
        self.changedFilesLabel = QLabel("-")
        self.untrackedFilesLabel = QLabel("-")

        form.addRow("Repository", self.repositoryLabel)
        form.addRow("Branch", self.branchLabel)
        form.addRow("Last Commit", self.lastCommitLabel)
        form.addRow("Changed Files", self.changedFilesLabel)
        form.addRow("Untracked Files", self.untrackedFilesLabel)

        main_layout.addLayout(form)

    def _create_release_section(
        self,
        main_layout: QVBoxLayout,
    ) -> None:
        """
        Create the release information section.
        """
        form = QFormLayout()

        self.releaseVersionLabel = QLabel("-")
        self.validationStatusLabel = QLabel("-")

        form.addRow("Release Version", self.releaseVersionLabel)
        form.addRow("Validation", self.validationStatusLabel)

        main_layout.addLayout(form)

    def _add_separator(
        self,
        main_layout: QVBoxLayout,
    ) -> None:
        """
        Add a horizontal separator to the dashboard.
        """
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)

        main_layout.addWidget(separator)

    def set_dashboard(
        self,
        dashboard: ProjectDashboard,
    ) -> None:
        """
        Display the supplied project dashboard state.
        """
        project_info = dashboard.project_info
        project_context = dashboard.project_context
        release_manifest = dashboard.release_manifest

        self.projectLabel.setText(
            project_info.display_name or "-"
        )
        self.descriptionLabel.setText(
            project_info.description or "-"
        )
        self.pathLabel.setText(
            project_context.project_path or "-"
        )
        self.initializationLabel.setText(
            "Initialized"
            if dashboard.is_initialized
            else "Not initialized"
        )

        self.repositoryLabel.setText(
            "Git Repository"
            if project_context.is_repository
            else "Not a Git repository"
        )
        self.branchLabel.setText(
            project_context.branch or "-"
        )
        self.lastCommitLabel.setText(
            project_context.last_commit or "-"
        )
        self.changedFilesLabel.setText(
            str(project_context.modified_count)
        )
        self.untrackedFilesLabel.setText(
            str(project_context.untracked_count)
        )

        self.releaseVersionLabel.setText(
            release_manifest.version or "-"
        )
        self.validationStatusLabel.setText(
            release_manifest.validation_status or "-"
        )

    def clear(self) -> None:
        """
        Clear all displayed dashboard values.
        """
        self.projectLabel.setText("-")
        self.descriptionLabel.setText("-")
        self.pathLabel.setText("-")
        self.initializationLabel.setText("-")

        self.repositoryLabel.setText("-")
        self.branchLabel.setText("-")
        self.lastCommitLabel.setText("-")
        self.changedFilesLabel.setText("-")
        self.untrackedFilesLabel.setText("-")

        self.releaseVersionLabel.setText("-")
        self.validationStatusLabel.setText("-")