from rest_framework import serializers
from scripts.models import ISBN

class ISBNSerializer(serializers.ModelSerializer):
    class Meta:
        model = ISBN
        fields = ["id", "isbn", "code"]