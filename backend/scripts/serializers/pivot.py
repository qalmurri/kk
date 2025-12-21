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

class ScriptOrdererSerializer(PolicyBasedSerializer):
    orderer = OrdererReadSerializer()

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
    section = SectionReadSerializer()
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
    items = TextReadSerializer(
        source="description_Text",
        many=True
    )
    descriptionpart = DescriptionPartReadSerializer()

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
    label = LabelReadSerializer()
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
    code = CodeReadSerializer()
    label = LabelReadSerializer()

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
    items = ContentReadSerializer(
        source="note_Content",
        many=True
    )
    notepart = NotePartReadSerializer()

    class Meta:
        model = Note
        fields = [
            "id",
            "items",
            "notepart",
            "created_at",
            "updated_at"
        ]