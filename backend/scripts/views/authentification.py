from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({
                "success": False,
                "message": "Username atau password salah"
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "success": True,
            "id": user.id,
            "username": user.username,
        })
