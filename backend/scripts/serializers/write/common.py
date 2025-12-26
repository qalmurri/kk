from scripts.serializers.base import BaseWriteSerializer
from scripts.models import (
    Size,
    Institute
)

class SizeWriteSerializer(BaseWriteSerializer):
    '''size write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Size
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

class InstituteWriteSerializer(BaseWriteSerializer):
    '''institute write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Institute
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )