from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from apps.category.service import CategoryService
from apps.shared.custom_api_exception import CustomApiException
from apps.category.api.serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    serializer_class = CategorySerializer

    def list(self, request):
        try:
            categories = CategoryService.list_all_instances()
            serializer = CategorySerializer(instance=categories, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)

    def create(self, request):
        try:
            serializer = CategorySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            category = CategoryService.create_instance(
                **serializer.validated_data)
            serializer = CategorySerializer(instance=category)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)
        except ValidationError as e:
            return Response(data={'error': e.detail}, status=e.status_code)

    def retrieve(self, request, pk=None):
        try:
            category = CategoryService.retrieve_instance(instance_id=pk)
            serializer = CategorySerializer(instance=category)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)

    def update(self, request, pk=None):
        try:
            serializer = CategorySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            category = CategoryService.update_instance(
                instance_id=pk, **serializer.validated_data)
            serializer = CategorySerializer(instance=category)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)
        except ValidationError as e:
            return Response(data={'error': e.detail}, status=e.status_code)

    def partial_update(self, request, pk=None):
        try:
            serializer = CategorySerializer(data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            category = CategoryService.partial_update_instance(
                instance_id=pk, **serializer.validated_data)
            serializer = CategorySerializer(instance=category)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)
        except ValidationError as e:
            return Response(data={'error': e.detail}, status=e.status_code)

    def destroy(self, request, pk):
        try:
            CategoryService.destroy_instance(instance_id=pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)
