from rest_framework import status

from apps.shared.custom_api_exception import CustomApiException
from apps.order.repository import OrderRepository


class OrderService:

    @staticmethod
    def list_all_instances_by_user_id(user_id):
        try:
            return OrderRepository.get_all_instances_by_user_id(user_id)
        except CustomApiException:
            raise
        except Exception as e:
            raise CustomApiException(
                detail=str(e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            ) from e

    @staticmethod
    def retrieve_instance_by_user_id(instance_id, user_id):
        try:
            return OrderRepository.get_instance_by_id_and_user_id(instance_id, user_id)
        except CustomApiException:
            raise
        except Exception as e:
            raise CustomApiException(
                detail=str(e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            ) from e
