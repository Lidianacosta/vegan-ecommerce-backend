from django.contrib import admin

from apps.mark.models import Mark


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'slug')
    readonly_fields = ('id', 'slug',)
