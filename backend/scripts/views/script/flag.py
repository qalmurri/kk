from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.read.script import (
    FlagReadSerializer,
    SectionFlagReadSerializer,
    )
from scripts.serializers.write.script import (
    FlagWriteSerializer,
    SectionFlagWriteSerializer,
    )
from scripts.repositories.command.script import (
    FlagCommandRepository,
    SectionFlagCommandRepository
    )
from scripts.repositories.query.script import (
    FlagQueryRepository,
    SectionFlagQueryRepository,
    )

class FlagViewSet(BaseCRUDViewSet):
    '''flag viewset'''
    read_serializer_class = FlagReadSerializer
    write_serializer_class = FlagWriteSerializer
    query_repo = FlagQueryRepository
    command_repo = FlagCommandRepository

class SectionFlagViewSet(BaseCRUDViewSet):
    '''part viewset'''
    read_serializer_class = SectionFlagReadSerializer
    write_serializer_class = SectionFlagWriteSerializer
    query_repo = SectionFlagQueryRepository
    command_repo = SectionFlagCommandRepository