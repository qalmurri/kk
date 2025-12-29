from scripts.serializers.write import BaseWriteSerializer
from scripts.models.script import Script

SCRIPTS_BASE_FIELDS = (
            "title",
            "alias",
            "is_active",
            "entry_date",
            "finish_date",
            "institute",
            "size",
)

class ScriptsWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Script
        fields = SCRIPTS_BASE_FIELDS