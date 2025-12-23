from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.pivot import (
    StatusReadSerializer,
    StatusWriteSerializer
    )
from scripts.repositories.pivot.status import (
    StatusQueryRepository,
    StatusCommandRepository
    )

class StatusViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = StatusReadSerializer
    write_serializer_class = StatusWriteSerializer
    query_repo = StatusQueryRepository
    command_repo = StatusCommandRepository