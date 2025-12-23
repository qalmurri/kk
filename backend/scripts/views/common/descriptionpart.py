from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.common import (
    DescriptionPartReadSerializer,
    DescriptionPartWriteSerializer
    )
from scripts.repositories.common.descriptionpart import (
    DescriptionPartQueryRepository,
    DescriptionPartCommandRepository
    )

class DescriptionPartViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = DescriptionPartReadSerializer
    write_serializer_class = DescriptionPartWriteSerializer
    query_repo = DescriptionPartQueryRepository
    command_repo = DescriptionPartCommandRepository