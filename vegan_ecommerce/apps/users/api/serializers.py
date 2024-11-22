from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from drf_spectacular.utils import extend_schema_serializer
from drf_spectacular.openapi import OpenApiExample

User = get_user_model()


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Example update Value",
            value={
                'full_name': 'Anna Smith',
                'cpf': '328.315.830-47',
                'date_of_birth': '01/01/2001',
                'phone_number': '11988888888'
            },
            request_only=True
        ),
        OpenApiExample(
            name="Example Value",
            value={
                'id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
                'full_name': 'Anna Smith',
                'email': 'user@exemple.com',
                'cpf': '328.315.830-47',
                'date_of_birth': '01/01/2001',
                'phone_number': '11988888888'
            },
            response_only=True
        )
    ]
)
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'full_name', 'email', 'cpf',
                  'date_of_birth', 'phone_number')
        read_only = ('id', 'email')


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Example create Value",
            value={
                'full_name': 'Anna Smith',
                'email': 'user@exemple.com',
                'cpf': '328.315.830-47',
                'date_of_birth': '01/01/2001',
                'phone_number': '11988888888',
                'password': 'String'
            },
            request_only=True
        ),
        OpenApiExample(
            name="Example Value",
            value={
                'id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
                'full_name': 'Anna Smith',
                'email': 'user@exemple.com',
                'cpf': '328.315.830-47',
                'date_of_birth': '01/01/2001',
                'phone_number': '11988888888',
            },
            response_only=True
        ),
    ]
)
class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('full_name', 'email', 'cpf',
                  'date_of_birth', 'phone_number', 'password')


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Example Value",
            value={
                "access": "string",
                "refresh": "string",
                'full_name': 'Anna Smith',
                'email': 'user@exemple.com',
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
        token['email'] = user.email
        token['cpf'] = user.cpf
        token['date_of_birth'] = user.date_of_birth
        token['phone_number'] = user.phone_number
        return token
