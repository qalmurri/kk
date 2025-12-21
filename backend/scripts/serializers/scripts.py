from .base import PolicyBasedSerializer
from scripts.models import Scripts
from .common import (
    InstituteReadSerializer,
    SizeReadSerializer
)
from .content import (
    FlagReadSerializer,
    ISBNReadSerializer,
    CoverBookReadSerializer
)
from .pivot import (
    ScriptOrdererReadSerializer,
    StatusSerializer,
    DescriptionSerializer,
    NoteSerializer,
    ScriptsProcessReadSerializer
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

SCRIPTS_BASE_FIELDS = (
            "title",
            "alias",
            "is_active",
            "entry_date",
            "finish_date",
            "institute",
            "size",
)

class ScriptsReadSerializer(BaseReadSerializer):
    institute = InstituteReadSerializer(
        read_only=True
    )
    size = SizeReadSerializer(
        read_only=True
    )

    orderers = ScriptOrdererReadSerializer(
        source="scripts_ScriptsOrderer",
        many=True,
        read_only=True
    )
    status = StatusSerializer(
        source="scripts_Status",
        many=True,
        read_only=True
    )
    flag = FlagReadSerializer(
        source="scripts_Flag",
        many=True,
        read_only=True
    )
    descriptions = DescriptionSerializer(
        source="scripts_Description",
        many=True,
        read_only=True
    )
    notes = NoteSerializer(
        source="scripts_Note",
        many=True,
        read_only=True
    )
    identification = ISBNReadSerializer(
        source="scripts_ISBN",
        many=True,
        read_only=True
    )
    process = ScriptsProcessReadSerializer(
        source="scripts_ScriptsProcess",
        many=True,
        read_only=True
    )
    cover = CoverBookReadSerializer(
        source="scripts_Cover",
        many=True,
        read_only=True
    )

    class Meta(BaseReadSerializer.Meta):
        model = Scripts
        fields = BaseReadSerializer.Meta.fields + SCRIPTS_BASE_FIELDS + (
            "orderers",
            "status",
            "flag",
            "descriptions",
            "notes",
            "identification",
            "process",
            "cover",
        )

class ScriptsWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Scripts
        fields = SCRIPTS_BASE_FIELDS