from scripts.serializers.read import BaseReadSerializer
from scripts.models.script import Script
from .common import (
    InstituteReadSerializer,
    SizeReadSerializer
)
from scripts.serializers.read.base_expandable import ExpandableFieldsMixin
from scripts.serializers.read.mixins import DynamicFieldsMixin

from .flag import FlagReadSerializer
from .isbn import IsbnReadSerializer
from .cover import CoverReadSerializer
from .status import StatusReadSerializer
from .description import DescriptionReadSerializer
from .note import NoteReadSerializer
from .orderer import ScriptOrdererReadSerializer
from .made import MadeReadSerializer

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
    status = StatusReadSerializer(
        source="scripts_Status",
        many=True,
        read_only=True
    )
    flag = FlagReadSerializer(
        source="scripts_Flag",
        many=True,
        read_only=True
    )
    descriptions = DescriptionReadSerializer(
        source="scripts_Description",
        many=True,
        read_only=True
    )
    notes = NoteReadSerializer(
        source="scripts_Note",
        many=True,
        read_only=True
    )
    identification = IsbnReadSerializer(
        source="scripts_ISBN",
        many=True,
        read_only=True
    )
    process = MadeReadSerializer(
        source="scripts_ScriptsProcess",
        many=True,
        read_only=True
    )
    cover = CoverReadSerializer(
        source="scripts_Cover",
        many=True,
        read_only=True
    )

    class Meta(BaseReadSerializer.Meta):
        model = Script
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

# DATA UNTUK TABEL DIBAGI MENJADI BEBERAPA TABS; DATA, COVER! BELUM DI IMPLEMENTASI 
class ScriptSidebarReadSerializer(
        ExpandableFieldsMixin,
        BaseReadSerializer
):
    institute = InstituteReadSerializer(
        read_only=True
    )
    size = SizeReadSerializer(
        read_only = True
    )

    class Meta(BaseReadSerializer.Meta):
        model = Script
        fields = (
            "id",
            "title",
            "alias",
            "is_active",
            "institute",
            "size",
        )

#testing SUDAH IMPLEMENTASI
class ScriptsPartReadSerializer(
    ExpandableFieldsMixin,
    BaseReadSerializer,
):
    institute = InstituteReadSerializer(
        read_only=True
    )

    class Meta(BaseReadSerializer.Meta):
        model = Script
        fields = (
            "id",
            "title",
            "alias",
            "is_active",
            "institute",
        )

# testing SUDAH DI IMPLEMENTASI
class ScriptsCardReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Script
        fields = (
            "id",
            "title",
            "is_active",
        )


