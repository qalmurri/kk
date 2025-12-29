from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.read import (
    MadeReadSerializer,
    ByMadeReadSerializer,
    SectionMadeReadSerializer
    )
from scripts.serializers.write import (
    MadeWriteSerializer,
    ByMadeWriteSerializer,
    SectionMadeWriteSerializer
    )
from scripts.repositories.command import (
    MadeCommandRepository,
    ByMadeCommandRepository,
    SectionMadeCommandRepository
    )
from scripts.repositories.query import (
    MadeQueryRepository,
    ByMadeQueryRepository,
    SectionMadeQueryRepository
    )

class SectionMadeViewSet(BaseCRUDViewSet):
    '''section viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = SectionMadeReadSerializer
    write_serializer_class = SectionMadeWriteSerializer
    query_repo = SectionMadeQueryRepository
    command_repo = SectionMadeCommandRepository

class ByMadeViewSet(BaseCRUDViewSet):
    '''by viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = ByMadeReadSerializer
    write_serializer_class = ByMadeWriteSerializer
    query_repo = ByMadeQueryRepository
    command_repo = ByMadeCommandRepository

class MadeViewSet(BaseCRUDViewSet):
    '''scrip process viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = MadeReadSerializer
    write_serializer_class = MadeWriteSerializer
    query_repo = MadeQueryRepository
    command_repo = MadeCommandRepository

