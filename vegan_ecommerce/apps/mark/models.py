import uuid

from django.db import models
from django.utils.text import gettext_lazy as _

from apps.shared.utils import Utils


class Mark(models.Model):
    id = models.UUIDField(
        _('id'),
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
        null=True
    )

    class Meta:
        verbose_name = 'Mark'
        verbose_name_plural = 'Marks'

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Utils.get_slug(self.name)
        super().save(*args, **kwargs)
