from .base import (
    BaseReadSerializer,
    BaseWriteSerializer
)
from scripts.models import (
    Description,
    SectionDescription,
    TextDescription
)

# TEXTDESCRIPTION READ & WRITE
class TextDescriptionReadSerializer(BaseReadSerializer):
    '''text description read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = TextDescription
        fields = BaseReadSerializer.Meta.fields + (
            "text",
        )

class TextDescriptionWriteSerializer(BaseWriteSerializer):
    '''text description write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = TextDescription
        fields = BaseWriteSerializer.Meta.fields + (
            "text",
            "description",
        )

# SECTIONDESCRIPTION READ & WRITE
class SectionDescriptionReadSerializer(BaseReadSerializer):
    '''section description read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = SectionDescription
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class SectionDescriptionWriteSerializer(BaseWriteSerializer):
    '''section description write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = SectionDescription
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

# DESCRIPTION READ & WRITE
class DescriptionReadSerializer(BaseReadSerializer):
    '''description read serializer'''
    textdescription = TextDescriptionReadSerializer(
        source="description_Text",
        many=True,
        read_only = True
    )
    sectiondescription = SectionDescriptionReadSerializer(
        read_only = True
    )
    class Meta(BaseReadSerializer.Meta):
        model = Description
        fields = BaseReadSerializer.Meta.fields + (
            "textdescription",
            "sectiondescription",
        )

class DescriptionWriteSerializer(BaseWriteSerializer):
    '''description write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Description
        fields = BaseWriteSerializer.Meta.fields + (
            "script",
            "sectiondescription",
        )