from rest_framework import serializers
from apps.category.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description',
                  'main_image', 'secondary_image')
        read_only_fields = ('slug',)
