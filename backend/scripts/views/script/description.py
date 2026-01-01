from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.read.script import (
    DescriptionReadSerializer,
    TextDescriptionReadSerializer,
    SectionDescriptionReadSerializer,
    )
from scripts.serializers.write.script import (
    DescriptionWriteSerializer,
    TextDescriptionWriteSerializer,
    SectionDescriptionWriteSerializer
    )
from scripts.repositories.command.script import (
    DescriptionCommandRepository,
    TextCommandRepository,
    DescriptionPartCommandRepository
    )
from scripts.repositories.query.script import (
    DescriptionQueryRepository,
    TextQueryRepository,
    DescriptionPartQueryRepository
    )

class DescriptionViewSet(BaseCRUDViewSet):
    ''''description viewset'''
    read_serializer_class = DescriptionReadSerializer
    write_serializer_class = DescriptionWriteSerializer
    query_repo = DescriptionQueryRepository
    command_repo = DescriptionCommandRepository

class TextDescriptionViewSet(BaseCRUDViewSet):
    '''text viewset'''
    read_serializer_class = TextDescriptionReadSerializer
    write_serializer_class = TextDescriptionWriteSerializer
    query_repo = TextQueryRepository
    command_repo = TextCommandRepository

class SectionDescriptionViewSet(BaseCRUDViewSet):
    '''description part viewset'''
    read_serializer_class = SectionDescriptionReadSerializer
    write_serializer_class = SectionDescriptionWriteSerializer
    query_repo = DescriptionPartQueryRepository
    command_repo = DescriptionPartCommandRepository