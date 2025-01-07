from django.template.defaultfilters import slugify

from rest_framework import status

from apps.shared.base_service import BaseService
from apps.shared.custom_api_exception import CustomApiException
from apps.category.repository import CategoryRepository


class CategoryService(BaseService):

    @staticmethod
    def list_all_instances():
        try:
            return CategoryRepository.get_all_instances()
        except Exception as e:
            raise CustomApiException(detail=str(
                e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def create_instance(**validated_data):
        try:
            validated_data['slug'] = slugify(validated_data['name'])
            return CategoryRepository.create_instance(data=validated_data)
        except Exception as e:
            raise CustomApiException(detail=str(
                e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def retrieve_instance(instance_id):
        try:
            return CategoryRepository.get_instance_by_id(instance_id=instance_id)
        except CustomApiException:
            raise
        except Exception as e:
            raise CustomApiException(detail=str(
                e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def update_instance(instance_id, **validated_data):
        try:
            validated_data['slug'] = slugify(validated_data['name'])
            return CategoryRepository.update_instance(instance_id=instance_id, data=validated_data)
        except CustomApiException:
            raise
        except Exception as e:
            raise CustomApiException(detail=str(
                e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def partial_update_instance(instance_id, **validated_data):
        try:
            if 'name' in validated_data:
                validated_data['slug'] = slugify(validated_data['name'])
            return CategoryRepository.update_instance(instance_id=instance_id, data=validated_data)
        except CustomApiException:
            raise
        except Exception as e:
            raise CustomApiException(detail=str(
                e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def destroy_instance(instance_id):
        try:
            CategoryRepository.delete_instance(instance_id=instance_id)
        except CustomApiException:
            raise
        except Exception as e:
            raise CustomApiException(detail=str(
                e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
