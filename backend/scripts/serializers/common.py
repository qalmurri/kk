from .base import PolicyBasedSerializer, BaseReadSerializer, BaseWriteSerializer
from scripts.models import Size, Institute

class SizeReadSerializer(BaseReadSerializer):
    '''size read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Size
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class SizeWriteSerializer(PolicyBasedSerializer):
    '''size write serializer'''
    class Meta:
        model = Size
        fields = (
            "name",
        )

# institute
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