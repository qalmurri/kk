from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.common import (
    SizeReadSerializer,
    SizeWriteSerializer,
    InstituteReadSerializer,
    InstituteWriteSerializer
    )
from scripts.repositories.common import (
    SizeQueryRepository,
    SizeCommandRepository,
    InstituteQueryRepository,
    InstituteCommandRepository
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