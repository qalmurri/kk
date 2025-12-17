from rest_framework import serializers
from django.shortcuts import get_object_or_404
from scripts.models import (
    Size, Scripts, ScriptsOrderer, Orderer,
    Purpose, ISBN, Institute, Description,
    ScriptsStatusCode, Bool, CoverColor
)

class PolicyBasedSerializer(serializers.ModelSerializer):
    PROTECTED_FIELDS = set()

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields) - self.PROTECTED_FIELDS
            existing = set(self.fields)

            invalid = allowed - existing
            if invalid:
                raise serializers.ValidationError(
                    f"Invalid fields requested: {invalid}"
                )

            for field in existing - allowed:
                self.fields.pop(field)

# BASIC SERIALIZERS

class SizeSerializer(PolicyBasedSerializer):
    class Meta:
        model = Size
        fields = ["id", "size", "created_at", "updated_at"]

class InstituteSerializer(PolicyBasedSerializer):
    class Meta:
        model = Institute
        fields = ["id", "institute", "created_at", "updated_at"]

class CodeSerializer(PolicyBasedSerializer):
    class Meta:
        model = ScriptsStatusCode
        fields = ["id", "code"]

class PurposeSerializer(PolicyBasedSerializer):
    code = CodeSerializer()

    class Meta:
        model = Purpose
        fields = ["id", "code", "label", "created_at", "updated_at"]

class BoolSerializer(PolicyBasedSerializer):
    class Meta:
        model = Bool
        fields = ["id", "boolean", "label", "created_at", "updated_at"]

class DescriptionSerializer(PolicyBasedSerializer):
    class Meta:
        model = Description
        fields = ["id", "description", "label", "created_at", "updated_at"]

class ISBNSerializer(PolicyBasedSerializer):
    class Meta:
        model = ISBN
        fields = ["id", "isbn", "code", "created_at", "updated_at"]

class CoverColorSerializer(PolicyBasedSerializer):
    class Meta:
        model = CoverColor
        fields = ["id", "color"]

# ORDERER

class OrdererSerializer(PolicyBasedSerializer):
    institute = InstituteSerializer()

    class Meta:
        model = Orderer
        fields = ["id", "name", "no", "institute", "created_at", "updated_at"]

class ScriptOrdererSerializer(PolicyBasedSerializer):
    orderer = OrdererSerializer()

    class Meta:
        model = ScriptsOrderer
        fields = ["id", "orderer", "created_at", "updated_at"]

class ScriptOrdererCreateSerializer(PolicyBasedSerializer): ####DONEEEE!
    scripts = serializers.PrimaryKeyRelatedField(queryset=Scripts.objects.all())
    orderer = serializers.PrimaryKeyRelatedField(queryset=Orderer.objects.all())

    class Meta:
        model = ScriptsOrderer
        fields = [
            "id",
            "scripts",
            "orderer",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

# SCRIPTS

class ScriptSerializer(PolicyBasedSerializer):
    class Meta:
        model = Scripts
        fields = ["id", "title", "entry_date", "created_at"]

class ScriptsSerializer(PolicyBasedSerializer):
    orderers = ScriptOrdererSerializer(
        source="scripts_ScriptsOrderer",
        many=True
    )
    purpose = PurposeSerializer(
        source="scripts_Purpose",
        many=True
    )
    bool = BoolSerializer(
        source="scripts_Bool",
        many=True
    )
    description = DescriptionSerializer(
        source="scripts_Description",
        many=True
    )
    identification = ISBNSerializer(
        source="scripts_ISBN",
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
            "entry_date",
            "finish_date",
            "orderers",
            "purpose",
            "bool",
            "description",
            "identification",
            "institute",
            "size",
            "created_at",
            "updated_at"
        ]


# PIVOT

class PurposeAllSerializer(PolicyBasedSerializer):
    class Meta:
        model = Purpose
        fields = ["id", "code", "purpose", "updated_at", "created_at"]

class OrdererAllSerializer(PolicyBasedSerializer):
    class Meta:
        model = Orderer
        fields = ["id", "orderer", "no", "institute", "updated_at", "created_at"]



