from .base import BaseReadSerializer, PolicyBasedSerializer
from scripts.models import Label, ScriptsStatusCode, Status

class BaseWriteSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True

class BaseWriteSerializer2(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "name",
        )


# labelread
class LabelReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Label
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class LabelWriteSerializer(BaseWriteSerializer2):
    class Meta(BaseWriteSerializer2.Meta):
        model = Label



# code
class CodeReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = ScriptsStatusCode
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class CodeWriteSerializer(BaseWriteSerializer2):
    class Meta(BaseWriteSerializer2.Meta):
        model = ScriptsStatusCode

# status
class StatusReadSerializer(BaseReadSerializer):
    code = CodeReadSerializer(
        read_only = True
    )
    label = LabelReadSerializer(
        read_only = True
    )

    class Meta(BaseReadSerializer.Meta):
        model = Status
        fields = BaseReadSerializer.Meta.fields + (
            "label",
            "code",
        )

class StatusWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Status
        fields = (
            "scripts",
            "label",
            "code",
        )

