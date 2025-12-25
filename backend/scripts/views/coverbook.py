from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.content import (
    CoverBookReadSerializer,
    CoverBookWriteSerializer
    )
from scripts.repositories.content.coverbook import (
    CoverBookQueryRepository,
    CoverBookCommandRepository
    )

class CoverBookViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = CoverBookReadSerializer
    write_serializer_class = CoverBookWriteSerializer
    query_repo = CoverBookQueryRepository
    command_repo = CoverBookCommandRepository