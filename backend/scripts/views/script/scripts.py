from rest_framework.decorators import action
from scripts.views.base import BaseViewSet
from scripts.serializers.read.script import ScriptsReadSerializer
from scripts.serializers.write.script import ScriptsWriteSerializer
from scripts.repositories.command.script import ScriptsCommandRepository
from scripts.repositories.query.script import ScriptsQueryRepository
from scripts.include import parse_include_param

class ScriptViewSet(BaseViewSet):
    # GET /scripts/ = /scripts/?title=...&active=...
    # =====
    # GET /script/?view=data
    # GET /script/?view=part
    # GET /script/?view=card
    # GET /script/?fields=title,alias,institute
    # GET /script/?view=part&include=cover,status
    def get_serializer_class(self):
        view_mode = self.request.query_params.get("view", "data")

        if view_mode == "part":
            from scripts.serializers.read.script.scripts import (
                ScriptsPartReadSerializer
            )
            return ScriptsPartReadSerializer
        
        if view_mode == "card":
            from scripts.serializers.read.script.scripts import (
                ScriptsCardReadSerializer
            )
            return ScriptsCardReadSerializer
        
        return ScriptsReadSerializer

    # ini jangan di rubah! Diperlukan untuk pengambilkan data dengan field custom. 
    def list (self, request):
        queryset = ScriptsQueryRepository.query(
            request.query_params
        )

        serializer_class = self.get_serializer_class()

        fields = request.query_params.get("fields") #
        field_list = fields.split(",") if fields else None #
        includes = parse_include_param(
            request.query_params.get("include")
        )
        serializer = serializer_class(
            queryset,
            many=True,
            fields=field_list,
            context={"includes": includes}
        )

        return self.success(serializer.data)

    # ===========================
    # POST /scripts/
    def create(self, request):
        serializer = ScriptsWriteSerializer(
            data=request.data
        )
        serializer.is_valid(
            raise_exception=True
        )
        ScriptsCommandRepository.create(
            **serializer.validated_data
        )
        return self.success(
            status_code=201
        )

    # GET /scripts/{id}/
    # GET /api/scripts/1?include=*
    # lazy expand 
# GET /api/scripts/1/status
# GET /api/scripts/1/notes
    def retrieve(self, request, pk=None):
        obj = ScriptsQueryRepository.get_by_id(
            pk
        )
        serializer = ScriptsReadSerializer(
            obj
        )
        return self.success(
            serializer.data
        )

    # PUT /scripts/{id}/
    def update(self, request, pk=None):
        pass

    # PATCH /scripts/{id}/
    def partial_update(self, request, pk=None):
        obj = ScriptsQueryRepository.get_by_id(
            pk
        )
        serializer = ScriptsWriteSerializer(
            instance=obj,
            data=request.data,
            partial=True
        )
        serializer.is_valid(
            raise_exception=True
        )
        ScriptsCommandRepository.update(
            obj,
            **serializer.validated_data
        )
        return self.success()

    # DELETE /scripts/{id}/
    def destroy(self, request, pk=None):
        obj = ScriptsQueryRepository.get_by_id(
            pk
        )
        ScriptsCommandRepository.archive(
            obj
        )
        return self.success()

    # POST /scripts/{id}/restore/
    @action(detail=True, methods=["post"])
    def restore(self, request, pk=None):
        obj = ScriptsQueryRepository.get_by_id(
            pk
        )
        ScriptsCommandRepository.restore(
            obj
        )
        return self.success()
    
    # DELETE /scripts/{id}/hard/
    @action(detail=True, methods=["delete"], url_path="hard")
    def hard_delete(self, request, pk=None):
        obj = ScriptsQueryRepository.get_by_id(
            pk
        )
        ScriptsCommandRepository.hard_delete(
            obj
        )
        return self.success()
