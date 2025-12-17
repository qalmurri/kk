from .policy_base import PolicyBasedSerializer
from scripts.models import Institute

class InstituteSerializer(PolicyBasedSerializer):
    class Meta:
        model = Institute
        fields = ["id", "institute", "created_at", "updated_at"]