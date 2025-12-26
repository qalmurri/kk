from scripts.serializers.base import BaseWriteSerializer
from scripts.models import (
    Section,
    By,
    ScriptProcess
)

class SectionWriteSerializer(BaseWriteSerializer):
    '''section write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Section
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

class ByWriteSerializer(BaseWriteSerializer):
    '''by write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = By
        fields = BaseWriteSerializer.Meta.fields + (
            "scriptprocess",
            "user",
        )

class ScriptProcessWriteSerializer(BaseWriteSerializer):
    '''script process write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = ScriptProcess
        fields = (
            "script",
            "section",
        )