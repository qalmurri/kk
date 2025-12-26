from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.read import (
    FlagReadSerializer,
    PartReadSerializer,
    )
from scripts.serializers.write import (
    FlagWriteSerializer,
    PartWriteSerializer,
    )
from scripts.repositories.command import (
    FlagCommandRepository,
    PartCommandRepository
    )
from scripts.repositories.query import (
    FlagQueryRepository,
    PartQueryRepository,
    )

class FlagViewSet(BaseCRUDViewSet):
    '''flag viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = FlagReadSerializer
    write_serializer_class = FlagWriteSerializer
    query_repo = FlagQueryRepository
    command_repo = FlagCommandRepository

class PartViewSet(BaseCRUDViewSet):
    '''part viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = PartReadSerializer
    write_serializer_class = PartWriteSerializer
    query_repo = PartQueryRepository
    command_repo = PartCommandRepository