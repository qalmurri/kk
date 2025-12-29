from scripts.serializers.base import BaseWriteSerializer
from scripts.models.script import (
    LabelStatus,
    SectionStatus,
    Status
)

class LabelStatusWriteSerializer(BaseWriteSerializer):
    '''label status write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = LabelStatus
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

class SectionStatusWriteSerializer(BaseWriteSerializer):
    '''section status write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = SectionStatus
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

class StatusWriteSerializer(BaseWriteSerializer):
    '''status write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Status
        fields = BaseWriteSerializer.Meta.fields + (
            "script",
            "labelstatus",
            "sectionstatus",
        )

