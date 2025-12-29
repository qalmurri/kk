from scripts.serializers.read import BaseReadSerializer
from scripts.models.script import (
    Note,
    SectionNote,
    TextNote
)

class SectionNoteReadSerializer(BaseReadSerializer):
    '''section note read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = SectionNote
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class TextNoteReadSerializer(BaseReadSerializer):
    '''text note read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = TextNote
        fields = BaseReadSerializer.Meta.fields + (
            "text",
        )

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