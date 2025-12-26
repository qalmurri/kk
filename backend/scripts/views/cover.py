from scripts.views.base import BaseCRUDViewSet
from scripts.serializers import (
    CoverReadSerializer,
    CoverWriteSerializer
    )
from scripts.repositories.command import CoverBookCommandRepository
from scripts.repositories.query import CoverBookQueryRepository

class CoverViewset(BaseCRUDViewSet):
    '''cover viewset'''
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    read_serializer_class = CoverReadSerializer
    write_serializer_class = CoverWriteSerializer
    query_repo = CoverBookQueryRepository
    command_repo = CoverBookCommandRepository