from .base import BaseReadSerializer, PolicyBasedSerializer
from scripts.models import Note, NotePart, Content

class BaseWriteSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True

class BaseWriteSerializer2(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "name",
        )

# notepart
class NotePartReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = NotePart
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class NotePartWriteSerializer(BaseWriteSerializer2):
    class Meta(BaseWriteSerializer2.Meta):
        model = NotePart

# content
class ContentReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Content
        fields = BaseReadSerializer.Meta.fields + (
            "content",
        )

class ContentWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Content
        fields = (
            "note",
            "content",
        )

# note
class NoteReadSerializer(BaseReadSerializer):
    items = ContentReadSerializer(
        source="note_Content",
        many=True,
        read_only = True
    )
    notepart = NotePartReadSerializer(
        read_only = True
    )

    class Meta(BaseReadSerializer.Meta):
        model = Note
        fields = BaseReadSerializer.Meta.fields + (
            "items",
            "notepart",
        )

class NoteWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Note
        fields = (
            "scripts",
            "notepart"
        )