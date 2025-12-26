from scripts.serializers.base import BaseReadSerializer
from scripts.models import (
    Description,
    SectionDescription,
    TextDescription
)

class TextDescriptionReadSerializer(BaseReadSerializer):
    '''text description read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = TextDescription
        fields = BaseReadSerializer.Meta.fields + (
            "text",
        )

class SectionDescriptionReadSerializer(BaseReadSerializer):
    '''section description read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = SectionDescription
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

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