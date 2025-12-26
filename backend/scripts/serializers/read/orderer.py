from scripts.serializers.base import BaseReadSerializer
from .common import InstituteReadSerializer
from scripts.models import (
    Orderer,
    ScriptsOrderer
)

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