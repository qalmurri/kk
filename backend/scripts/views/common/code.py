from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.common import (
    CodeReadSerializer,
    CodeWriteSerializer
    )
from scripts.repositories.common.code import (
    ScriptsStatusCodeQueryRepository,
    ScriptsStatusCodeCommandRepository
    )

class CodeViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = CodeReadSerializer
    write_serializer_class = CodeWriteSerializer
    query_repo = ScriptsStatusCodeQueryRepository
    command_repo = ScriptsStatusCodeCommandRepository