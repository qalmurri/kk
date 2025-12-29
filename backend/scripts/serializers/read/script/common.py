from scripts.serializers.base import BaseReadSerializer
from scripts.models.script import (
    Size,
    Institute
)

class SizeReadSerializer(BaseReadSerializer):
    '''size read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Size
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class InstituteReadSerializer(BaseReadSerializer):
    '''institute read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Institute
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )