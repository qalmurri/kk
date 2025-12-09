from rest_framework import serializers
from scripts.models import CoverColor

class CoverColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverColor
        fields = ["id", "color"]

