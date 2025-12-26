from scripts.serializers.base import BaseWriteSerializer
from scripts.models import (
    Orderer,
    ScriptsOrderer
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

class ScriptOrdererWriteSerializer(BaseWriteSerializer):
    '''script orderer write serializer'''
    class Meta(BaseWriteSerializer.Meta):
        model = ScriptsOrderer
        fields = BaseWriteSerializer.Meta.fields + (
            "script",
            "orderer",
        )