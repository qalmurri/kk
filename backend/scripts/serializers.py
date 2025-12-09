from rest_framework import serializers
from .models import Scripts, Purpose, Size, Institute, Orderer, CoverColor, ScriptOrderer

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scripts
        fields = ["id", "title", "entry_date", "created_at"]

    def create(self, validated_data):
        """
        Untuk shell
        """
        return Scripts.objects.create(**validated_data)

class PurposeAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ["id", "code", "purpose", "updated_at", "created_at"]

class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ["id", "purpose"]

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["id", "size"]

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ["id", "institute"]

class OrdererAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderer
        fields = ["id", "orderer", "no", "institute", "updated_at", "created_at"]

class OrdererSerializer(serializers.ModelSerializer):
    institute = serializers.SerializerMethodField()

    def get_institute(self, obj):
        return obj.institute.institute if obj.institute else ""

    class Meta:
        model = Orderer
        fields = ["id", "orderer", "no", "institute"]

class ScriptOrdererSerializer(serializers.ModelSerializer):
    orderer = OrdererSerializer()

    class Meta:
        model = ScriptOrderer
        fields = ["id", "orderer"]

class ScriptsSerializer(serializers.ModelSerializer):
    orderers = ScriptOrdererSerializer(
        source="scripts_ScriptOrderer", many=True
    )

    class Meta:
        model = Scripts
        fields = [
            "id",
            "title",
            "entry_date",
            "orderers"
        ]

class CoverColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverColor
        fields = ["id", "color"]

class ScriptOrdererCreateSerializer(serializers.ModelSerializer):
    scripts_id = serializers.IntegerField(write_only=True)
    orderer_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ScriptOrderer
        fields = [
            "id",
            "scripts_id",
            "orderer_id",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        scripts = Scripts.objects.get(id=validated_data["scripts_id"])
        orderer = Orderer.objects.get(id=validated_data["orderer_id"])

        return ScriptOrderer.objects.create(
            scripts=scripts,
            orderer=orderer
        )