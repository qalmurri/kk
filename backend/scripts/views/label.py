from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.common import (
    LabelReadSerializer,
    LabelWriteSerializer
    )
from scripts.repositories.common.label import (
    LabelQueryRepository,
    LabelCommandRepository
    )

class LabelViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = LabelReadSerializer
    write_serializer_class = LabelWriteSerializer
    query_repo = LabelQueryRepository
    command_repo = LabelCommandRepository