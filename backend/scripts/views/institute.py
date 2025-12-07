from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scripts.repositories import InstituteRepository
from scripts.serializers import InstituteSerializer
from scripts.utils import current_timestamp

class InstituteAllView(APIView):
    def get(self, request):
        queryset = InstituteRepository.list_all()
        serializer = InstituteSerializer(queryset, many=True)
        return Response(
            {
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
    
class InstituteCreatedView(APIView):
    def post(self, request):
        institute = request.data.get("institute")
        if institute is None:
            return Response(
                {
                    "success": False
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        InstituteRepository.create(institute=institute)
        return Response(
            {
                "success": True,
            },
            status=status.HTTP_201_CREATED
        )
    
class InstituteUpdateView(APIView):
    def patch(self, request, id):
        obj = InstituteRepository.get_by_id(id)
        if not obj:
            return Response({
                "success": False,
            }, status=status.HTTP_404_NOT_FOUND)
        institute = request.data.get("institute")
        InstituteRepository.update(
            id=id,
            institute=institute,
            updated_at=current_timestamp()
        )
        return Response({
            "success": True,
        }, status=status.HTTP_200_OK)