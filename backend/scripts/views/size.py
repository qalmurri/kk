from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scripts.repositories import SizeRepository
from scripts.serializers import SizeSerializer
from scripts.utils import current_timestamp

class SizeAllView(APIView):
    def get(self, request):
        queryset = SizeRepository.list_all()
        serializer = SizeSerializer(queryset, many=True)
        return Response(
            {
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
    
class SizeCreatedView(APIView):
    def post(self, request):
        size = request.data.get("size")

        if size is None:
            return Response(
                {
                    "success": False
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        SizeRepository.create(size=size)
        return Response(
            {
                "success": True,
            },
            status=status.HTTP_201_CREATED
        )
    
class SizeUpdateView(APIView):
    def patch(self, request, id):
        obj = SizeRepository.get_by_id(id)
        if not obj:
            return Response({
                "success": False,
            }, status=status.HTTP_404_NOT_FOUND)
        size = request.data.get("size")
        SizeRepository.update(
            id=id,
            size=size,
            updated_at=current_timestamp()
        )
        return Response({
            "success": True,
        }, status=status.HTTP_200_OK)