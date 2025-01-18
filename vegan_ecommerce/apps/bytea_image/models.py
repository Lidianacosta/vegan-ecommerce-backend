import uuid

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class ByteaImage(models.Model):
    id = models.UUIDField(
        _('id'),
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    image_name = models.CharField(
        _('image name'),
        max_length=255,
        default=''
    )
    content_type = models.CharField(
        _('content-type'),
        max_length=50,
        default=''
    )
    image_data = models.BinaryField(_('image data'))

    def get_absolute_url(self):
        return reverse('bytea_image:bytea_image', args=(self.id,))

    def __str__(self):
        return str(self.image_name)
