from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.read import (
    IsbnReadSerializer,
    TypeReadSerializer
)
from scripts.serializers.write import (
    IsbnWriteSerializer,
    TypeWriteSerializer
)
from scripts.repositories.command import (
    IsbnCommandRepository,
    TypeCommandRepository
)
from scripts.repositories.query import (
    IsbnQueryRepository,
    TypeQueryRepository
)

class IsbnViewSet(BaseCRUDViewSet):
    '''isbn viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = IsbnReadSerializer
    write_serializer_class = IsbnWriteSerializer
    query_repo = IsbnQueryRepository
    command_repo = IsbnCommandRepository

class TypeIsbnViewSet(BaseCRUDViewSet):
    '''type viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = TypeReadSerializer
    write_serializer_class = TypeWriteSerializer
    query_repo = TypeQueryRepository
    command_repo = TypeCommandRepository