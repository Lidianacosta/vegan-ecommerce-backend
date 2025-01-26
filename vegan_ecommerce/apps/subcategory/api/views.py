from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.subcategory.service import SubcategoryService
from apps.shared.custom_api_exception import CustomApiException
from apps.subcategory.api.serializers import SubcategorySerializer


class SubcategoryViewSet(viewsets.ViewSet):
    serializer_class = SubcategorySerializer

    def list(self, request):
        try:
            subcategories = SubcategoryService.list_all_instances()
            serializer = SubcategorySerializer(
                instance=subcategories, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)

    def retrieve(self, request, pk=None):
        try:
            subcategory = SubcategoryService.retrieve_instance(instance_id=pk)
            serializer = SubcategorySerializer(instance=subcategory)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)
