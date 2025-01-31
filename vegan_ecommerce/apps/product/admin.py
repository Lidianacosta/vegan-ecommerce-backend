from django.contrib import admin

from apps.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'slug', 'price', 'stock', 'image', 'description')
    readonly_fields = ('id', 'slug',)
