from rest_framework.decorators import action
from .base import BaseViewSet
from scripts.serializers.scripts import ScriptsSerializer
from scripts.repositories.scripts import (
    ScriptsQueryRepository,
    ScriptsCommandRepository
    )

class ScriptsViewSet(BaseViewSet):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    # GET /scripts/
    def list(self, request):
        queryset = ScriptsQueryRepository.list_all()
        serializer = ScriptsSerializer(queryset, many=True)
        return self.success(serializer.data)
    
    # GET /scripts/{id}/
    def retrieve(self, request, pk=None):
        obj = ScriptsQueryRepository.get_by_id(pk)
        serializer = ScriptsSerializer(obj)
        return self.success(serializer.data)

    # POST /scripts/
    def create(self, request):
        data = request.data
        if not data.get("title"):
            return self.error("title is required")
        script = ScriptsCommandRepository.create(
            title=data["title"],
            alias=data.get("alias"),
            institute_id=data.get("institute"),
            size_id=data.get("size"),
        )
        return self.success(
            {"id": script.id},
            status_code=201
        )

    # PATCH /scripts/{id}/
    def partial_update(self, request, pk=None):
        ScriptsQueryRepository.get_by_id(pk)
        ScriptsCommandRepository.update_fast(
            id=pk,
            **request.data
        )
        return self.success()

    # POST /scripts/{id}/archive/
    @action(detail=True, methods=["post"])
    def archive(self, request, pk=None):
        ScriptsQueryRepository.get_by_id(pk)
        ScriptsCommandRepository.archive(pk)
        return self.success({"archived": True})
    
    # POST /scripts/{id}/restore/
    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        ScriptsQueryRepository.get_by_id(pk)
        ScriptsCommandRepository.restore(pk)
        return self.success({"restored": True})
    
    # GET /scripts/search/?title=...&active=...
    @action(detail=False, methods=["get"])
    def search(self, request):
        queryset = ScriptsQueryRepository.query(request.query_params)
        serializer = ScriptsSerializer(queryset , many=True)
        return self.success(serializer.data)