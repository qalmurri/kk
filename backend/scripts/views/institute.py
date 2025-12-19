from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scripts.repositories.institute import InstituteCommandRepository, InstituteQueryRepository
from scripts.serializers.common import InstituteSerializer
from scripts.utils import current_timestamp

class InstituteAllView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        queryset = InstituteQueryRepository.list_all()
        serializer = InstituteSerializer(queryset, many=True)
        return Response(
            {
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
    
class InstituteCreatedView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        institute = request.data.get("institute")
        if institute is None:
            return Response(
                {
                    "success": False
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        InstituteCommandRepository.create(institute=institute)
        return Response(
            {
                "success": True,
            },
            status=status.HTTP_201_CREATED
        )
    
class InstituteUpdateView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    
    def patch(self, request, id):
        obj = InstituteQueryRepository.get_by_id(id)
        if not obj:
            return Response({
                "success": False,
            }, status=status.HTTP_404_NOT_FOUND)
        institute = request.data.get("institute")
        InstituteCommandRepository.update_safe(
            id=id,
            institute=institute,
            updated_at=current_timestamp()
        )
        return Response({
            "success": True,
        }, status=status.HTTP_200_OK)