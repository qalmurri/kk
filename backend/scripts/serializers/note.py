from .base import BaseReadSerializer, BaseWriteSerializer
from scripts.models import Note, SectionNote, TextNote

# NOTEPART READ & WRITE
class SectionNoteReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = SectionNote
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class SectionNoteWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = SectionNote
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

# CONTENT READ & WRITE
class TextNoteReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = TextNote
        fields = BaseReadSerializer.Meta.fields + (
            "text",
        )

class TextNoteWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = TextNote
        fields = BaseWriteSerializer.Meta.fields + (
            "note",
            "text",
        )

# NOTE_ READ & WRITE
class NoteReadSerializer(BaseReadSerializer):
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
            "items",
            "sectionnote",
        )

class NoteWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Note
        fields = (
            "script",
            "sectionnote"
        )