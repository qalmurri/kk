from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scripts.models import Scripts
from scripts.serializers.scripts import ScriptsSerializer
from rest_framework.permissions import IsAuthenticated

class ScriptsView(APIView):
    throttle_classes = []
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        queryset = Scripts.objects.all().prefetch_related(
            "scripts_ScriptsOrderer__orderer__institute"
        )

        serializer = ScriptsSerializer(queryset, many=True)
        return Response(serializer.data)