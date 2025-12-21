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

# description
class DescriptionSerializer(BaseReadSerializer):
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

# statusall
class StatusAllSerializer(BaseReadSerializer):
    label = LabelReadSerializer(
        read_only = True
    )
    class Meta(BaseReadSerializer.Meta):
        model = Status
        fields = BaseReadSerializer.Meta.fields + (
            "code",
            "label",
        )

# status
class StatusSerializer(BaseReadSerializer):
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

# note
class NoteSerializer(BaseReadSerializer):
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