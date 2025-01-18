from django.contrib import admin

from apps.bytea_image.forms import ByteaImageAddForm, ByteaImagechangeForm
from apps.bytea_image.models import ByteaImage


class ByteaImageAdmin(admin.ModelAdmin):
    readonly_fields = ('image_name', 'content_type')

    fieldsets = [
        (
            "Image information",
            {
                "fields": ['image_name', 'content_type'],
            },
        ),
        (
            "Upload image",
            {
                "fields": ["image"],
            },
        ),
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        kwargs["form"] = ByteaImagechangeForm if change else ByteaImageAddForm
        return super().get_form(request, obj, **kwargs)


admin.site.register(ByteaImage, ByteaImageAdmin)
