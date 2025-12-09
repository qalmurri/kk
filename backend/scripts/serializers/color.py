from rest_framework import serializers
from scripts.models import Scripts, Purpose, Size, Institute, Orderer, CoverColor, ScriptsOrderer

class CoverColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverColor
        fields = ["id", "color"]

