from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.read.script import (
    IsbnReadSerializer,
    TypeIsbnReadSerializer
)
from scripts.serializers.write.script import (
    IsbnWriteSerializer,
    TypeIsbnWriteSerializer
)
from scripts.repositories.command.script import (
    IsbnCommandRepository,
    TypeIsbnCommandRepository
)
from scripts.repositories.query.script import (
    IsbnQueryRepository,
    TypeIsbnQueryRepository
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
    read_serializer_class = TypeIsbnReadSerializer
    write_serializer_class = TypeIsbnWriteSerializer
    query_repo = TypeIsbnQueryRepository
    command_repo = TypeIsbnCommandRepository