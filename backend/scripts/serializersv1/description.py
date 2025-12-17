from scripts.models import Description
from .policy_base import PolicyBasedSerializer

class DescriptionSerializer(PolicyBasedSerializer):
    class Meta:
        model = Description
        fields = ["id", "description", "label", "created_at", "updated_at"]