from .base import PolicyBasedSerializer
from .user import UserSerializer
from scripts.models import (
    ScriptsOrderer,
    Status,
    Description,
    Note,
    ScriptsProcess,
    By,
)
from .common import (
    OrdererReadSerializer,
    SectionReadSerializer,
    DescriptionPartReadSerializer,
    LabelReadSerializer,
    CodeReadSerializer,
    NotePartReadSerializer
)
from .content import (
    TextReadSerializer,
    ContentReadSerializer
)

class BaseReadSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "id",
            "created_at",
            "updated_at",
        )

class BaseWriteSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True

# scriptorderer
class ScriptOrdererReadSerializer(BaseReadSerializer):
    orderer = OrdererReadSerializer(
        read_only = True
    )

    class Meta(BaseReadSerializer.Meta):
        model = ScriptsOrderer
        fields = BaseReadSerializer.Meta.fields + (
            "orderer",
        )

class ScriptOrdererWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = ScriptsOrderer
        fields = (
            "scripts",
            "orderer",
        )

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

# description
class DescriptionReadSerializer(BaseReadSerializer):
    items = TextReadSerializer(
        source="description_Text",
        many=True,
        read_only = True
    )
    descriptionpart = DescriptionPartReadSerializer(
        read_only = True
    )

    class Meta(BaseReadSerializer.Meta):
        model = Description
        fields = BaseReadSerializer.Meta.fields + (
            "items",
            "descriptionpart",
        )

class DescriptionWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Description
        fields = (
            "scripts",
            "descriptionpart",
        )

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

# note
class NoteReadSerializer(BaseReadSerializer):
    items = ContentReadSerializer(
        source="note_Content",
        many=True,
        read_only = True
    )
    notepart = NotePartReadSerializer(
        read_only = True
    )

    class Meta(BaseReadSerializer.Meta):
        model = Note
        fields = BaseReadSerializer.Meta.fields + (
            "items",
            "notepart",
        )

class NoteWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Note
        fields = (
            "scripts",
            "notepart"
        )