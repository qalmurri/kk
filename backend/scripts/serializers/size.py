from rest_framework import serializers
from scripts.models import Scripts, Purpose, Size, Institute, Orderer, CoverColor, ScriptsOrderer

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["id", "size"]


