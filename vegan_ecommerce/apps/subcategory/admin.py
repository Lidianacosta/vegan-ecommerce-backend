from django.contrib import admin

from apps.subcategory.models import Subcategory


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'slug', 'category', 'description')
    readonly_fields = ('id', 'slug',)
