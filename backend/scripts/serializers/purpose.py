from rest_framework import serializers
from scripts.models import Purpose

class PurposeAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ["id", "code", "purpose", "updated_at", "created_at"]

class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ["id", "purpose"]