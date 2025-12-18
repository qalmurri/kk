from django.contrib.auth import get_user_model
from rest_framework import serializers
from scripts.models import (
    Size,
    Scripts,
    ScriptsOrderer,
    Orderer,
    Status,
    ISBN,
    Institute,
    Description,
    ScriptsStatusCode,
    Flag,
    Note,
    ScriptsProcess,
    By,
    Content,
    Text,
    Label,
    Type,
    Cover
)

User = get_user_model()

COMPACT_FIELD_MAP = {
    #timestampt
    "created_at": "a",
    "updated_at": "b",
    "is_active": "i",
    "title": "e",
    "alias": "a_",
    "entry_date": "f",
    "finish_date": "g",
    "orderer": "o",
    "text": "c",
    "content": "d",
    "code": "h",
    "institute": "j",
    "isbn": "k",
    "label": "l",
    "no": "m",
    "name": "n",
    "size": "p",
    "type": "q",
    "user": "r",
    "height": "s",
    "thumbnail": "t",
    "length": "u",
    "width": "v",
    "x_axis": "w",
    "y_axis": "x",
}

class BaseCompactSerializer(serializers.ModelSerializer):
    pass
#    def get_fields(self):
#        fields = super().get_fields()
#        compacted = {}
#
#        for field_name, field in fields.items():
#            if field_name == "id":
#                compacted[field_name] = field
#                continue
#
#            short_name = COMPACT_FIELD_MAP.get(field_name)
#            if short_name:
#                field.source = field_name
#                compacted[short_name] = field
#            else:
#                compacted[field_name] = field
#        return compacted
#   
#    def to_representation(self, instance):
#        data = super().to_representation(instance)
#        return {
#            k: v for k, v in data.items()
#            if v not in (None, [], {})
#        }

class PolicyBasedSerializer(BaseCompactSerializer):
    PROTECTED_FIELDS = set()

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop(
            "fields",
            None
        )
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(
                fields
            ) - self.PROTECTED_FIELDS
            existing = set(
                self.fields
            )

            invalid = allowed - existing
            if invalid:
                raise serializers.ValidationError(
                    f"Invalid fields requested: {invalid}"
                )

            for field in existing - allowed:
                self.fields.pop(
                    field
                )

# BASIC SERIALIZERS

class ContentSerializer(PolicyBasedSerializer):
    class Meta:
        model = Content
        fields = [
            "id",
            "content",
            "created_at",
            "updated_at"
        ]

class TextSerializer(PolicyBasedSerializer):
    class Meta:
        model = Text
        fields = [
            "id",
            "text",
            "created_at",
            "updated_at"
        ]

class SizeSerializer(PolicyBasedSerializer):
    class Meta:
        model = Size
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at"
        ]

class InstituteSerializer(PolicyBasedSerializer):
    class Meta:
        model = Institute
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at"
        ]

class LabelSerializer(PolicyBasedSerializer):
    class Meta:
        model = Label
        fields = [
            "id",
            "name"
        ]

class CodeSerializer(PolicyBasedSerializer):
    class Meta:
        model = ScriptsStatusCode
        fields = [
            "id",
            "name"
        ]

class TypeSerializer(PolicyBasedSerializer):
    class Meta:
        model = Type
        fields = [
            "id",
            "name"
        ]

class CoverSerializer(PolicyBasedSerializer):
    class Meta:
        model = Cover
        fields = [
            "id",
            "thumbnail",
            "length",
            "height",
            "width",
            "x_axis",
            "y_axis",
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

class FlagSerializer(PolicyBasedSerializer):
    label = LabelSerializer()

    class Meta:
        model = Flag
        fields = [
            "id",
            "is_active",
            "label",
            "created_at",
            "updated_at"
        ]

class DescriptionSerializer(PolicyBasedSerializer):
    items = TextSerializer(
        source="description_Text",
        many=True
    )
    label = LabelSerializer()

    class Meta:
        model = Description
        fields = [
            "id",
            "items",
            "label",
            "created_at",
            "updated_at"
        ]

class NoteSerializer(PolicyBasedSerializer):
    items = ContentSerializer(
        source="note_Content",
        many=True
    )
    label = LabelSerializer()

    class Meta:
        model = Note
        fields = [
            "id",
            "items",
            "label",
            "created_at",
            "updated_at"
        ]

class ISBNSerializer(PolicyBasedSerializer):
    type = TypeSerializer()

    class Meta:
        model = ISBN
        fields = [
            "id",
            "isbn",
            "type",
            "created_at",
            "updated_at"
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username"
        ]

# ORDERER

class OrdererSerializer(PolicyBasedSerializer):
    institute = InstituteSerializer()

    class Meta:
        model = Orderer
        fields = [
            "id",
            "name",
            "no",
            "institute",
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
    label = LabelSerializer()
    class Meta:
        model = ScriptsProcess
        fields = [
            "id",
            "by",
            "label",
            "created_at",
            "updated_at"
        ]

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

class ScriptOrdererCreateSerializer(PolicyBasedSerializer):
    scripts = serializers.PrimaryKeyRelatedField(queryset=Scripts.objects.all())
    orderer = serializers.PrimaryKeyRelatedField(queryset=Orderer.objects.all())

    class Meta:
        model = ScriptsOrderer
        fields = [
            "id",
            "scripts",
            "orderer",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at"
        ]

# SCRIPTS

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


# PIVOT

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

class OrdererAllSerializer(PolicyBasedSerializer):
    class Meta:
        model = Orderer
        fields = [
            "id",
            "orderer",
            "no",
            "institute",
            "updated_at",
            "created_at"
        ]