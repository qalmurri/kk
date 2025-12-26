from scripts.serializers.base import BaseWriteSerializer
from scripts.models import (
    Note,
    SectionNote,
    TextNote
)

class SectionNoteWriteSerializer(BaseWriteSerializer):
    '''section note write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = SectionNote
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

class TextNoteWriteSerializer(BaseWriteSerializer):
    '''text note write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = TextNote
        fields = BaseWriteSerializer.Meta.fields + (
            "note",
            "text",
        )

class NoteWriteSerializer(BaseWriteSerializer):
    '''note write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Note
        fields = BaseWriteSerializer.Meta.fields + (
            "script",
            "sectionnote"
        )