"""
ForgeBud

Project summary service.

Responsible for loading, validating, and saving the project-summary
document stored in a project's ForgeBud memory.
"""

from __future__ import annotations

from pathlib import Path

from models.project_summary import ProjectSummary
from services.file_service import FileService


class ProjectSummaryService:
    """
    Manages persistent project-summary data for a project.
    """

    FORGEBUD_FOLDER = ".forgebud"
    PROJECT_SUMMARY_FILE = "project_summary.md"

    @classmethod
    def load(
        cls,
        project_path: str | Path,
    ) -> ProjectSummary:
        """
        Load a project's project-summary document.

        Returns empty ProjectSummary state when the document
        does not exist.
        """
        project_summary_file = cls._project_summary_path(
            project_path
        )

        if not project_summary_file.exists():
            return ProjectSummary()

        return ProjectSummary(
            markdown=FileService.read_text(
                project_summary_file
            )
        )

    @classmethod
    def save(
        cls,
        project_path: str | Path,
        project_summary: ProjectSummary,
    ) -> None:
        """
        Validate and save a project's project summary.

        Raises ValueError when project-summary state is invalid.
        """
        errors = cls.validate(project_summary)

        if errors:
            raise ValueError(
                "Project summary cannot be saved: "
                + "; ".join(errors)
            )

        FileService.write_text(
            cls._project_summary_path(project_path),
            cls._normalize_markdown(
                project_summary.markdown
            ),
        )

    @classmethod
    def validate(
        cls,
        project_summary: ProjectSummary,
    ) -> list[str]:
        """
        Return validation errors for project-summary state.
        """
        if not isinstance(
            project_summary,
            ProjectSummary,
        ):
            return [
                "Project summary must be a "
                "ProjectSummary instance."
            ]

        if not isinstance(project_summary.markdown, str):
            return [
                "Project summary Markdown must be a string."
            ]

        return []

    @classmethod
    def _project_summary_path(
        cls,
        project_path: str | Path,
    ) -> Path:
        """
        Return the project-summary document path.
        """
        return (
            Path(project_path)
            / cls.FORGEBUD_FOLDER
            / cls.PROJECT_SUMMARY_FILE
        )

    @staticmethod
    def _normalize_markdown(markdown: str) -> str:
        """
        Normalize Markdown before it is written to disk.
        """
        normalized = markdown.rstrip()

        if not normalized:
            return ""

        return normalized + "\n"