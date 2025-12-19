from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scripts.repositories.purpose import StatusCommandRepository, StatusQueryRepository
from scripts.serializers.pivot import StatusSerializer, StatusAllSerializer
from scripts.utils import current_timestamp

class StatusByCodeView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    def get(self, request, code):
        obj = StatusQueryRepository.get_by_code(
            code
        )
        if not obj:
            return Response(
                {
                    "success": False,
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = StatusSerializer(
            obj,
            many=True
        )
        return Response(
            {
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

class StatusAllView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        queryset = StatusQueryRepository.list_all()
        serializer = StatusAllSerializer(
            queryset,
            many=True
        )

        return Response(
            {
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

class StatusCreateView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        code = request.data.get(
            "code"
        )
        purpose = request.data.get(
            "purpose"
        )
        if code is None or purpose is None:
            return Response(
                {
                    "success": False,
                }, status=status.HTTP_400_BAD_REQUEST)
        
        StatusCommandRepository.create(
            code=code,
            purpose=purpose
        )
        return Response({
            "success": True,
        }, status=status.HTTP_201_CREATED)
    
class StatusUpdateView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    
    def patch(self, request, id):
        obj = StatusQueryRepository.get_by_id(
            id
        )
        if not obj:
            return Response({
                "success": False,
            },
            status=status.HTTP_404_NOT_FOUND
        )
        purpose = request.data.get(
            "purpose"
        )
        StatusCommandRepository.update_safe(
            id=id,
            purpose=purpose,
            updated_at=current_timestamp()
        )
        return Response(
            {
                "success": True,
            },
            status=status.HTTP_200_OK
            )