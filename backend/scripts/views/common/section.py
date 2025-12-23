from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.common import (
    SectionReadSerializer,
    SectionWriteSerializer
    )
from scripts.repositories.common.section import (
    SectionQueryRepository,
    SectionCommandRepository
    )

class SectionViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = SectionReadSerializer
    write_serializer_class = SectionWriteSerializer
    query_repo = SectionQueryRepository
    command_repo = SectionCommandRepository