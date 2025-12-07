from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

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

        # --- PERUBAHAN PENTING DI SINI ---
        # 1. Dapatkan atau buat token untuk user
        token, created = Token.objects.get_or_create(user=user)

        # 2. Kembalikan token ke client
        return Response({
            "success": True,
            "token": token.key, # <-- Kunci token yang dibutuhkan PySide6
            "id": user.id,
            "username": user.username,
        }, status=status.HTTP_200_OK) # Gunakan 200 OK untuk sukses