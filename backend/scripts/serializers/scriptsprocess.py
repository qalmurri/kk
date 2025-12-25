from .base import BaseReadSerializer, PolicyBasedSerializer
from scripts.models import Section, By, ScriptsProcess
from .user import UserSerializer

class BaseWriteSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True

class BaseWriteSerializer2(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "name",
        )

# section
class SectionReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Section
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class SectionWriteSerializer(BaseWriteSerializer2):
    class Meta(v.Meta):
        model = Section

# by
class ByReadSerializer(BaseReadSerializer):
    user = UserSerializer(
        read_only=True
    )

    class Meta(BaseReadSerializer.Meta):
        model = By
        fields = BaseReadSerializer.Meta.fields + (
            "user",
        )

class ByWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = By
        fields = (
            "scriptsprocess",
            "user",
        )

# scriptsprocess
class ScriptsProcessReadSerializer(BaseReadSerializer):
    by = ByReadSerializer(
        source="scriptsprocess_By",
        many=True
    )
    section = SectionReadSerializer(
        read_only = True
    )

    class Meta(BaseReadSerializer.Meta):
        model = ScriptsProcess
        fields = BaseReadSerializer.Meta.fields + (
            "by",
            "section",
        )

class ScriptsProcessWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = ScriptsProcess
        fields = (
            "scripts",
            "section",
        )