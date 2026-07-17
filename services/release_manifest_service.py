"""
ForgeBud

Release manifest service.

Responsible for validating, loading, and saving release manifests.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from models.release_manifest import ReleaseManifest
from services.file_service import FileService


class ReleaseManifestService:
    """
    Manages persistent release manifest data for a project.
    """

    FORGEBUD_FOLDER = ".forgebud"
    MANIFEST_FILE = "release_manifest.json"

    @classmethod
    def load(
        cls,
        project_path: str | Path,
    ) -> ReleaseManifest:
        """
        Load a project's release manifest.

        Returns an empty manifest when no JSON manifest exists.
        Raises ValueError when an existing manifest is invalid.
        """
        manifest_file = cls._manifest_path(project_path)

        if not manifest_file.exists():
            return ReleaseManifest()

        try:
            data = json.loads(
                FileService.read_text(manifest_file)
            )
        except json.JSONDecodeError as error:
            raise ValueError(
                "Release manifest contains invalid JSON."
            ) from error

        if not isinstance(data, dict):
            raise ValueError(
                "Release manifest must contain a JSON object."
            )

        try:
            manifest = ReleaseManifest(**data)
        except TypeError as error:
            raise ValueError(
                "Release manifest has an unsupported structure."
            ) from error

        errors = cls.validate(manifest)

        if errors:
            raise ValueError(
                "Release manifest is invalid: "
                + "; ".join(errors)
            )

        return manifest

    @classmethod
    def save(
        cls,
        project_path: str | Path,
        manifest: ReleaseManifest,
    ) -> None:
        """
        Validate and save a project's release manifest.

        Raises ValueError when the manifest structure is invalid.
        """
        errors = cls.validate(manifest)

        if errors:
            raise ValueError(
                "Release manifest cannot be saved: "
                + "; ".join(errors)
            )

        manifest_file = cls._manifest_path(project_path)

        FileService.write_text(
            manifest_file,
            json.dumps(
                asdict(manifest),
                indent=4,
                ensure_ascii=False,
            ),
        )

    @classmethod
    def validate(
        cls,
        manifest: ReleaseManifest,
    ) -> list[str]:
        """
        Return structure validation errors for a release manifest.
        """
        errors: list[str] = []

        if not isinstance(manifest, ReleaseManifest):
            return ["Manifest must be a ReleaseManifest instance."]

        if not cls._is_nonempty_text(manifest.version):
            errors.append("Version must be a nonempty string.")

        if not cls._is_nonempty_text(manifest.goal):
            errors.append("Goal must be a nonempty string.")

        if not cls._is_nonempty_text(
            manifest.validation_status
        ):
            errors.append(
                "Validation status must be a nonempty string."
            )

        cls._validate_file_list(
            "Files added",
            manifest.files_added,
            errors,
        )
        cls._validate_file_list(
            "Files changed",
            manifest.files_changed,
            errors,
        )
        cls._validate_file_list(
            "Files removed",
            manifest.files_removed,
            errors,
        )
        cls._validate_text_list(
            "Validation details",
            manifest.validation_details,
            errors,
        )
        cls._validate_text_list(
            "Known issues",
            manifest.known_issues,
            errors,
        )
        cls._validate_text_list(
            "Release notes",
            manifest.release_notes,
            errors,
        )
        cls._validate_text_list(
            "Future work",
            manifest.future_work,
            errors,
        )
        cls._validate_metadata(manifest.metadata, errors)

        return errors

    @classmethod
    def _manifest_path(
        cls,
        project_path: str | Path,
    ) -> Path:
        """
        Return the JSON release manifest path for a project.
        """
        return (
            Path(project_path)
            / cls.FORGEBUD_FOLDER
            / cls.MANIFEST_FILE
        )

    @classmethod
    def _validate_file_list(
        cls,
        name: str,
        values: object,
        errors: list[str],
    ) -> None:
        """
        Validate a list of project-relative file paths.
        """
        if not cls._is_text_list(values):
            errors.append(
                f"{name} must be a list of nonempty strings."
            )

    @classmethod
    def _validate_text_list(
        cls,
        name: str,
        values: object,
        errors: list[str],
    ) -> None:
        """
        Validate a list of text values.
        """
        if not cls._is_text_list(values):
            errors.append(
                f"{name} must be a list of nonempty strings."
            )

    @classmethod
    def _validate_metadata(
        cls,
        metadata: object,
        errors: list[str],
    ) -> None:
        """
        Validate extensible string metadata.
        """
        if not isinstance(metadata, dict):
            errors.append(
                "Metadata must be a dictionary of strings."
            )
            return

        if not all(
            cls._is_nonempty_text(key)
            and isinstance(value, str)
            for key, value in metadata.items()
        ):
            errors.append(
                "Metadata must be a dictionary of strings."
            )

    @classmethod
    def _is_text_list(cls, values: object) -> bool:
        """
        Return whether a value is a list of nonempty strings.
        """
        return (
            isinstance(values, list)
            and all(
                cls._is_nonempty_text(value)
                for value in values
            )
        )

    @staticmethod
    def _is_nonempty_text(value: object) -> bool:
        """
        Return whether a value is a nonempty string.
        """
        return (
            isinstance(value, str)
            and bool(value.strip())
        )