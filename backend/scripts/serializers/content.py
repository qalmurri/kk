from .base import PolicyBasedSerializer
from scripts.models import (
    ISBN,
    Flag,
    Content,
    Text,
    CoverBook
)
from .common import (
    PartReadSerializer,
    TypeReadSerializer
)

# base
class BaseReadSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "id",
            "created_at",
            "updated_at",
        )

# coverbook
COVERBOOK_FIELDS = (
    "thumbnail",
    "length",
    "height",
    "width",
    "x_axis",
    "y_axis",
)

class CoverBookReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = CoverBook
        fields = BaseReadSerializer.Meta.fields + COVERBOOK_FIELDS

class CoverBookWriteSerializer(PolicyBasedSerializer):
    class Meta:
        model = CoverBook
        fields = (
            "scripts",
        ) + COVERBOOK_FIELDS
        read_only_fields = (
            "id",
        )

# text
class TextReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Text
        fields = BaseReadSerializer.Meta.fields + (
            "text",
        )

# content
class ContentReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Content
        fields = BaseReadSerializer.Meta.fields + (
            "content",
        )

# flag
class FlagReadSerializer(BaseReadSerializer):
    part = PartReadSerializer(
        read_only=True
    )

    class Meta(BaseReadSerializer):
        model = Flag
        fields = BaseReadSerializer.Meta.fields + (
            "is_active",
            "part",
        )

# isbn
class ISBNReadSerializer(BaseReadSerializer):
    type = TypeReadSerializer(
        read_only=True
    )

    class Meta(BaseReadSerializer.Meta):
        model = ISBN
        fields = BaseReadSerializer.Meta.fields + (
            "isbn",
            "type",
        )