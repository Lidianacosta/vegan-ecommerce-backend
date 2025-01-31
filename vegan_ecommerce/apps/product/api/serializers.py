from rest_framework import serializers

from apps.product.models import Product

from apps.bytea_image.service import ByteaImageService


class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'price',
                  'stock', 'image_url', 'description')

    def get_image_url(self, obj):
        return ByteaImageService.get_image_url(obj.image)
