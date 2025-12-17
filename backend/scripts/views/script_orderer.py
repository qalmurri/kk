from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scripts.serializers import ScriptOrdererCreateSerializer


class ScriptOrdererCreateView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        serializer = ScriptOrdererCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "ScriptOrderer created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
