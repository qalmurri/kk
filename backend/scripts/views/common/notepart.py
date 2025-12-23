from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.common import (
    NotePartReadSerializer,
    NotePartWriteSerializer
    )
from scripts.repositories.common.notepart import (
    NotePartQueryRepository,
    NotePartCommandRepository
    )

class NotePartViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = NotePartReadSerializer
    write_serializer_class = NotePartWriteSerializer
    query_repo = NotePartQueryRepository
    command_repo = NotePartCommandRepository
