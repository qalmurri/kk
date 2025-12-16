from rest_framework import serializers
from scripts.models import Description

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ["id", "description", "label", "created_at", "updated_at"]