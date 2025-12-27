from scripts.serializers.base import BaseWriteSerializer
from scripts.models import (
    Type,
    Isbn
)

class TypeWriteSerializer(BaseWriteSerializer):
    '''type write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Type
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
            "type",
        )