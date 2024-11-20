from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from drf_spectacular.utils import extend_schema_serializer
from drf_spectacular.openapi import OpenApiExample


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Example Value",
            value={
                "access": "string",
                "refresh": "string",
                'full_name': 'Anna Smith',
                'cpf': '328.315.830-47',
                'date_of_birth': '01/01/2001',
                'phone_number': '11988888888'
            },
            response_only=True
        )
    ]
)
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['full_name'] = user.full_name
        token['cpf'] = user.cpf
        token['date_of_birth'] = user.date_of_birth
        token['phone_number'] = user.phone_number
        return token
