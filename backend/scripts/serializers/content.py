from .base import PolicyBasedSerializer
from scripts.models import (
    ISBN,
    Flag,
    Content,
    Text,
    Cover
)
from .common import (
    PartSerializer,
    TypeSerializer
)

class CoverSerializer(PolicyBasedSerializer):
    class Meta:
        model = Cover
        fields = [
            "id",
            "thumbnail",
            "length",
            "height",
            "width",
            "x_axis",
            "y_axis",
        ]

class TextSerializer(PolicyBasedSerializer):
    class Meta:
        model = Text
        fields = [
            "id",
            "text",
            "created_at",
            "updated_at"
        ]

class FlagSerializer(PolicyBasedSerializer):
    part = PartSerializer()

    class Meta:
        model = Flag
        fields = [
            "id",
            "is_active",
            "part",
            "created_at",
            "updated_at"
        ]

class ISBNSerializer(PolicyBasedSerializer):
    type = TypeSerializer()

    class Meta:
        model = ISBN
        fields = [
            "id",
            "isbn",
            "type",
            "created_at",
            "updated_at"
        ]

class ContentSerializer(PolicyBasedSerializer):
    class Meta:
        model = Content
        fields = [
            "id",
            "content",
            "created_at",
            "updated_at"
        ]