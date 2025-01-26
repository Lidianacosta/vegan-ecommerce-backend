from django.db import models

from django.utils.text import gettext_lazy as _

from apps.category.models import Category


class Subcategory(models.Model):
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
