from scripts.serializers.base import BaseReadSerializer
from scripts.models.script import (
    Flag,
    SectionFlag
)

class SectionFlagReadSerializer(BaseReadSerializer):
    '''part read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = SectionFlag
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class FlagReadSerializer(BaseReadSerializer):
    '''flag read serializer'''
    sectionflag = SectionFlagReadSerializer(
        read_only=True
    )
    class Meta(BaseReadSerializer):
        model = Flag
        fields = BaseReadSerializer.Meta.fields + (
            "sectionflag",
            "is_active",
        )