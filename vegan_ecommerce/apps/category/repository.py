from django.core.exceptions import ValidationError

from rest_framework import status

from apps.category.models import Category
from apps.shared.base_repository import BaseRepository
from apps.shared.custom_api_exception import CustomApiException


class CategoryRepository(BaseRepository):

    @staticmethod
    def get_all_instances():
        return Category.objects.all()

    @staticmethod
    def create_instance(data):
        return Category.objects.create(**data)

    @staticmethod
    def get_instance_by_id(instance_id):
        try:
            return Category.objects.get(id=instance_id)
        except Category.DoesNotExist:
            raise CustomApiException(
                detail='category not found',
                status_code=status.HTTP_404_NOT_FOUND
            )
        except ValidationError as e:
            raise CustomApiException(
                detail=str(e), status_code=status.HTTP_400_BAD_REQUEST) from e

    @staticmethod
    def update_instance(instance_id, data):
        try:
            instance = Category.objects.get(id=instance_id)
            for field, value in data.items():
                setattr(instance, field, value)
            instance.save()
            return instance
        except Category.DoesNotExist:
            raise CustomApiException(
                detail='category not found',
                status_code=status.HTTP_404_NOT_FOUND
            )
        except ValidationError as e:
            raise CustomApiException(
                detail=str(e), status_code=status.HTTP_400_BAD_REQUEST) from e

    @staticmethod
    def delete_instance(instance_id):
        try:
            instance = Category.objects.get(id=instance_id)
            instance.delete()
        except Category.DoesNotExist:
            raise CustomApiException(
                detail='category not found',
                status_code=status.HTTP_404_NOT_FOUND
            )
        except ValidationError as e:
            raise CustomApiException(
                detail=str(e), status_code=status.HTTP_400_BAD_REQUEST) from e
