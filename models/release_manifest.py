"""
ForgeBud

Release manifest model.

Represents the persistent release metadata stored in:

    .forgebud/release_manifest.json
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class ReleaseManifest:
    """
    Persistent metadata describing a ForgeBud release.
    """

    version: str = ""

    goal: str = ""

    files_added: list[str] = field(default_factory=list)

    files_changed: list[str] = field(default_factory=list)

    files_removed: list[str] = field(default_factory=list)

    validation_status: str = "not_run"

    validation_details: list[str] = field(default_factory=list)

    known_issues: list[str] = field(default_factory=list)

    release_notes: list[str] = field(default_factory=list)

    future_work: list[str] = field(default_factory=list)

    metadata: dict[str, str] = field(default_factory=dict)