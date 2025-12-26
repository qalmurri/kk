from scripts.serializers.base import BaseReadSerializer
from scripts.models import (
    Flag,
    Part
)

class PartReadSerializer(BaseReadSerializer):
    '''part read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Part
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

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