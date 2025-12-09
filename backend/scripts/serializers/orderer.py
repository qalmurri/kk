from rest_framework import serializers
from scripts.models import Scripts, Purpose, Size, Institute, Orderer, CoverColor, ScriptsOrderer
from .institute import InstituteSerializer

class OrdererAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderer
        fields = ["id", "orderer", "no", "institute", "updated_at", "created_at"]

class OrdererSerializer(serializers.ModelSerializer):
    institute = InstituteSerializer()

    def get_institute(self, obj):
        return obj.institute.institute if obj.institute else ""

    class Meta:
        model = Orderer
        fields = ["id", "orderer", "no", "institute"]