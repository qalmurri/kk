from rest_framework import serializers
from scripts.models import ScriptsStatusCode

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptsStatusCode
        fields = ["id", "code"]