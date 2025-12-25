from .base import BaseReadSerializer, BaseWriteSerializer
from .common import InstituteReadSerializer
from scripts.models import Orderer, ScriptsOrderer

# ORDERER READ & WRITE
class OrdererReadSerializer(BaseReadSerializer):
    '''orderer read serializer'''
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

class OrdererWriteSerializer(BaseWriteSerializer):
    '''orderer write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = Orderer
        fields = BaseWriteSerializer.Meta.fields + (
            "name",
            "no",
            "institute",
        )

# SCRIPTORDERER READ & WRITE
class ScriptOrdererReadSerializer(BaseReadSerializer):
    '''script orderer read serializer'''
    orderer = OrdererReadSerializer(
        read_only = True
    )
    class Meta(BaseReadSerializer.Meta):
        model = ScriptsOrderer
        fields = BaseReadSerializer.Meta.fields + (
            "orderer",
        )

class ScriptOrdererWriteSerializer(BaseWriteSerializer):
    '''script orderer write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = ScriptsOrderer
        fields = BaseWriteSerializer.Meta.fields + (
            "script",
            "orderer",
        )