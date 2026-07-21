"""
ForgeBud

Engineering Context service.

Builds the canonical, provider-independent EngineeringContext
from the current project state.
"""

from __future__ import annotations

from pathlib import Path

from models.engineering_context import EngineeringContext
from services.coding_standards_service import (
    CodingStandardsService,
)
from services.context_service import ContextService
from services.current_task_service import CurrentTaskService
from services.decisions_service import DecisionsService
from services.project_service import ProjectService
from services.project_summary_service import (
    ProjectSummaryService,
)
from services.project_validation_service import (
    ProjectValidationService,
)
from services.release_manifest_service import (
    ReleaseManifestService,
)


class EngineeringContextService:
    """
    Builds EngineeringContext from an initialized ForgeBud project.
    """

    @classmethod
    def build(
        cls,
        project_path: str | Path,
    ) -> EngineeringContext:
        """
        Construct the complete engineering context for a project.

        This operation is read-only.
        """
        project_path = Path(project_path)

        return EngineeringContext(
            project_info=ProjectService.load(project_path),
            project_context=ContextService.build(project_path),
            project_summary=ProjectSummaryService.load(
                project_path
            ),
            current_task=CurrentTaskService.load(project_path),
            coding_standards=CodingStandardsService.load(
                project_path
            ),
            decisions=DecisionsService.load(project_path),
            release_manifest=ReleaseManifestService.load(
                project_path
            ),
            project_validation=ProjectValidationService.validate(
                project_path
            ),
        )