from .base import (
    BaseReadSerializer,
    BaseWriteSerializer
)
from scripts.models import (
    Size,
    Institute
)

# SIZE READ & WRITE
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

# INSTITUTE READ & WRITE
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