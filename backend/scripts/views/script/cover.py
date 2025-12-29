from scripts.views.base import BaseCRUDViewSet
from scripts.serializers.read.script import CoverReadSerializer
from scripts.serializers.write.script import CoverWriteSerializer
from scripts.repositories.command.script import CoverBookCommandRepository
from scripts.repositories.query.script import CoverBookQueryRepository

class CoverViewset(BaseCRUDViewSet):
    '''cover viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = CoverReadSerializer
    write_serializer_class = CoverWriteSerializer
    query_repo = CoverBookQueryRepository
    command_repo = CoverBookCommandRepository