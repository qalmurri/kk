from .base import BaseReadSerializer, BaseWriteSerializer
from scripts.models import Size, Institute

class SizeReadSerializer(BaseReadSerializer):
    '''size read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Size
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class SizeWriteSerializer(BaseWriteSerializer):
    '''size write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Size
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

class InstituteReadSerializer(BaseReadSerializer):
    '''institute read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Institute
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class InstituteWriteSerializer(BaseWriteSerializer):
    '''institute write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Institute
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )