from django.core.exceptions import ValidationError

from rest_framework import status

from apps.bytea_image.models import ByteaImage
from apps.shared.custom_api_exception import CustomApiException


class ByteaImageRepository:

    @staticmethod
    def get_instance_by_id(instance_id):
        try:
            return ByteaImage.objects.get(id=instance_id)
        except ByteaImage.DoesNotExist as e:
            raise CustomApiException(
                detail='image not found',
                status_code=status.HTTP_404_NOT_FOUND
            ) from e
        except ValidationError as e:
            raise CustomApiException(
                detail=str(e),
                status_code=status.HTTP_400_BAD_REQUEST
            ) from e
