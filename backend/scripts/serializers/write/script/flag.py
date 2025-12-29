from scripts.serializers.write import BaseWriteSerializer
from scripts.models.script import (
    Flag,
    SectionFlag
)

class SectionFlagWriteSerializer(BaseWriteSerializer):
    '''part write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = SectionFlag
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
            "sectionflag",
        )