from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.write.script import (
    SizeWriteSerializer,
    InstituteWriteSerializer
    )
from scripts.repositories.command.script import (
    SizeCommandRepository,
    InstituteCommandRepository
    )
from scripts.serializers.read.script import (
    SizeReadSerializer,
    InstituteReadSerializer,
    )
from scripts.repositories.query.script import (
    SizeQueryRepository,
    InstituteQueryRepository
    )

class SizeViewSet(BaseCRUDViewSet):
    '''size viewset'''
    read_serializer_class = SizeReadSerializer
    write_serializer_class = SizeWriteSerializer
    query_repo = SizeQueryRepository
    command_repo = SizeCommandRepository

class InstituteViewSet(BaseCRUDViewSet):
    '''institute viewset'''
    read_serializer_class = InstituteReadSerializer
    write_serializer_class = InstituteWriteSerializer
    query_repo = InstituteQueryRepository
    command_repo = InstituteCommandRepository