from scripts.views.base import BaseCRUDViewSet
#from scripts.serializers.pivot import (
#    ScriptsOrdererReadSerializer,
#    ScriptsOrdererWriteSerializer
#    )
from scripts.repositories.pivot.scriptsorderer import (
    ScriptsOrdererQueryRepository,
    ScriptsOrdererCommandRepository
    )

class ScriptsOrdererViewSet(BaseCRUDViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

#    read_serializer_class = ScriptsOrdererReadSerializer
#    write_serializer_class = ScriptsOrdererWriteSerializer
    query_repo = ScriptsOrdererQueryRepository
    command_repo = ScriptsOrdererCommandRepository