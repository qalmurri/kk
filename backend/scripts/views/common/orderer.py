from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.common import (
    OrdererReadSerializer,
    OrdererWriteSerializer
    )
from scripts.repositories.common.orderer import (
    OrdererQueryRepository,
    OrdererCommandRepository
    )

class OrdererViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = OrdererReadSerializer
    write_serializer_class = OrdererWriteSerializer
    query_repo = OrdererQueryRepository
    command_repo = OrdererCommandRepository