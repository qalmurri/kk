from scripts.serializers.base import BaseReadSerializer
from scripts.models import (
    Section,
    By,
    ScriptProcess
)
from .user import UserSerializer

class SectionReadSerializer(BaseReadSerializer):
    '''section read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Section
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class ByReadSerializer(BaseReadSerializer):
    '''by read serializer'''
    user = UserSerializer(
        read_only=True
    )
    class Meta(BaseReadSerializer.Meta):
        model = By
        fields = BaseReadSerializer.Meta.fields + (
            "user",
        )

class ScriptProcessReadSerializer(BaseReadSerializer):
    '''script process read serializer'''
    by = ByReadSerializer(
        source="scriptsprocess_By",
        many=True
    )
    section = SectionReadSerializer(
        read_only = True
    )
    class Meta(BaseReadSerializer.Meta):
        model = ScriptProcess
        fields = BaseReadSerializer.Meta.fields + (
            "by",
            "section",
        )