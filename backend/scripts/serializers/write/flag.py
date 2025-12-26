from scripts.serializers.base import BaseWriteSerializer
from scripts.models import (
    Flag,
    Part
)

class PartWriteSerializer(BaseWriteSerializer):
    '''part write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Part
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
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