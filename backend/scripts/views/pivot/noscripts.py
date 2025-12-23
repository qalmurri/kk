from scripts.views.base import BaseCRUDViewSet
#from scripts.serializers.pivot import (
#    NoScriptsReadSerializer,
#    NoScriptsWriteSerializer
#    )
from scripts.repositories.pivot.noscripts import (
    NoScriptsQueryRepository,
    NoScriptsCommandRepository
    )

class NoScriptsViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

#    read_serializer_class = NoScriptsReadSerializer
#    write_serializer_class = NoScriptsWriteSerializer
    query_repo = NoScriptsQueryRepository
    command_repo = NoScriptsCommandRepository