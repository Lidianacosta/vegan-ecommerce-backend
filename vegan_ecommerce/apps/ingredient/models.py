import uuid

from django.db import models
from django.utils.text import gettext_lazy as _

from apps.shared.utils import Utils


class Ingredient(models.Model):
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

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Utils.get_slug(self.name)
        super().save(*args, **kwargs)
