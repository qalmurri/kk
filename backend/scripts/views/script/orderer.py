from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.read.script import (
    OrdererReadSerializer,
    ScriptOrdererReadSerializer
    )
from scripts.serializers.write.script import (
    OrdererWriteSerializer,
    ScriptOrdererWriteSerializer
    )
from scripts.repositories.command.script import (
    OrdererCommandRepository,
    ScriptsOrdererCommandRepository
    )
from scripts.repositories.query.script import (
    OrdererQueryRepository,
    ScriptsOrdererQueryRepository
    )

class OrdererViewSet(BaseCRUDViewSet):
    '''orderer viewset'''
    read_serializer_class = OrdererReadSerializer
    write_serializer_class = OrdererWriteSerializer
    query_repo = OrdererQueryRepository
    command_repo = OrdererCommandRepository

class ScriptOrdererViewSet(BaseCRUDViewSet):
    '''script orderer viewset'''
    read_serializer_class = ScriptOrdererReadSerializer
    write_serializer_class = ScriptOrdererWriteSerializer
    query_repo = ScriptsOrdererQueryRepository
    command_repo = ScriptsOrdererCommandRepository