from scripts.serializers.base import BaseReadSerializer
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
    '''cover read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Cover
        fields = BaseReadSerializer.Meta.fields + cover_fields