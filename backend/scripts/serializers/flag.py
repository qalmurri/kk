from .base import PolicyBasedSerializer, BaseReadSerializer
from scripts.models import Flag, Part

class BaseWriteSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True

class BaseWriteSerializer2(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "name",
        )

# part
class PartReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Part
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class PartWriteSerializer(BaseWriteSerializer2):
    class Meta(BaseWriteSerializer.Meta):
        model = Part

# flag
class FlagReadSerializer(BaseReadSerializer):
    part = PartReadSerializer(
        read_only=True
    )

    class Meta(BaseReadSerializer):
        model = Flag
        fields = BaseReadSerializer.Meta.fields + (
            "is_active",
            "part",
        )

class FlagWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Flag
        fields = (
            "scripts",
            "is_active",
            "part",
        )