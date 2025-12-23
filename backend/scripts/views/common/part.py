from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.common import (
    PartReadSerializer,
    PartWriteSerializer
    )
from scripts.repositories.common.part import (
    PartQueryRepository,
    PartCommandRepository
    )

class PartViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = PartReadSerializer
    write_serializer_class = PartWriteSerializer
    query_repo = PartQueryRepository
    command_repo = PartCommandRepository