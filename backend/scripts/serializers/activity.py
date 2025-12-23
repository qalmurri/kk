from .base import PolicyBasedSerializer
from scripts.models import ActivityLog

class ActivitySerializer(PolicyBasedSerializer):
    class Meta:
        model = ActivityLog
        fields = (
            "id",
            "user",
            "model_name",
            "object_id",
            "action",
            "changes",
            "created_at"
        )