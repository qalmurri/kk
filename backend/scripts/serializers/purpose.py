from rest_framework import serializers
from scripts.models import Scripts, Purpose, Size, Institute, Orderer, CoverColor, ScriptsOrderer

class PurposeAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ["id", "code", "purpose", "updated_at", "created_at"]

class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ["id", "purpose"]