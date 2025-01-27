import uuid
from django.db import models

from django.utils.text import gettext_lazy as _

from apps.category.models import Category

from apps.shared.utils import Utils


class Subcategory(models.Model):
    id = models.UUIDField(
        _('id'),
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    name = models.CharField(
        _("name"),
        max_length=255,
        unique=True,
        null=True
    )
    slug = models.SlugField(
        _('slug'),
        max_length=255,
        null=True
    )
    description = models.TextField(
        _('description'),
        default=''
    )
    category = models.ForeignKey(
        verbose_name=_('category'),
        to=Category,
        related_name='subcategories',
        null=True,
        on_delete=models.SET_NULL
    )
    is_highlighted = models.BooleanField(
        _('is highlighted ?'),
        default=False
    )

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Utils.get_slug(self.name)
        super().save(*args, **kwargs)
