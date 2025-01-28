from rest_framework import status

from apps.ingredient.repository import IngredientRepository

from apps.shared.custom_api_exception import CustomApiException


class IngredientService:

    @staticmethod
    def list_all_instances():
        try:
            return IngredientRepository.get_all_instances()
        except Exception as e:
            raise CustomApiException(
                detail=str(e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            ) from e

    @staticmethod
    def retrieve_instance(instance_id):
        try:
            return IngredientRepository.get_instance_by_id(instance_id)
        except CustomApiException:
            raise
        except Exception as e:
            raise CustomApiException(
                detail=str(e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            ) from e
