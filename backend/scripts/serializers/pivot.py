from rest_framework import serializers
from .base import PolicyBasedSerializer
from .user import UserSerializer
from scripts.models import (
    Scripts,
    ScriptsOrderer,
    Status,
    Description,
    Note,
    ScriptsProcess,
    By,
    Orderer
)
from .common import (
    OrdererSerializer,
    SectionSerializer,
    DescriptionPartSerializer,
    LabelSerializer,
    CodeSerializer,
    NotePartSerializer
)
from .content import (
    TextSerializer,
    ContentSerializer
)

class ScriptOrdererSerializer(PolicyBasedSerializer):
    orderer = OrdererSerializer()

    class Meta:
        model = ScriptsOrderer
        fields = [
            "id",
            "orderer",
            "created_at",
            "updated_at"
        ]

class BySerializer(PolicyBasedSerializer):
    user = UserSerializer()

    class Meta:
        model = By
        fields = [
            "id",
            "user",
            "created_at",
            "updated_at"
        ]

class ScriptsProcessSerializer(PolicyBasedSerializer):
    by = BySerializer(
        source="scriptsprocess_By",
        many=True
    )
    section = SectionSerializer()
    class Meta:
        model = ScriptsProcess
        fields = [
            "id",
            "by",
            "section",
            "created_at",
            "updated_at"
        ]
class DescriptionSerializer(PolicyBasedSerializer):
    items = TextSerializer(
        source="description_Text",
        many=True
    )
    descriptionpart = DescriptionPartSerializer()

    class Meta:
        model = Description
        fields = [
            "id",
            "items",
            "descriptionpart",
            "created_at",
            "updated_at"
        ]

class StatusAllSerializer(PolicyBasedSerializer):
    label = LabelSerializer()
    class Meta:
        model = Status
        fields = [
            "id",
            "code",
            "label",
            "updated_at",
            "created_at"
        ]

class StatusSerializer(PolicyBasedSerializer):
    code = CodeSerializer()
    label = LabelSerializer()

    class Meta:
        model = Status
        fields = [
            "id",
            "label",
            "code",
            "created_at",
            "updated_at"
        ]

class NoteSerializer(PolicyBasedSerializer):
    items = ContentSerializer(
        source="note_Content",
        many=True
    )
    notepart = NotePartSerializer()

    class Meta:
        model = Note
        fields = [
            "id",
            "items",
            "notepart",
            "created_at",
            "updated_at"
        ]