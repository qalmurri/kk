from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.content import (
    FlagReadSerializer,
    FlagWriteSerializer
    )
from scripts.repositories.content.flag import (
    FlagQueryRepository,
    FlagCommandRepository
    )

class FlagViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = FlagReadSerializer
    write_serializer_class = FlagWriteSerializer
    query_repo = FlagQueryRepository
    command_repo = FlagCommandRepository