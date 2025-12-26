from scripts.views.base import BaseCRUDViewSet
from scripts.serializers import (
    ScriptProcessReadSerializer,
    ScriptProcessWriteSerializer,
    ByReadSerializer,
    ByWriteSerializer,
    SectionReadSerializer,
    SectionWriteSerializer
    )
from scripts.repositories import (
    ScriptsProcessQueryRepository,
    ScriptsProcessCommandRepository,
    ByQueryRepository,
    ByCommandRepository,
    SectionQueryRepository,
    SectionCommandRepository
    )

class SectionViewSet(BaseCRUDViewSet):
    '''section viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = SectionReadSerializer
    write_serializer_class = SectionWriteSerializer
    query_repo = SectionQueryRepository
    command_repo = SectionCommandRepository

class ByViewSet(BaseCRUDViewSet):
    '''by viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = ByReadSerializer
    write_serializer_class = ByWriteSerializer
    query_repo = ByQueryRepository
    command_repo = ByCommandRepository

class ScriptProcessViewSet(BaseCRUDViewSet):
    '''scrip process viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = ScriptProcessReadSerializer
    write_serializer_class = ScriptProcessWriteSerializer
    query_repo = ScriptsProcessQueryRepository
    command_repo = ScriptsProcessCommandRepository

