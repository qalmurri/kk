from scripts.models import Bool
from .policy_base import PolicyBasedSerializer

class BoolSerializer(PolicyBasedSerializer):
    class Meta:
        model = Bool
        fields = ["id", "boolean", "label", "created_at", "updated_at"]