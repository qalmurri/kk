from scripts.models import Size
from .policy_base import PolicyBasedSerializer

class SizeSerializer(PolicyBasedSerializer):
    class Meta:
        model = Size
        fields = ["id", "size", "created_at", "updated_at"]


