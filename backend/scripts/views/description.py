from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.pivot import (
    DescriptionReadSerializer,
    DescriptionWriteSerializer
    )
from scripts.repositories.pivot.description import (
    DescriptionQueryRepository,
    DescriptionCommandRepository
    )

class DescriptionViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = DescriptionReadSerializer
    write_serializer_class = DescriptionWriteSerializer
    query_repo = DescriptionQueryRepository
    command_repo = DescriptionCommandRepository