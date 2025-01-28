from rest_framework import serializers

from apps.ingredient.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'slug')
