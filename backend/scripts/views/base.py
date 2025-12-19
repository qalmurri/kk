from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status


class BaseViewSet(ViewSet):
    """
    Base ViewSet untuk semua resource
    """

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
