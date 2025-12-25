from .base import BaseReadSerializer, PolicyBasedSerializer
from scripts.models import Cover

cover_fields = (
    "thumbnail",
    "length",
    "height",
    "width",
    "x_axis",
    "y_axis",
)

class CoverReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Cover
        fields = BaseReadSerializer.Meta.fields + cover_fields

class CoverWriteSerializer(PolicyBasedSerializer):
    class Meta:
        model = Cover
        fields = (
            "scripts",
        ) + cover_fields