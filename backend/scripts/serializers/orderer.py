from .base import BaseReadSerializer, PolicyBasedSerializer
from .common import InstituteReadSerializer
from scripts.models import Orderer, ScriptsOrderer

class BaseWriteSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True

class BaseWriteSerializer2(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "name",
        )

# orderer
class OrdererReadSerializer(BaseReadSerializer):
    institute = InstituteReadSerializer(
        read_only=True
    )

    class Meta(BaseReadSerializer.Meta):
        model = Orderer
        fields = BaseReadSerializer.Meta.fields + (
            "name",
            "no",
            "institute"
        )

class OrdererWriteSerializer(BaseWriteSerializer2):
    class Meta(BaseWriteSerializer2.Meta):
        model = Orderer
        fields = BaseWriteSerializer2.Meta.fields + (
            "no",
            "institute",
        )

# scriptorderer
class ScriptOrdererReadSerializer(BaseReadSerializer):
    orderer = OrdererReadSerializer(
        read_only = True
    )

    class Meta(BaseReadSerializer.Meta):
        model = ScriptsOrderer
        fields = BaseReadSerializer.Meta.fields + (
            "orderer",
        )

class ScriptOrdererWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = ScriptsOrderer
        fields = (
            "scripts",
            "orderer",
        )