from scripts.serializers.base import BaseWriteSerializer
from scripts.models import (
    SectionMade,
    ByMade,
    Made
)

class SectionMadeWriteSerializer(BaseWriteSerializer):
    '''section write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = SectionMade
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

class ByMadeWriteSerializer(BaseWriteSerializer):
    '''by write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = ByMade
        fields = BaseWriteSerializer.Meta.fields + (
            "made",
            "user",
        )

class MadeWriteSerializer(BaseWriteSerializer):
    '''script process write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Made
        fields = (
            "script",
            "section",
        )