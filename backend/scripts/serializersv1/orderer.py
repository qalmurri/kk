from .policy_base import PolicyBasedSerializer
from scripts.models import Orderer
from .institute import InstituteSerializer

class OrdererAllSerializer(PolicyBasedSerializer):
    class Meta:
        model = Orderer
        fields = ["id", "orderer", "no", "institute", "updated_at", "created_at"]

class OrdererSerializer(PolicyBasedSerializer):
    institute = InstituteSerializer()

    class Meta:
        model = Orderer
        fields = ["id", "name", "no", "institute", "created_at", "updated_at"]