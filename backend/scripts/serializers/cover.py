from .base import BaseReadSerializer, BaseWriteSerializer
from scripts.models import Cover

cover_fields = (
    "thumbnail",
    "length",
    "height",
    "width",
    "x_axis",
    "y_axis",
)

# COVER READ & WRITE
class CoverReadSerializer(BaseReadSerializer):
    '''cover read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Cover
        fields = BaseReadSerializer.Meta.fields + cover_fields

class CoverWriteSerializer(BaseWriteSerializer):
    '''cover read serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Cover
        fields = BaseWriteSerializer.Meta.fields + cover_fields + (
            "scripts",
        )