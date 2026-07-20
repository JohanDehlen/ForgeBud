"""
ForgeBud

Project service.

Responsible for validating, creating, and maintaining
ForgeBud project metadata.

Project Structure

<Project>/
    .forgebud/
        project.json
        project_summary.md
        roadmap.md
        architecture.md
        current_task.md
        assistant_rules.md
        coding_standards.md
        decisions.md
        changelog.md
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from models.project_info import ProjectInfo
from services.file_service import FileService


class ProjectService:
    """
    Manages ForgeBud project initialization and metadata.
    """

    FORGEBUD_FOLDER = ".forgebud"
    PROJECT_FILE = "project.json"

    DEFAULT_PROJECT_SUMMARY = """# Project Summary

## Purpose

Describe why this project exists.

## What It Does

Describe the primary functionality of the project.

## Intended Users

Describe who or what the project is designed for.

## Technology

Document the primary language, framework, platform, and important
dependencies.

## Current State

Describe the project's present development state.

## Important Context

Record constraints, assumptions, or background information needed
to understand the project.
"""

    DEFAULT_CODING_STANDARDS = """# Coding Standards

## General Principles

- Prefer readable code over clever code.
- Keep responsibilities clearly separated.
- Preserve existing functionality unless a change is intentional.
- Avoid duplicated logic.
- Keep implementations simple and explicit.

## Language and Framework Conventions

Document the language, framework, and library conventions used by
this project.

## Naming

- Use descriptive names.
- Follow the naming conventions of the project's language.
- Avoid unclear abbreviations.

## Type Hints

- Add type hints where supported and practical.
- Keep public interfaces explicit.
- Avoid ambiguous return types.

## Functions and Classes

- Give each function and class one clear responsibility.
- Keep methods focused and reasonably short.
- Prefer composition over inheritance.
- Avoid hidden side effects.

## Error Handling

- Handle expected failures explicitly.
- Do not silently ignore important errors.
- Provide useful error messages.
- Avoid broad exception handling unless recovery is intentional.

## Documentation

- Write meaningful docstrings for public classes and methods.
- Explain why a non-obvious decision was made.
- Keep documentation synchronized with implementation.

## Testing

- Add tests for new behavior where practical.
- Preserve existing tests.
- Test failure paths as well as successful paths.

## Dependencies

- Reuse existing dependencies when appropriate.
- Avoid adding unnecessary packages.
- Record significant dependency decisions in project memory.

## Project-Specific Rules

Add project-specific coding rules below this section.
"""

    DEFAULT_FILES = {
        "project_summary.md": DEFAULT_PROJECT_SUMMARY,
        "roadmap.md": "# Roadmap\n",
        "architecture.md": "# Architecture\n",
        "current_task.md": "# Current Task\n",
        "assistant_rules.md": "# Assistant Rules\n",
        "coding_standards.md": DEFAULT_CODING_STANDARDS,
        "decisions.md": "# Decisions\n",
        "changelog.md": "# Changelog\n",
    }

    @classmethod
    def initialize(
        cls,
        project_path: str | Path,
        info: ProjectInfo,
    ) -> None:
        """
        Initialize a project for ForgeBud.

        Project metadata is validated and normalized before any
        filesystem changes occur. Existing project-memory documents
        are preserved.
        """
        normalized_info = cls._normalize_project_info(info)

        project_path = Path(project_path)
        fb_folder = project_path / cls.FORGEBUD_FOLDER

        FileService.create_directory(fb_folder)
        cls._write_project_info(
            fb_folder,
            normalized_info,
        )

        for filename, contents in cls.DEFAULT_FILES.items():
            file_path = fb_folder / filename

            if not FileService.exists(file_path):
                FileService.write_text(
                    file_path,
                    contents,
                )

    @classmethod
    def save(
        cls,
        project_path: str | Path,
        info: ProjectInfo,
    ) -> None:
        """
        Validate, normalize, and save project.json.
        """
        normalized_info = cls._normalize_project_info(info)

        project_path = Path(project_path)
        fb_folder = project_path / cls.FORGEBUD_FOLDER

        FileService.create_directory(fb_folder)
        cls._write_project_info(
            fb_folder,
            normalized_info,
        )

    @classmethod
    def load(
        cls,
        project_path: str | Path,
    ) -> ProjectInfo:
        """
        Load project.json.
        """
        project_path = Path(project_path)

        project_file = (
            project_path
            / cls.FORGEBUD_FOLDER
            / cls.PROJECT_FILE
        )

        if not FileService.exists(project_file):
            return ProjectInfo()

        data = json.loads(
            FileService.read_text(project_file)
        )

        return ProjectInfo(**data)

    @classmethod
    def is_initialized(
        cls,
        project_path: str | Path,
    ) -> bool:
        """
        Return True when a project has been initialized for ForgeBud.
        """
        project_path = Path(project_path)

        return FileService.exists(
            project_path
            / cls.FORGEBUD_FOLDER
            / cls.PROJECT_FILE
        )

    @classmethod
    def _normalize_project_info(
        cls,
        info: ProjectInfo,
    ) -> ProjectInfo:
        """
        Validate project metadata and return normalized state.

        Raises:
            ValueError: If the supplied project information is invalid.
        """
        if not isinstance(info, ProjectInfo):
            raise ValueError(
                "Project information must be a ProjectInfo instance."
            )

        string_fields = {
            "name": info.name,
            "version": info.version,
            "description": info.description,
            "language": info.language,
            "framework": info.framework,
            "repository": info.repository,
            "created_by": info.created_by,
            "forgebud_version": info.forgebud_version,
        }

        normalized_fields: dict[str, str] = {}

        for field_name, value in string_fields.items():
            if not isinstance(value, str):
                display_name = field_name.replace("_", " ")
                raise ValueError(
                    f"Project {display_name} must be a string."
                )

            normalized_fields[field_name] = value.strip()

        if not normalized_fields["name"]:
            raise ValueError("Project name is required.")

        if not normalized_fields["version"]:
            raise ValueError("Project version is required.")

        if not isinstance(info.assistant_rules, list):
            raise ValueError(
                "Project assistant rules must be a list of strings."
            )

        normalized_rules: list[str] = []

        for rule in info.assistant_rules:
            if not isinstance(rule, str):
                raise ValueError(
                    "Every project assistant rule must be a string."
                )

            normalized_rules.append(rule.strip())

        return ProjectInfo(
            name=normalized_fields["name"],
            version=normalized_fields["version"],
            description=normalized_fields["description"],
            language=normalized_fields["language"],
            framework=normalized_fields["framework"],
            repository=normalized_fields["repository"],
            created_by=normalized_fields["created_by"],
            forgebud_version=normalized_fields[
                "forgebud_version"
            ],
            assistant_rules=normalized_rules,
        )

    @classmethod
    def _write_project_info(
        cls,
        fb_folder: Path,
        info: ProjectInfo,
    ) -> None:
        """
        Write normalized project information to project.json.
        """
        project_file = fb_folder / cls.PROJECT_FILE

        FileService.write_text(
            project_file,
            json.dumps(
                asdict(info),
                indent=4,
            ),
        )