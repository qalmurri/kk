from .policy_base import PolicyBasedSerializer
from rest_framework import serializers
from scripts.models import Scripts, ScriptsOrderer, Orderer
from .orderer import OrdererSerializer
from .institute import InstituteSerializer
from .size import SizeSerializer
from .purpose import PurposeSerializer
from .isbn import ISBNSerializer
from .bool import BoolSerializer
from .description import DescriptionSerializer

class ScriptSerializer(PolicyBasedSerializer):
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
        fields = ["id", "orderer", "created_at", "updated_at"]
       
class ScriptsSerializer(serializers.ModelSerializer):
    orderers = ScriptOrdererSerializer(
        source="scripts_ScriptsOrderer", many=True
    )
    purpose = PurposeSerializer(
        source="scripts_Purpose", many=True
    )
    bool = BoolSerializer(
        source="scripts_Bool", many=True
    )
    description = DescriptionSerializer(
        source="scripts_Description", many=True
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