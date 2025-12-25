from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.pivot import (
    ByReadSerializer,
    ByWriteSerializer
    )
from scripts.repositories.pivot.by import (
    ByQueryRepository,
    ByCommandRepository
    )

class ByViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = ByReadSerializer
    write_serializer_class = ByWriteSerializer
    query_repo = ByQueryRepository
    command_repo = ByCommandRepository