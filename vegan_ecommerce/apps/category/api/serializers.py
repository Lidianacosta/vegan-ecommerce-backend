from rest_framework import serializers
from apps.category.models import Category

from apps.bytea_image.service import ByteaImageService


class CategorySerializer(serializers.ModelSerializer):

    main_image_url = serializers.SerializerMethodField()
    secondary_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description',
                  'main_image_url', 'secondary_image_url')
        read_only_fields = ('slug',)

    def get_main_image_url(self, obj):
        return ByteaImageService.get_image_url(obj.main_image)

    def get_secondary_image_url(self, obj):
        return ByteaImageService.get_image_url(obj.secondary_image)
