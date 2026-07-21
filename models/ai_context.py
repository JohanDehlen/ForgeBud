"""
ForgeBud

Deprecated EngineeringContext compatibility module.

This module temporarily preserves the former AIContext name while
the project transitions to provider-independent Engineering Context
terminology.
"""

from models.engineering_context import EngineeringContext


AIContext = EngineeringContext