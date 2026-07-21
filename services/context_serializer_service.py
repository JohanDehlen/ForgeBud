"""
ForgeBud

Deprecated compatibility wrapper.

This module exists temporarily while the project transitions to
EngineeringContext terminology.

It will be removed after all imports have been migrated.
"""

from services.engineering_context_serializer import (
    EngineeringContextSerializer,
)


class ContextSerializerService(EngineeringContextSerializer):
    """
    Backwards-compatible alias.

    Deprecated.
    """

    pass