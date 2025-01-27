from django.core.exceptions import ValidationError

from rest_framework import status

from apps.shared.custom_api_exception import CustomApiException

from apps.mark.models import Mark


class MarkRepository:

    @staticmethod
    def get_all_instances():
        return Mark.objects.all()

    @staticmethod
    def get_instance_by_id(instance_id):
        try:
            return Mark.objects.get(id=instance_id)
        except Mark.DoesNotExist as e:
            raise CustomApiException(
                detail='Mark not found',
                status_code=status.HTTP_404_NOT_FOUND
            ) from e
        except ValidationError as e:
            raise CustomApiException(
                detail=str(e),
                status_code=status.HTTP_400_BAD_REQUEST
            ) from e
