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
    ScriptOrdererSerializer,
    StatusSerializer,
    DescriptionSerializer,
    NoteSerializer,
    ScriptsProcessSerializer
)

SCRIPTS_BASE_FIELDS = (
            "id",
            "title",
            "alias",
            "is_active",
            "entry_date",
            "finish_date",
            
            "institute",
            "size",
)

class ScriptsReadSerializer(PolicyBasedSerializer):
    institute = InstituteReadSerializer()
    size = SizeReadSerializer()

    orderers = ScriptOrdererSerializer(
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
    process = ScriptsProcessSerializer(
        source="scripts_ScriptsProcess",
        many=True,
        read_only=True
    )
    cover = CoverBookReadSerializer(
        source="scripts_Cover",
        many=True,
        read_only=True
    )

    class Meta:
        model = Scripts
        fields = SCRIPTS_BASE_FIELDS + (
            "orderers",
            "status",
            "flag",
            "descriptions",
            "notes",
            "identification",
            "process",
            "cover",
            "created_at",
            "updated_at"
        )

class ScriptsWriteSerializer(PolicyBasedSerializer):
    class Meta:
        model = Scripts
        fields = SCRIPTS_BASE_FIELDS
        read_only_fields = (
            "id",
        )