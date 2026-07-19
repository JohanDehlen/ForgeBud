"""
ForgeBud

Coding standards service.

Responsible for loading, validating, and saving the coding-standards
document stored in a project's ForgeBud memory.
"""

from __future__ import annotations

from pathlib import Path

from models.coding_standards import CodingStandards
from services.file_service import FileService


class CodingStandardsService:
    """
    Manages persistent coding standards for a project.
    """

    FORGEBUD_FOLDER = ".forgebud"
    CODING_STANDARDS_FILE = "coding_standards.md"

    @classmethod
    def load(
        cls,
        project_path: str | Path,
    ) -> CodingStandards:
        """
        Load a project's coding-standards document.

        Returns empty CodingStandards state when the document
        does not exist.
        """
        coding_standards_file = cls._coding_standards_path(
            project_path
        )

        if not coding_standards_file.exists():
            return CodingStandards()

        return CodingStandards(
            markdown=FileService.read_text(
                coding_standards_file
            )
        )

    @classmethod
    def save(
        cls,
        project_path: str | Path,
        coding_standards: CodingStandards,
    ) -> None:
        """
        Validate and save a project's coding standards.

        Raises ValueError when the coding-standards state is invalid.
        """
        errors = cls.validate(coding_standards)

        if errors:
            raise ValueError(
                "Coding standards cannot be saved: "
                + "; ".join(errors)
            )

        FileService.write_text(
            cls._coding_standards_path(project_path),
            cls._normalize_markdown(
                coding_standards.markdown
            ),
        )

    @classmethod
    def validate(
        cls,
        coding_standards: CodingStandards,
    ) -> list[str]:
        """
        Return validation errors for coding-standards state.
        """
        if not isinstance(
            coding_standards,
            CodingStandards,
        ):
            return [
                "Coding standards must be a "
                "CodingStandards instance."
            ]

        if not isinstance(coding_standards.markdown, str):
            return [
                "Coding standards Markdown must be a string."
            ]

        return []

    @classmethod
    def _coding_standards_path(
        cls,
        project_path: str | Path,
    ) -> Path:
        """
        Return the coding-standards document path.
        """
        return (
            Path(project_path)
            / cls.FORGEBUD_FOLDER
            / cls.CODING_STANDARDS_FILE
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