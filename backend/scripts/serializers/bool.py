from rest_framework import serializers
from scripts.models import Bool

class BoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bool
        fields = ["id", "boolean", "label", "created_at", "updated_at"]