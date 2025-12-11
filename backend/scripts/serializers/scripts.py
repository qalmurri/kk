from rest_framework import serializers
from scripts.models import Scripts, ScriptsOrderer, Orderer, ScriptsStatus
from .orderer import OrdererSerializer
from .institute import InstituteSerializer
from .size import SizeSerializer
from .code import CodeSerializer
from .purpose import PurposeSerializer
from .isbn import ISBNSerializer

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scripts
        fields = ["id", "title", "entry_date", "created_at"]

    def create(self, validated_data):
        """
        Untuk shell
        """
        return Scripts.objects.create(**validated_data)
    
class ScriptOrdererSerializer(serializers.ModelSerializer):
    orderer = OrdererSerializer()

    class Meta:
        model = ScriptsOrderer
        fields = ["id", "orderer"]

class ScriptsStatusSerializer(serializers.ModelSerializer):
    purpose = PurposeSerializer()

    class Meta:
        model = ScriptsStatus
        fields = [
            "id",
            "purpose"
        ]
        
class ScriptsSerializer(serializers.ModelSerializer):
    orderers = ScriptOrdererSerializer(
        source="scripts_ScriptsOrderer", many=True
    )
    status = ScriptsStatusSerializer(
        source="scripts_ScriptsStatus", many=True
    )
    identification = ISBNSerializer(
        source="scripts_ISBN", many=True
    )
    institute = InstituteSerializer()
    size = SizeSerializer()

    class Meta:
        model = Scripts
        fields = [
            "id",
            "title",
            "entry_date",
            "orderers",
            "status",
            "identification",
            "institute",
            "size"
        ]

class ScriptOrdererCreateSerializer(serializers.ModelSerializer):
    scripts_id = serializers.IntegerField(write_only=True)
    orderer_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ScriptsOrderer
        fields = [
            "id",
            "scripts_id",
            "orderer_id",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        scripts = Scripts.objects.get(id=validated_data["scripts_id"])
        orderer = Orderer.objects.get(id=validated_data["orderer_id"])

        return ScriptsOrderer.objects.create(
            scripts=scripts,
            orderer=orderer
        )