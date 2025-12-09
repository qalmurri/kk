from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scripts.models import Scripts
from scripts.serializers import ScriptSerializer, ScriptsSerializer
from rest_framework.permissions import IsAuthenticated

class ScriptsView(APIView):
    permission_classes = []

    def get(self, request):
        queryset = Scripts.objects.all().prefetch_related(
            "scripts_ScriptOrderer__orderer__institute"
        )

        serializer = ScriptsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ScriptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "data": serializer.data
                }
            )
        return Response(
            {
                "success": False,
                "message": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
