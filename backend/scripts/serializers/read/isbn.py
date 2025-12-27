from scripts.serializers.base import BaseReadSerializer
from scripts.models import (
    Type,
    Isbn
)

class TypeReadSerializer(BaseReadSerializer):
    '''type read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Type
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class IsbnReadSerializer(BaseReadSerializer):
    '''isbn read serializer'''
    type = TypeReadSerializer(
        read_only=True
    )
    class Meta(BaseReadSerializer.Meta):
        model = Isbn
        fields = BaseReadSerializer.Meta.fields + (
            "type",
            "isbn",
        )