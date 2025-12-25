from .base import PolicyBasedSerializer
from scripts.models import Size, Institute

class BaseReadSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "id",
            "created_at",
            "updated_at",
        )

class BaseWriteSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "name",
        )

# size
class SizeReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Size
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class SizeWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Size

# institute
class InstituteReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Institute
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class InstituteWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Institute