from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scripts.models import Scripts
from scripts.serializers import ScriptSerializer

class ScriptsView(APIView):
    def get(self, request):
        scripts = Scripts.objects.all()
        serializer = ScriptSerializer(scripts, many=True)
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
