from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


from apps.ingredient.api.serializers import IngredientSerializer
from apps.ingredient.service import IngredientService
from apps.shared.custom_api_exception import CustomApiException


class IngredientViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            ingredients = IngredientService.list_all_instances()
            serializer = IngredientSerializer(instance=ingredients, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)

    def retrieve(self, request, pk):
        try:
            ingredient = IngredientService.retrieve_instance(instance_id=pk)
            serializer = IngredientSerializer(instance=ingredient)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)
