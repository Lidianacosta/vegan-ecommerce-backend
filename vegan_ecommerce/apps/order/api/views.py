from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.order.service import OrderService
from apps.shared.custom_api_exception import CustomApiException
from apps.order.api.serializers import OrderSerializer


class OrderViewSet(viewsets.ViewSet):
    serializer_class = OrderSerializer

    def list(self, request, user_id=None):
        try:
            orders = OrderService.list_all_instances_by_user_id(user_id)
            serializer = OrderSerializer(
                instance=orders, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)

    def retrieve(self, request, pk=None, user_id=None):
        try:
            order = OrderService.retrieve_instance_by_user_id(
                instance_id=pk, user_id=user_id)
            serializer = OrderSerializer(instance=order)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except CustomApiException as e:
            return Response(data=e.detail, status=e.status_code)
