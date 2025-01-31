from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.product.service import ProductService
from apps.shared.custom_api_exception import CustomApiException
from apps.product.api.serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    serializer_class = ProductSerializer

    def list(self, request):
        try:
            products = ProductService.list_all_instances()
            serializer = ProductSerializer(
                instance=products, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)

    def retrieve(self, request, pk=None):
        try:
            product = ProductService.retrieve_instance(instance_id=pk)
            serializer = ProductSerializer(instance=product)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)
