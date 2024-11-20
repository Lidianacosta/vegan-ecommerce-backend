from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import (
    RefreshToken,
    TokenError
)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = RefreshToken(request.data.get("refresh_token"))
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
