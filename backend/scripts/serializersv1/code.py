from .policy_base import PolicyBasedSerializer
from scripts.models import ScriptsStatusCode

class CodeSerializer(PolicyBasedSerializer):
    class Meta:
        model = ScriptsStatusCode
        fields = ["id", "code"]