from .policy_base import PolicyBasedSerializer
from scripts.models import ISBN

class ISBNSerializer(PolicyBasedSerializer):
    class Meta:
        model = ISBN
        fields = ["id", "isbn", "code", "created_at", "updated_at"]