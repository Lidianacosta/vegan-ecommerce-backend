from django.core.exceptions import ValidationError

from rest_framework import status

from apps.shared.custom_api_exception import CustomApiException

from apps.ingredient.models import Ingredient


class IngredientRepository:

    @staticmethod
    def get_all_instances():
        return Ingredient.objects.all()

    @staticmethod
    def get_instance_by_id(instance_id):
        try:
            return Ingredient.objects.get(id=instance_id)
        except Ingredient.DoesNotExist as e:
            raise CustomApiException(
                detail='Ingredient not found',
                status_code=status.HTTP_404_NOT_FOUND
            ) from e
        except ValidationError as e:
            raise CustomApiException(
                detail=str(e),
                status_code=status.HTTP_400_BAD_REQUEST
            ) from e
