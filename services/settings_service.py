"""
ForgeBud

Application settings service.

Responsibilities:
- Load and save application settings.
- Maintain the recent-projects list.
- Ensure the configuration directory exists.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class SettingsService:
    """
    Service responsible for persistent application settings.
    """

    CONFIG_DIR = Path("config")
    SETTINGS_FILE = CONFIG_DIR / "settings.json"

    RECENT_PROJECTS_KEY = "recent_projects"
    MAX_RECENT_PROJECTS = 10

    DEFAULT_SETTINGS: dict[str, Any] = {
        "last_project": "",
        "recent_projects": [],
        "window_width": 1400,
        "window_height": 900,
        "window_x": None,
        "window_y": None,
    }

    @classmethod
    def load(cls) -> dict[str, Any]:
        """
        Load application settings and ensure default values exist.
        """
        cls._ensure_config_exists()

        if not cls.SETTINGS_FILE.exists():
            settings = cls._default_settings()
            cls.save(settings)
            return settings

        try:
            loaded_settings = json.loads(
                cls.SETTINGS_FILE.read_text(
                    encoding="utf-8"
                )
            )
        except (
            json.JSONDecodeError,
            OSError,
        ):
            loaded_settings = {}

        if not isinstance(loaded_settings, dict):
            loaded_settings = {}

        settings = cls._default_settings()
        settings.update(loaded_settings)

        return settings

    @classmethod
    def save(cls, settings: dict[str, Any]) -> None:
        """
        Save application settings.
        """
        cls._ensure_config_exists()

        cls.SETTINGS_FILE.write_text(
            json.dumps(
                settings,
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    @classmethod
    def get(
        cls,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve a single setting.
        """
        settings = cls.load()

        return settings.get(key, default)

    @classmethod
    def set(cls, key: str, value: Any) -> None:
        """
        Store a single setting.
        """
        settings = cls.load()
        settings[key] = value

        cls.save(settings)

    @classmethod
    def get_recent_projects(cls) -> list[str]:
        """
        Return valid recent project folders, newest first.

        Invalid, duplicate, and nonexistent entries are removed
        from persistent settings.
        """
        settings = cls.load()
        recent_projects = cls._normalize_recent_projects(
            settings.get(cls.RECENT_PROJECTS_KEY, [])
        )

        if settings.get(cls.RECENT_PROJECTS_KEY) != recent_projects:
            settings[cls.RECENT_PROJECTS_KEY] = recent_projects
            cls.save(settings)

        return recent_projects

    @classmethod
    def add_recent_project(
        cls,
        project_path: str | Path,
    ) -> None:
        """
        Add a valid project folder to the recent-projects list.

        The newest project is kept first. Duplicate entries are
        removed and the list is limited to MAX_RECENT_PROJECTS.
        """
        path = Path(project_path)

        if not path.is_dir():
            return

        resolved_path = str(path.resolve())
        existing_projects = cls.get_recent_projects()

        recent_projects = [
            existing_path
            for existing_path in existing_projects
            if not cls._paths_match(
                existing_path,
                resolved_path,
            )
        ]

        recent_projects.insert(0, resolved_path)

        settings = cls.load()
        settings[cls.RECENT_PROJECTS_KEY] = (
            recent_projects[:cls.MAX_RECENT_PROJECTS]
        )

        cls.save(settings)

    @classmethod
    def _default_settings(cls) -> dict[str, Any]:
        """
        Return an independent copy of the default settings.
        """
        return {
            key: value.copy()
            if isinstance(value, list)
            else value
            for key, value in cls.DEFAULT_SETTINGS.items()
        }

    @classmethod
    def _normalize_recent_projects(
        cls,
        recent_projects: Any,
    ) -> list[str]:
        """
        Return valid, unique project folders in their saved order.
        """
        if not isinstance(recent_projects, list):
            return []

        normalized_projects: list[str] = []
        seen_paths: set[str] = set()

        for project_path in recent_projects:
            if not isinstance(project_path, str):
                continue

            path = Path(project_path)

            if not path.is_dir():
                continue

            resolved_path = str(path.resolve())
            comparison_path = resolved_path.casefold()

            if comparison_path in seen_paths:
                continue

            seen_paths.add(comparison_path)
            normalized_projects.append(resolved_path)

            if len(normalized_projects) == cls.MAX_RECENT_PROJECTS:
                break

        return normalized_projects

    @staticmethod
    def _paths_match(
        first_path: str,
        second_path: str,
    ) -> bool:
        """
        Compare project paths without case sensitivity.
        """
        return first_path.casefold() == second_path.casefold()

    @classmethod
    def _ensure_config_exists(cls) -> None:
        """
        Ensure the configuration directory exists.
        """
        cls.CONFIG_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )