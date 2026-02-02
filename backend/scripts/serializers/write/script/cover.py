from scripts.serializers.write import BaseWriteSerializer
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

class CoverWriteSerializer(BaseWriteSerializer):
    '''cover read serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Cover
        fields = BaseWriteSerializer.Meta.fields + cover_fields + (
            "scripts",
        )
