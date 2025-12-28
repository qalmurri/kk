from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.read import (
    NoteReadSerializer,
    SectionNoteReadSerializer,
    TextNoteReadSerializer,
    )
from scripts.serializers.write import (
    NoteWriteSerializer,
    SectionNoteWriteSerializer,
    TextNoteWriteSerializer
    )
from scripts.repositories.command import (
    NoteCommandRepository,
    TextNoteCommandRepository,
    SectionNoteCommandRepository
    )
from scripts.repositories.query import (
    NoteQueryRepository,
    TextNoteQueryRepository,
    SectionNoteQueryRepository
    )

class NoteViewSet(BaseCRUDViewSet):
    '''note viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = NoteReadSerializer
    write_serializer_class = NoteWriteSerializer
    query_repo = NoteQueryRepository
    command_repo = NoteCommandRepository

class TextNoteViewSet(BaseCRUDViewSet):
    '''content viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = TextNoteReadSerializer
    write_serializer_class = TextNoteWriteSerializer
    query_repo = SectionNoteQueryRepository
    command_repo = TextNoteCommandRepository

class SectionNoteViewSet(BaseCRUDViewSet):
    '''note part viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = SectionNoteReadSerializer
    write_serializer_class = SectionNoteWriteSerializer
    query_repo = SectionNoteQueryRepository
    command_repo = TextNoteCommandRepository
