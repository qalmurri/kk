from scripts.views.base import BaseCRUDViewSet
from scripts.serializers import (
    FlagReadSerializer,
    FlagWriteSerializer,
    PartReadSerializer,
    PartWriteSerializer
    )
from scripts.repositories import (
    FlagQueryRepository,
    FlagCommandRepository,
    PartQueryRepository,
    PartCommandRepository
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