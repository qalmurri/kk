from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scripts.repositories.size import SizeCommandRepository, SizeQueryRepository
from scripts.serializers.size import SizeSerializer
from scripts.utils import current_timestamp

class SizeAllView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        queryset = SizeQueryRepository.list_all()
        serializer = SizeSerializer(
            queryset,
            many=True
        )
        return Response(
            {
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
    
class SizeCreatedView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        size = request.data.get(
            "size"
        )

        if size is None:
            return Response(
                {
                    "success": False
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        SizeCommandRepository.create(size=size)
        return Response(
            {
                "success": True,
            },
            status=status.HTTP_201_CREATED
        )
    
class SizeUpdateView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    
    def patch(self, request, id):
        obj = SizeQueryRepository.get_by_id(
            id
        )
        print(obj)
        if not obj:
            return Response(
                {
                    "success": False,
                },
                status=status.HTTP_404_NOT_FOUND
            )
        size = request.data.get(
            "size"
        )
        SizeCommandRepository.update_fast(
            id=id,
            size=size,
            updated_at=current_timestamp()
        )
        return Response(
            {
                "success": True,
            },
            status=status.HTTP_200_OK
        )