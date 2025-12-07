from rest_framework import serializers
from .models import Scripts, Purpose, Size, Institute, Orderer

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scripts
        fields = ["id", "title", "entry_date", "orderer", "institute", "created_at"]
    def create(self, validated_data):
        """
        Untuk shell
        """
        return Scripts.objects.create(**validated_data)

# PURPOSE
class PurposeAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ["id", "code", "purpose", "updated_at", "created_at"]

class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ["id", "purpose"]

# SIZE
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["id", "size"]

# INSTITUTE
class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ["id", "institute"]

# ORDERER
class OrdererAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderer
        fields = ["id", "orderer", "no", "institute", "updated_at", "created_at"]