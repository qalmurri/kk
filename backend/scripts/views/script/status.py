from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.read.script import (
    StatusReadSerializer,
    LabelStatusReadSerializer,
    SectionStatusReadSerializer
    )
from scripts.serializers.write.script import (
    StatusWriteSerializer,
    LabelStatusWriteSerializer,
    SectionStatusWriteSerializer
    )
from scripts.repositories.command.script import (
    StatusCommandRepository,
    LabelStatusCommandRepository,
    SectionStatusCommandRepository
    )
from scripts.repositories.query.script import (
    StatusQueryRepository,
    LabelStatusQueryRepository,
    SectionStatusQueryRepository
    )

class SectionStatusViewSet(BaseCRUDViewSet):
    '''cover viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = SectionStatusReadSerializer
    write_serializer_class = SectionStatusWriteSerializer
    query_repo = SectionStatusQueryRepository
    command_repo = SectionStatusCommandRepository

class LabelStatusViewSet(BaseCRUDViewSet):
    '''label viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = LabelStatusReadSerializer
    write_serializer_class = LabelStatusWriteSerializer
    query_repo = LabelStatusQueryRepository
    command_repo = LabelStatusCommandRepository

class StatusViewSet(BaseCRUDViewSet):
    '''status viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = StatusReadSerializer
    write_serializer_class = StatusWriteSerializer
    query_repo = StatusQueryRepository
    command_repo = StatusCommandRepository