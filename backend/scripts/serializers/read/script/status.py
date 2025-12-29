from scripts.serializers.read import BaseReadSerializer
from scripts.models.script import (
    LabelStatus,
    SectionStatus,
    Status
)

class LabelStatusReadSerializer(BaseReadSerializer):
    '''label status read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = LabelStatus
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class SectionStatusReadSerializer(BaseReadSerializer):
    '''section status read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = SectionStatus
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class StatusReadSerializer(BaseReadSerializer):
    '''status read serializer'''
    sectionstatus = SectionStatusReadSerializer(
        read_only = True
    )
    labelstatus = LabelStatusReadSerializer(
        read_only = True
    )
    class Meta(BaseReadSerializer.Meta):
        model = Status
        fields = BaseReadSerializer.Meta.fields + (
            "labelstatus",
            "sectionstatus",
        )