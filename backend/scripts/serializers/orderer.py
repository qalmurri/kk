from rest_framework import serializers
from scripts.models import Orderer, CoverColor, ScriptsOrderer
from .institute import InstituteSerializer

class OrdererAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderer
        fields = ["id", "orderer", "no", "institute", "updated_at", "created_at"]

class OrdererSerializer(serializers.ModelSerializer):
    institute = InstituteSerializer()

    class Meta:
        model = Orderer
        fields = ["id", "name", "no", "institute"]