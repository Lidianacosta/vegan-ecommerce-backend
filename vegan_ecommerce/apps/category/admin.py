from django.contrib import admin

from apps.category.models import Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description', 'main_image', 'secondary_image')
    readonly_fields = ('slug',)
