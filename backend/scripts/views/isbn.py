from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.content import (
    ISBNReadSerializer,
    ISBNWriteSerializer
    )
from scripts.repositories.content.isbn import (
    ISBNQueryRepository,
    ISBNCommandRepository
    )

class ISBNViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = ISBNReadSerializer
    write_serializer_class = ISBNWriteSerializer
    query_repo = ISBNQueryRepository
    command_repo = ISBNCommandRepository