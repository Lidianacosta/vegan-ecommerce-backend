from django.core.exceptions import ValidationError

from rest_framework import status

from apps.category.models import Category
from apps.shared.custom_api_exception import CustomApiException


class CategoryRepository:

    @staticmethod
    def get_all_instances():
        return Category.objects.all()

    @staticmethod
    def get_instance_by_id(instance_id):
        try:
            return Category.objects.get(id=instance_id)
        except Category.DoesNotExist as e:
            raise CustomApiException(
                detail='category not found',
                status_code=status.HTTP_404_NOT_FOUND
            ) from e
        except ValidationError as e:
            raise CustomApiException(
                detail=str(e), status_code=status.HTTP_400_BAD_REQUEST) from e
