from rest_framework import status

from apps.mark.repository import MarkRepository

from apps.shared.custom_api_exception import CustomApiException


class MarkService:

    @staticmethod
    def list_all_instances():
        try:
            return MarkRepository.get_all_instances()
        except Exception as e:
            raise CustomApiException(
                detail=str(e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            ) from e

    @staticmethod
    def retrieve_instance(instance_id):
        try:
            return MarkRepository.get_instance_by_id(instance_id)
        except CustomApiException:
            raise
        except Exception as e:
            raise CustomApiException(
                detail=str(e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            ) from e
