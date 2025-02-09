import uuid

from django.db import models

from django.utils.text import gettext_lazy as _

from apps.users.models import User


class Order(models.Model):
    ORDER_STATUS = [
        ('P', 'PENDING'),
        ('C', 'CANCELED'),
        ('F', 'FINISHED')
    ]
    id = models.UUIDField(
        verbose_name=_('id'),
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    user = models.ForeignKey(
        verbose_name=_('user'),
        to=User,
        editable=False,
        on_delete=models.DO_NOTHING
    )
    status = models.CharField(
        verbose_name=_('status'),
        choices=ORDER_STATUS,
        max_length=1,
        default='P'
    )
    zip_code = models.CharField(
        verbose_name=_('zip code'),
        max_length=8,
        default=''
    )
    state = models.CharField(
        verbose_name=_('state'),
        max_length=255,
        default=''
    )
    city = models.CharField(
        _('city'),
        max_length=255,
        default=''
    )
    neigborhood = models.CharField(
        verbose_name=_('neigborhood'),
        max_length=255,
        default=''
    )
    street = models.CharField(
        verbose_name=_('street'),
        max_length=255,
        default=''
    )
    number = models.CharField(
        verbose_name=_('number'),
        max_length=10,
        default=''
    )
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"User: {self.user.name}" if self.user else "" \
            f"Pedido: {self.id}"
