from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {
                    "detail": "Refresh token is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # tambahkan token ke daftar hitam


            return Response(
                {
                    "message": "Logout successful."
                },
                status=status.HTTP_200_OK
            )

        except TokenError:
            return Response(
                {
                    "detail": "Invalid or expired refresh token."
                },
                status=status.HTTP_400_BAD_REQUEST
            )