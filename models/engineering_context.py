"""
ForgeBud

Engineering Context model.

Represents the complete, provider-independent engineering state
of a software project.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from models.coding_standards import CodingStandards
from models.current_task import CurrentTask
from models.decisions import Decisions
from models.project_context import ProjectContext
from models.project_info import ProjectInfo
from models.project_summary import ProjectSummary
from models.project_validation import ProjectValidation
from models.release_manifest import ReleaseManifest


@dataclass(slots=True)
class EngineeringContext:
    """
    Canonical engineering representation of a software project.

    The context is derived from repository and project-memory state.
    It is provider-independent and contains no business logic.
    """

    project_info: ProjectInfo = field(
        default_factory=ProjectInfo
    )

    project_context: ProjectContext = field(
        default_factory=ProjectContext
    )

    project_summary: ProjectSummary = field(
        default_factory=ProjectSummary
    )

    current_task: CurrentTask = field(
        default_factory=CurrentTask
    )

    coding_standards: CodingStandards = field(
        default_factory=CodingStandards
    )

    decisions: Decisions = field(
        default_factory=Decisions
    )

    release_manifest: ReleaseManifest = field(
        default_factory=ReleaseManifest
    )

    project_validation: ProjectValidation = field(
        default_factory=ProjectValidation
    )