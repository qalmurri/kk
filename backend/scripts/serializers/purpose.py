from rest_framework import serializers
from scripts.models import Purpose
from scripts.serializers.code import CodeSerializer

class PurposeAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ["id", "code", "purpose", "updated_at", "created_at"]

class PurposeSerializer(serializers.ModelSerializer):
    code = CodeSerializer()

    class Meta:
        model = Purpose
        fields = ["id", "code", "label", "created_at", "updated_at"]