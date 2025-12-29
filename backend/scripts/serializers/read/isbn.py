from scripts.serializers.base import BaseReadSerializer
from scripts.models.script import (
    TypeIsbn,
    Isbn
)

class TypeIsbnReadSerializer(BaseReadSerializer):
    '''type read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = TypeIsbn
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
            "typeisbn",
            "isbn",
        )