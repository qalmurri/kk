from rest_framework import serializers
from scripts.models import Size

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["id", "size", "created_at", "updated_at"]


