from .base import BaseReadSerializer, BaseWriteSerializer
from scripts.models import LabelStatus, SectionStatus, Status

# LABEL READ & WRITE
class LabelStatusReadSerializer(BaseReadSerializer):
    '''label status read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = LabelStatus
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class LabelStatusWriteSerializer(BaseWriteSerializer):
    '''label status write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = LabelStatus
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

# CODE READ & WRITE
class SectionStatusReadSerializer(BaseReadSerializer):
    '''section status read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = SectionStatus
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class SectionStatusWriteSerializer(BaseWriteSerializer):
    '''section status write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = SectionStatus
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

# STATUS READ & WRITE
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

class StatusWriteSerializer(BaseWriteSerializer):
    '''status write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Status
        fields = BaseWriteSerializer.Meta.fields + (
            "script",
            "labelstatus",
            "sectionstatus",
        )

