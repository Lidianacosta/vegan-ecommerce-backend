import uuid

from django.db import models
from django.utils.text import gettext_lazy as _

from apps.bytea_image.models import ByteaImage
from apps.shared.utils import Utils


class Product(models.Model):
    id = models.UUIDField(
        verbose_name=_('id'),
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        unique=True,
        null=True
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
        max_length=255,
        null=True
    )
    description = models.TextField(
        verbose_name=_('description'),
        default=''
    )
    price = models.FloatField(
        verbose_name=_('price'),
        default=0.0
    )
    stock = models.PositiveIntegerField(
        verbose_name=_('stock'),
        default=0
    )
    image = models.OneToOneField(
        verbose_name=_('image'),
        to=ByteaImage,
        on_delete=models.SET_NULL,
        null=True,
        unique=True
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Utils.get_slug(self.name)
        super().save(*args, **kwargs)
