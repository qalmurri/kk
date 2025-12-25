from .base import BaseWriteSerializer, BaseReadSerializer
from scripts.models import Type, Isbn

class TypeReadSerializer(BaseReadSerializer):
    '''type read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Type
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class TypeWriteSerializer(BaseWriteSerializer):
    '''type write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Type
        fields = BaseWriteSerializer.Meta.fields + (
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
            "isbn",
            "type",
        )

class IsbnWriteSerializer(BaseWriteSerializer):
    '''isbn write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Isbn
        fields = BaseReadSerializer.Meta.fields + (
            "script",
            "isbn",
            "type",
        )