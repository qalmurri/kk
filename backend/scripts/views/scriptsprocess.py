from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.pivot import (
    ScriptsProcessReadSerializer,
    ScriptsProcessWriteSerializer
    )
from scripts.repositories.pivot.scriptsprocess import (
    ScriptsProcessQueryRepository,
    ScriptsProcessCommandRepository
    )

class ScriptsProcessViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = ScriptsProcessReadSerializer
    write_serializer_class = ScriptsProcessWriteSerializer
    query_repo = ScriptsProcessQueryRepository
    command_repo = ScriptsProcessCommandRepository