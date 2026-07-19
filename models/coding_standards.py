"""
ForgeBud

Coding standards model.

Represents the persistent coding-standards document stored in:

    .forgebud/coding_standards.md
"""

from dataclasses import dataclass


@dataclass(slots=True)
class CodingStandards:
    """
    Persistent coding standards for a ForgeBud project.
    """

    markdown: str = ""

    @property
    def is_empty(self) -> bool:
        """
        Return True when the coding-standards document contains
        no meaningful text.
        """
        return not self.markdown.strip()