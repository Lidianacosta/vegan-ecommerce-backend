from apps.subcategory.models import Subcategory
from apps.shared.custom_api_exception import CustomApiException
from rest_framework import status
from django.core.exceptions import ValidationError


class SubcategoryRepository:

    @staticmethod
    def get_all_instances():
        return Subcategory.objects.all()

    @staticmethod
    def get_instance_by_id(instance_id):
        try:
            return Subcategory.objects.get(id=instance_id)
        except Subcategory.DoesNotExist as e:
            raise CustomApiException(
                detail="subcategory not found",
                status_code=status.HTTP_404_NOT_FOUND
            ) from e
        except ValidationError as e:
            raise CustomApiException(
                detail=str(e),
                status_code=status.HTTP_404_NOT_FOUND
            ) from e
