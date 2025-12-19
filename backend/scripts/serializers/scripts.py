from .base import PolicyBasedSerializer
from scripts.models import Scripts
from .common import (
    InstituteSerializer,
    SizeSerializer
)
from .content import (
    FlagSerializer,
    ISBNSerializer,
    CoverSerializer
)
from .pivot import (
    ScriptOrdererSerializer,
    StatusSerializer,
    DescriptionSerializer,
    NoteSerializer,
    ScriptsProcessSerializer
)

class ScriptSerializer(PolicyBasedSerializer):
    class Meta:
        model = Scripts
        fields = [
            "id",
            "title",
            "entry_date",
            "created_at"
        ]

class ScriptsSerializer(PolicyBasedSerializer):
    orderers = ScriptOrdererSerializer(
        source="scripts_ScriptsOrderer",
        many=True
    )
    status = StatusSerializer(
        source="scripts_Status",
        many=True
    )
    flag = FlagSerializer(
        source="scripts_Flag",
        many=True
    )
    descriptions = DescriptionSerializer(
        source="scripts_Description",
        many=True
    )
    notes = NoteSerializer(
        source="scripts_Note",
        many=True
    )
    identification = ISBNSerializer(
        source="scripts_ISBN",
        many=True
    )
    process = ScriptsProcessSerializer(
        source="scripts_ScriptsProcess",
        many=True
    )
    cover = CoverSerializer(
        source="scripts_Cover",
        many=True
    )
    institute = InstituteSerializer()
    size = SizeSerializer()

    class Meta:
        model = Scripts
        fields = [
            "id",
            "is_active",
            "title",
            "alias",
            "entry_date",
            "finish_date",
            "orderers",
            "status",
            "flag",
            "descriptions",
            "notes",
            "identification",
            "process",
            "cover",
            "institute",
            "size",
            "created_at",
            "updated_at"
        ]