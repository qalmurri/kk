from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.content import (
    ContentReadSerializer,
    ContentWriteSerializer
    )
from scripts.repositories.content.content import (
    ContentQueryRepository,
    ContentCommandRepository
    )

class ContentViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = ContentReadSerializer
    write_serializer_class = ContentWriteSerializer
    query_repo = ContentQueryRepository
    command_repo = ContentCommandRepository