from .base import (
    BaseReadSerializer,
    BaseWriteSerializer
)
from scripts.models import (
    Section,
    By,
    ScriptProcess
)
from .user import UserSerializer

# SECTION READ & WRITE
class SectionReadSerializer(BaseReadSerializer):
    '''section read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Section
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class SectionWriteSerializer(BaseWriteSerializer):
    '''section write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Section
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

# BY READ & WRITE
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

class ByWriteSerializer(BaseWriteSerializer):
    '''by write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = By
        fields = BaseWriteSerializer.Meta.fields + (
            "scriptprocess",
            "user",
        )

# SCRIPT PROCESS READ & WRITE
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

class ScriptProcessWriteSerializer(BaseWriteSerializer):
    '''script process write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = ScriptProcess
        fields = (
            "script",
            "section",
        )