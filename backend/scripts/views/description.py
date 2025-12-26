from scripts.views.base import BaseCRUDViewSet
from scripts.serializers import (
    DescriptionReadSerializer,
    DescriptionWriteSerializer,
    TextDescriptionReadSerializer,
    TextDescriptionWriteSerializer,
    SectionDescriptionReadSerializer,
    SectionDescriptionWriteSerializer
    )
from scripts.repositories import (
    DescriptionQueryRepository,
    DescriptionCommandRepository,
    TextQueryRepository,
    TextCommandRepository,
    DescriptionPartQueryRepository,
    DescriptionPartCommandRepository
    )

class DescriptionViewSet(BaseCRUDViewSet):
    ''''description viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = DescriptionReadSerializer
    write_serializer_class = DescriptionWriteSerializer
    query_repo = DescriptionQueryRepository
    command_repo = DescriptionCommandRepository

class TextViewSet(BaseCRUDViewSet):
    '''text viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = TextDescriptionReadSerializer
    write_serializer_class = TextDescriptionWriteSerializer
    query_repo = TextQueryRepository
    command_repo = TextCommandRepository

class DescriptionPartViewSet(BaseCRUDViewSet):
    '''description part viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = SectionDescriptionReadSerializer
    write_serializer_class = SectionDescriptionWriteSerializer
    query_repo = DescriptionPartQueryRepository
    command_repo = DescriptionPartCommandRepository