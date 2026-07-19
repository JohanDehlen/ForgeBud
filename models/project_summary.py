"""
ForgeBud

Project summary model.

Represents the persistent project-summary document stored in:

    .forgebud/project_summary.md
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ProjectSummary:
    """
    Persistent project-summary state for a ForgeBud project.
    """

    markdown: str = ""

    @property
    def is_empty(self) -> bool:
        """
        Return True when the project-summary document contains
        no meaningful text.
        """
        return not self.markdown.strip()