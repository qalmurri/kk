from scripts.serializers.base import BaseWriteSerializer
from scripts.models import (
    Description,
    SectionDescription,
    TextDescription
)

class TextDescriptionWriteSerializer(BaseWriteSerializer):
    '''text description write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = TextDescription
        fields = BaseWriteSerializer.Meta.fields + (
            "text",
            "description",
        )

class SectionDescriptionWriteSerializer(BaseWriteSerializer):
    '''section description write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = SectionDescription
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

class DescriptionWriteSerializer(BaseWriteSerializer):
    '''description write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Description
        fields = BaseWriteSerializer.Meta.fields + (
            "script",
            "sectiondescription",
        )