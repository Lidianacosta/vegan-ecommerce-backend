from apps.product.models import Product
from apps.shared.custom_api_exception import CustomApiException
from rest_framework import status
from django.core.exceptions import ValidationError


class ProductRepository:

    @staticmethod
    def get_all_instances():
        return Product.objects.all()

    @staticmethod
    def get_instance_by_id(instance_id):
        try:
            return Product.objects.get(id=instance_id)
        except Product.DoesNotExist as e:
            raise CustomApiException(
                detail="Product not found",
                status_code=status.HTTP_404_NOT_FOUND
            ) from e
        except ValidationError as e:
            raise CustomApiException(
                detail=str(e),
                status_code=status.HTTP_404_NOT_FOUND
            ) from e
