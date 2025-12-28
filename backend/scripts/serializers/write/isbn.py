from scripts.serializers.base import BaseWriteSerializer
from scripts.models import (
    TypeIsbn,
    Isbn
)

class TypeIsbnWriteSerializer(BaseWriteSerializer):
    '''type write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = TypeIsbn
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
        )

class IsbnWriteSerializer(BaseWriteSerializer):
    '''isbn write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Isbn
        fields = BaseWriteSerializer.Meta.fields + (
            "script",
            "isbn",
            "typeisbn",
        )