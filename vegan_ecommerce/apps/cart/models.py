import uuid

from django.db import models

from django.utils.text import gettext_lazy as _

from apps.users.models import User


class Cart(models.Model):
    id = models.UUIDField(
        verbose_name=_('id'),
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    user = models.OneToOneField(
        verbose_name=_('user'),
        to=User,
        editable=False,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return f"Cart of user: {self.user.name} - " if self.user else "" \
            f"Cart: {self.id}"
