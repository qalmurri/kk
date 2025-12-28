from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.read import (
    FlagReadSerializer,
    SectionFlagReadSerializer,
    )
from scripts.serializers.write import (
    FlagWriteSerializer,
    SectionFlagWriteSerializer,
    )
from scripts.repositories.command import (
    FlagCommandRepository,
    SectionFlagCommandRepository
    )
from scripts.repositories.query import (
    FlagQueryRepository,
    SectionFlagQueryRepository,
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

class SectionFlagViewSet(BaseCRUDViewSet):
    '''part viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = SectionFlagReadSerializer
    write_serializer_class = SectionFlagWriteSerializer
    query_repo = SectionFlagQueryRepository
    command_repo = SectionFlagCommandRepository