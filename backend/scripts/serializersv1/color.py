from .policy_base import PolicyBasedSerializer
from scripts.models import CoverColor

class CoverColorSerializer(PolicyBasedSerializer):
    class Meta:
        model = CoverColor
        fields = ["id", "color"]

