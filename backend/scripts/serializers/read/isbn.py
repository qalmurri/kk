from scripts.serializers.base import BaseReadSerializer
from scripts.models import (
    Type,
    Isbn
)

class TypeIsbnReadSerializer(BaseReadSerializer):
    '''type read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Type
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class IsbnReadSerializer(BaseReadSerializer):
    '''isbn read serializer'''
    typeisbn = TypeIsbnReadSerializer(
        read_only=True
    )
    class Meta(BaseReadSerializer.Meta):
        model = Isbn
        fields = BaseReadSerializer.Meta.fields + (
            "isbn",
            "typeisbn",
        )