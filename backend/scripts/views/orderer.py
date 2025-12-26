from scripts.views.base import BaseCRUDViewSet
from scripts.serializers import (
    OrdererReadSerializer,
    OrdererWriteSerializer,
    ScriptOrdererReadSerializer,
    ScriptOrdererWriteSerializer
    )
from scripts.repositories import (
    OrdererQueryRepository,
    OrdererCommandRepository,
    ScriptsOrdererQueryRepository,
    ScriptsOrdererCommandRepository
    )

class OrdererViewSet(BaseCRUDViewSet):
    '''orderer viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = OrdererReadSerializer
    write_serializer_class = OrdererWriteSerializer
    query_repo = OrdererQueryRepository
    command_repo = OrdererCommandRepository

class ScriptOrdererViewSet(BaseCRUDViewSet):
    '''script orderer viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = ScriptOrdererReadSerializer
    write_serializer_class = ScriptOrdererWriteSerializer
    query_repo = ScriptsOrdererQueryRepository
    command_repo = ScriptsOrdererCommandRepository