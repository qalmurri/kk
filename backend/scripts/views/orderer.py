from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scripts.repositories.orderer import OrdererCommandRepository, OrdererQueryRepository
from scripts.serializers import OrdererAllSerializer
from scripts.utils import current_timestamp

class OrdererAllView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    
    def get(self, request):
        queryset = OrdererQueryRepository.list_all()
        serializer = OrdererAllSerializer(queryset, many=True)
        return Response(
            {
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
    
class OrdererCreatedView(APIView):
    def post(self, request):
        orderer = request.data.get("orderer")
        no = request.data.get("no")
        if orderer is None:
            return Response(
                {
                    "success": False
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        OrdererCommandRepository.create(orderer=orderer, no=no)
        return Response(
            {
                "success": True,
            },
            status=status.HTTP_201_CREATED
        )
    
class OrdererUpdateView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    
    def patch(self, request, id):
        obj = OrdererQueryRepository.get_by_id(id)
        if not obj:
            return Response({
                "success": False,
            }, status=status.HTTP_404_NOT_FOUND)
        name = request.data.get("name")
        no = request.data.get("no")
        institute = request.data.get("institute")
        OrdererCommandRepository.update_safe(
            id=id,
            name=name,
            no=no,
            institute=institute,
            updated_at=current_timestamp()
        )
        return Response({
            "success": True,
        }, status=status.HTTP_200_OK)