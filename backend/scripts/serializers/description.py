from .base import BaseReadSerializer, PolicyBasedSerializer
from scripts.models import Description, DescriptionPart, Text

class BaseWriteSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True

class BaseWriteSerializer2(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "name",
        )

class TextReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Text
        fields = BaseReadSerializer.Meta.fields + (
            "text",
        )

class TextWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Text
        fields = (
            "description",
            "text,"
        )

class DescriptionPartReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = DescriptionPart
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class DescriptionPartWriteSerializer(BaseWriteSerializer2):
    class Meta(BaseWriteSerializer.Meta):
        model = DescriptionPart

class DescriptionReadSerializer(BaseReadSerializer):
    items = TextReadSerializer(
        source="description_Text",
        many=True,
        read_only = True
    )
    descriptionpart = DescriptionPartReadSerializer(
        read_only = True
    )

    class Meta(BaseReadSerializer.Meta):
        model = Description
        fields = BaseReadSerializer.Meta.fields + (
            "items",
            "descriptionpart",
        )

class DescriptionWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Description
        fields = (
            "scripts",
            "descriptionpart",
        )