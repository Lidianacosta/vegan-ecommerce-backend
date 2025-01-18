from django.http import Http404

from rest_framework import status

from apps.shared.custom_api_exception import CustomApiException
from apps.bytea_image.repository import ByteaImageRepository
from apps.bytea_image.models import ByteaImage


class ByteaImageService:

    @staticmethod
    def get_instance_by_id_or_404(instance_id):
        try:
            return ByteaImageRepository.get_instance_by_id(instance_id=instance_id)
        except CustomApiException as e:
            raise Http404(
                f"No {ByteaImage.__name__} matches the given query."
            ) from e

    @staticmethod
    def get_instance_of_bytea_image_from_image(image, obj=None, save=False):
        if obj is None:
            obj = ByteaImage()
        obj.image_name = image.name
        obj.content_type = image.content_type
        obj.image_data = image.read()
        if save:
            obj.save()
        return obj

    @staticmethod
    def get_image_url_by_id(instance_id):
        try:
            return ByteaImageRepository.get_instance_by_id(instance_id=instance_id)
        except CustomApiException:
            raise
        except Exception as e:
            raise CustomApiException(
                detail=str(e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            ) from e
