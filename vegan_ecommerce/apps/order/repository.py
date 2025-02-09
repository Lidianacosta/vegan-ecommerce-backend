from apps.order.models import Order
from apps.shared.custom_api_exception import CustomApiException
from rest_framework import status
from django.core.exceptions import ValidationError


class OrderRepository:

    @staticmethod
    def get_all_instances_by_user_id(user_id):
        try:
            return Order.objects.filter(user__id=user_id)
        except ValidationError as e:
            raise CustomApiException(
                detail="Order not found",
                status_code=status.HTTP_404_NOT_FOUND
            ) from e

    @staticmethod
    def get_instance_by_id_and_user_id(instance_id, user_id):
        try:
            return Order.objects.get(id=instance_id, user__id=user_id)
        except ValidationError as e:
            raise CustomApiException(
                detail="Order not found",
                status_code=status.HTTP_404_NOT_FOUND
            ) from e
