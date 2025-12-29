from scripts.serializers.read import BaseReadSerializer, UserReadSerializer
from scripts.models.script import (
    Made,
    SectionMade,
    ByMade
)

class SectionMadeReadSerializer(BaseReadSerializer):
    '''section read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = SectionMade
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class ByMadeReadSerializer(BaseReadSerializer):
    '''by read serializer'''
    user = UserReadSerializer(
        read_only=True
    )
    class Meta(BaseReadSerializer.Meta):
        model = ByMade
        fields = BaseReadSerializer.Meta.fields + (
            "user",
        )

class MadeReadSerializer(BaseReadSerializer):
    '''script process read serializer'''
    bymade = ByMadeReadSerializer(
        source="scriptsprocess_By",
        many=True
    )
    sectionmade = SectionMadeReadSerializer(
        read_only = True
    )
    class Meta(BaseReadSerializer.Meta):
        model = Made
        fields = BaseReadSerializer.Meta.fields + (
            "bymade",
            "sectionmade",
        )