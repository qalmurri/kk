from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scripts.repositories import CoverColorRepository
from scripts.serializers import CoverColorSerializer
from scripts.utils import current_timestamp

class CoverColorAllView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        queryset = CoverColorRepository.list_all()
        serializer = CoverColorSerializer(queryset, many=True)
        return Response(
            {
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
    
class CoverColorCreatedView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        color = request.data.get("color")
        if color is None:
            return Response(
                {
                    "success": False
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        CoverColorRepository.create(color=color)
        return Response(
            {
                "success": True,
            },
            status=status.HTTP_201_CREATED
        )
    
class CoverColorUpdateView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    
    def patch(self, request, id):
        obj = CoverColorRepository.get_by_id(id)
        if not obj:
            return Response({
                "success": False,
            }, status=status.HTTP_404_NOT_FOUND)
        color = request.data.get("color")
        CoverColorRepository.update(
            id=id,
            color=color,
            updated_at=current_timestamp()
        )
        return Response({
            "success": True,
        }, status=status.HTTP_200_OK)