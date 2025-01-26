from rest_framework import serializers

from apps.subcategory.models import Subcategory


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'slug', 'description',
                  'category', 'is_highlighted')
