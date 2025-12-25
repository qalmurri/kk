from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.content import (
    TextReadSerializer,
    TextWriteSerializer
    )
from scripts.repositories.content.text import (
    TextQueryRepository,
    TextCommandRepository
    )

class TextViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    read_serializer_class = TextReadSerializer
    write_serializer_class = TextWriteSerializer
    query_repo = TextQueryRepository
    command_repo = TextCommandRepository