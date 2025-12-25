from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.pivot import (
    NoteReadSerializer,
    NoteWriteSerializer
    )
from scripts.repositories.pivot.note import (
    NoteQueryRepository,
    NoteCommandRepository
    )

class NoteViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = NoteReadSerializer
    write_serializer_class = NoteWriteSerializer
    query_repo = NoteQueryRepository
    command_repo = NoteCommandRepository