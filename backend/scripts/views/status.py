from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.read import (
    StatusReadSerializer,
    LabelStatusReadSerializer,
    SectionReadSerializer
    )
from scripts.serializers.write import (
    StatusWriteSerializer,
    LabelStatusWriteSerializer,
    SectionWriteSerializer
    )
from scripts.repositories.command import (
    StatusCommandRepository,
    LabelCommandRepository,
    ScriptsStatusCodeCommandRepository
    )
from scripts.repositories.query import (
    StatusQueryRepository,
    LabelQueryRepository,
    ScriptsStatusCodeQueryRepository
    )

class CodeViewSet(BaseCRUDViewSet):
    '''cover viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = SectionReadSerializer
    write_serializer_class = SectionWriteSerializer
    query_repo = ScriptsStatusCodeQueryRepository
    command_repo = ScriptsStatusCodeCommandRepository

class LabelViewSet(BaseCRUDViewSet):
    '''label viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = LabelStatusReadSerializer
    write_serializer_class = LabelStatusWriteSerializer
    query_repo = LabelQueryRepository
    command_repo = LabelCommandRepository

class StatusViewSet(BaseCRUDViewSet):
    '''status viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = StatusReadSerializer
    write_serializer_class = StatusWriteSerializer
    query_repo = StatusQueryRepository
    command_repo = StatusCommandRepository