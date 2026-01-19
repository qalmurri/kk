from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class BaseViewSet(ViewSet):
    """
    Base ViewSet untuk semua resource
    """
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]
    authentication_classes = []
    permission_classes = []
    throttle_classes = []

    # ---------- Response Helpers ----------

    def success(
        self,
        data=None,
        status_code=status.HTTP_200_OK
    ):
        payload = {"success": True}

        if data is not None:
            payload["data"] = data

        return Response(payload, status=status_code)

    def error(
        self,
        message="Invalid request",
        status_code=status.HTTP_400_BAD_REQUEST,
        extra=None
    ):
        payload = {
            "success": False,
            "message": message
        }

        if extra:
            payload["errors"] = extra

        return Response(payload, status=status_code)

    # ---------- Validation Helpers ----------

    def require_fields(self, data: dict, fields: list):
        missing = [
            field for field in fields
            if not data.get(field)
        ]

        if missing:
            return self.error(
                message="Missing required fields",
                extra={"missing": missing},
                status_code=status.HTTP_400_BAD_REQUEST
            )

        return None

class BaseCRUDViewSet(BaseViewSet):
    read_serializer_class = None
    write_serializer_class = None
    query_repo = None
    command_repo = None

    def list(self, request):
        queryset = self.query_repo.query()
        serializer = self.read_serializer_class(
            queryset,
            many=True
        )
        return self.success(serializer.data)

    def create(self, request):
        serializer = self.write_serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        self.command_repo.create(
            **serializer.validated_data
        )
        return self.success(status_code=201)

    def retrieve(self, request, pk=None):
        obj = self.query_repo.get_by_id(pk)
        serializer = self.read_serializer_class(obj)
        return self.success(serializer.data)

    def partial_update(self, request, pk=None):
        obj = self.query_repo.get_by_id(pk)
        serializer = self.write_serializer_class(
            instance=obj,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.command_repo.update(
            obj,
            **serializer.validated_data
        )
        return self.success()

    @action(detail=True, methods=["delete"], url_path="hard")
    def hard_delete(self, request, pk=None):
        obj = self.query_repo.get_by_id(pk)
        self.command_repo.hard_delete(obj)
        return self.success()
