import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.bytea_image.models import ByteaImage
from apps.shared.utils import Utils


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
    main_image = models.OneToOneField(
        to=ByteaImage,
        on_delete=models.CASCADE,
        related_name="category_main_image",
        verbose_name=_('main image'),
        blank=True,
        null=True,
        help_text='image that will be displayed on the home page.'
    )
    secondary_image = models.OneToOneField(
        to=ByteaImage,
        on_delete=models.CASCADE,
        related_name='category_secondary_image',
        verbose_name=_('secondary image'),
        blank=True,
        null=True,
        help_text='image that will be displayed on the category page.'
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Utils.get_slug(self.name)
        super().save(*args, **kwargs)
