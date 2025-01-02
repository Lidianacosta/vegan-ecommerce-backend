import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    id = models.UUIDField(
        _('id'),
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    name = models.CharField(
        _('name'),
        max_length=255,
        unique=True
    )
    slug = models.SlugField(
        _('slug'),
        max_length=255,
        unique=True,
        null=True
    )
    description = models.TextField(_('description'), default='')
    main_image = models.ImageField(
        _('main image'),
        upload_to='category/main_image/%Y/%m',
        blank=True,
        null=True,
        help_text='image that will be displayed on the home page.'
    )
    secondary_image = models.ImageField(
        _('secondary image'),
        upload_to='category/secondary_image/%Y/%m',
        blank=True,
        null=True,
        help_text='image that will be displayed on the category page.'
    )

    def __str__(self):
        return str(self.name)
