from scripts.serializers.read import BaseReadSerializer
from scripts.models.script import Cover

cover_fields = (
    "thumbnail",
    "length",
    "height",
    "width",
    "x_axis",
    "y_axis",
    "zoom",
)

class CoverReadSerializer(BaseReadSerializer):
    '''cover read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Cover
        fields = BaseReadSerializer.Meta.fields + cover_fields
