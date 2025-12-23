from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.common import (
    InstituteReadSerializer,
    InstituteWriteSerializer
    )
from scripts.repositories.common.institute import (
    InstituteQueryRepository,
    InstituteCommandRepository
    )

class InstituteViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = InstituteReadSerializer
    write_serializer_class = InstituteWriteSerializer
    query_repo = InstituteQueryRepository
    command_repo = InstituteCommandRepository