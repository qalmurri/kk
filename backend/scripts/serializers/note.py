from .base import (
    BaseReadSerializer,
    BaseWriteSerializer
)
from scripts.models import (
    Note,
    SectionNote,
    TextNote
)

# SECTIONNOTE READ & WRITE
class SectionNoteReadSerializer(BaseReadSerializer):
    '''section note read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = SectionNote
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class SectionNoteWriteSerializer(BaseWriteSerializer):
    '''section note write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = SectionNote
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

# CONTENT READ & WRITE
class TextNoteReadSerializer(BaseReadSerializer):
    '''text note read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = TextNote
        fields = BaseReadSerializer.Meta.fields + (
            "text",
        )

class TextNoteWriteSerializer(BaseWriteSerializer):
    '''text note write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = TextNote
        fields = BaseWriteSerializer.Meta.fields + (
            "note",
            "text",
        )

# NOTE_ READ & WRITE
class NoteReadSerializer(BaseReadSerializer):
    '''note read serializer'''
    textnote = TextNoteReadSerializer(
        source="note_Content",
        many=True,
        read_only = True
    )
    sectionnote = SectionNoteReadSerializer(
        read_only = True
    )
    class Meta(BaseReadSerializer.Meta):
        model = Note
        fields = BaseReadSerializer.Meta.fields + (
            "textnote",
            "sectionnote",
        )

class NoteWriteSerializer(BaseWriteSerializer):
    '''note write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Note
        fields = BaseWriteSerializer.Meta.fields + (
            "script",
            "sectionnote"
        )