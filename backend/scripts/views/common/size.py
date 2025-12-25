from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.common import (
    SizeReadSerializer,
    SizeWriteSerializer
    )
from scripts.repositories.common import (
    SizeQueryRepository,
    SizeCommandRepository
    )

class SizeViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = SizeReadSerializer
    write_serializer_class = SizeWriteSerializer
    query_repo = SizeQueryRepository
    command_repo = SizeCommandRepository