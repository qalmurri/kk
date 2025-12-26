from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.write import (
    SizeWriteSerializer,
    InstituteWriteSerializer
    )
from scripts.repositories.command import (
    SizeCommandRepository,
    InstituteCommandRepository
    )
from scripts.serializers.read import (
    SizeReadSerializer,
    InstituteReadSerializer,
    )
from scripts.repositories.query import (
    SizeQueryRepository,
    InstituteQueryRepository
    )

class SizeViewSet(BaseCRUDViewSet):
    '''size viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = SizeReadSerializer
    write_serializer_class = SizeWriteSerializer
    query_repo = SizeQueryRepository
    command_repo = SizeCommandRepository

class InstituteViewSet(BaseCRUDViewSet):
    '''institute viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = InstituteReadSerializer
    write_serializer_class = InstituteWriteSerializer
    query_repo = InstituteQueryRepository
    command_repo = InstituteCommandRepository