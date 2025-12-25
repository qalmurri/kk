from .base import PolicyBasedSerializer, BaseReadSerializer
from scripts.models import Type, ISBN

class BaseWriteSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True

class BaseWriteSerializer2(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "name",
        )

# type
class TypeReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Type
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class TypeWriteSerializer(BaseWriteSerializer2):
    class Meta(BaseWriteSerializer.Meta):
        model = Type

# isbn
class ISBNReadSerializer(BaseReadSerializer):
    type = TypeReadSerializer(
        read_only=True
    )

    class Meta(BaseReadSerializer.Meta):
        model = ISBN
        fields = BaseReadSerializer.Meta.fields + (
            "isbn",
            "type",
        )

class ISBNWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = ISBN
        fields = (
            "scripts",
            "isbn",
            "type",
        )