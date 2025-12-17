from .policy_base import PolicyBasedSerializer
from scripts.models import Purpose
from scripts.serializers.code import CodeSerializer

class PurposeAllSerializer(PolicyBasedSerializer):
    class Meta:
        model = Purpose
        fields = ["id", "code", "purpose", "updated_at", "created_at"]

class PurposeSerializer(PolicyBasedSerializer):
    code = CodeSerializer()

    class Meta:
        model = Purpose
        fields = ["id", "code", "label", "created_at", "updated_at"]