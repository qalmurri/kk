from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.read.script import (
    NoteReadSerializer,
    SectionNoteReadSerializer,
    TextNoteReadSerializer,
    )
from scripts.serializers.write.script import (
    NoteWriteSerializer,
    SectionNoteWriteSerializer,
    TextNoteWriteSerializer
    )
from scripts.repositories.command.script import (
    NoteCommandRepository,
    TextNoteCommandRepository,
    SectionNoteCommandRepository
    )
from scripts.repositories.query.script import (
    NoteQueryRepository,
    TextNoteQueryRepository,
    SectionNoteQueryRepository
    )

class NoteViewSet(BaseCRUDViewSet):
    '''note viewset'''
    read_serializer_class = NoteReadSerializer
    write_serializer_class = NoteWriteSerializer
    query_repo = NoteQueryRepository
    command_repo = NoteCommandRepository

class TextNoteViewSet(BaseCRUDViewSet):
    '''content viewset'''
    read_serializer_class = TextNoteReadSerializer
    write_serializer_class = TextNoteWriteSerializer
    query_repo = TextNoteQueryRepository
    command_repo = TextNoteCommandRepository

class SectionNoteViewSet(BaseCRUDViewSet):
    '''note part viewset'''
    read_serializer_class = SectionNoteReadSerializer
    write_serializer_class = SectionNoteWriteSerializer
    query_repo = SectionNoteQueryRepository
    command_repo = SectionNoteCommandRepository
