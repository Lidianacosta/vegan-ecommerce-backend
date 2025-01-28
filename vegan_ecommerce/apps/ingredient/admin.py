from django.contrib import admin

from apps.ingredient.models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'slug')
    readonly_fields = ('id', 'slug',)
