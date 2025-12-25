from .base import BaseWriteSerializer, BaseReadSerializer
from scripts.models import Flag, Part

# PART READ & WRITE
class PartReadSerializer(BaseReadSerializer):
    '''part read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Part
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class PartWriteSerializer(BaseWriteSerializer):
    '''part write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Part
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

# FLAG READ & WRITE
class FlagReadSerializer(BaseReadSerializer):
    '''flag read serializer'''
    part = PartReadSerializer(
        read_only=True
    )
    class Meta(BaseReadSerializer):
        model = Flag
        fields = BaseReadSerializer.Meta.fields + (
            "part",
            "is_active",
        )

class FlagWriteSerializer(BaseWriteSerializer):
    '''flag write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Flag
        fields = BaseWriteSerializer.Meta.fields + (
            "scripts",
            "is_active",
            "part",
        )