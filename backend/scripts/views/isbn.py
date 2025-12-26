from scripts.views.base import BaseCRUDViewSet
from scripts.serializers import (
    IsbnReadSerializer,
    IsbnWriteSerializer,
    TypeReadSerializer,
    TypeWriteSerializer
    )
from scripts.repositories import (
    ISBNQueryRepository,
    ISBNCommandRepository,
    TypeQueryRepository,
    TypeCommandRepository
    )

class IsbnViewSet(BaseCRUDViewSet):
    '''isbn viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = IsbnReadSerializer
    write_serializer_class = IsbnWriteSerializer
    query_repo = ISBNQueryRepository
    command_repo = ISBNCommandRepository

class TypeViewSet(BaseCRUDViewSet):
    '''type viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = TypeReadSerializer
    write_serializer_class = TypeWriteSerializer
    query_repo = TypeQueryRepository
    command_repo = TypeCommandRepository