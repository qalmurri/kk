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

class ScriptsReadSerializer(PolicyBasedSerializer):
    institute = InstituteSerializer()
    size = SizeSerializer()

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
    flag = FlagSerializer(
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
    identification = ISBNSerializer(
        source="scripts_ISBN",
        many=True,
        read_only=True
    )
    process = ScriptsProcessSerializer(
        source="scripts_ScriptsProcess",
        many=True,
        read_only=True
    )
    cover = CoverSerializer(
        source="scripts_Cover",
        many=True,
        read_only=True
    )

    class Meta:
        model = Scripts
        fields = [
            "id",
            "title",
            "alias",
            "is_active",
            "entry_date",
            "finish_date",
            
            "institute",
            "size",

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
        ]

class ScriptsWriteSerializer(PolicyBasedSerializer):
#    institute = serializers.PrimaryKeyRelatedField(
#        queryset=Institute.objects.all(),
#        required=False
#    )
#    size = serializers.PrimaryKeyRelatedField(
#        queryset=Size.objects.all(),
#        required=False
#    )

    class Meta:
        model = Scripts
        fields = [
            "title", 
            "alias", 
            "is_active", 
            "entry_date", 
            "finish_date",

            "institute", 
            "size"
        ]