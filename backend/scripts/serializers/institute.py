from rest_framework import serializers
from scripts.models import Scripts, Purpose, Size, Institute, Orderer, CoverColor, ScriptsOrderer

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ["id", "institute"]

