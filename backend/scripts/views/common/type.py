from rest_framework.decorators import action
from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.common import (
    TypeReadSerializer,
    TypeWriteSerializer
    )
from scripts.repositories.common.type import (
    TypeQueryRepository,
    TypeCommandRepository
    )

class TypeViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = TypeReadSerializer
    write_serializer_class = TypeWriteSerializer
    query_repo = TypeQueryRepository
    command_repo = TypeCommandRepository