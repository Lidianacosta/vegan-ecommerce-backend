import uuid

from django.db import models

from django.utils.text import gettext_lazy as _

from apps.cart.models import Cart
from apps.order.models import Order
from apps.product.models import Product


class OrderItem(models.Model):
    id = models.UUIDField(
        verbose_name=_('id'),
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    cart = models.ForeignKey(
        verbose_name=_('cart'),
        to=Cart,
        related_name='items',
        null=True,
        on_delete=models.DO_NOTHING
    )
    order = models.ForeignKey(
        verbose_name=_('order'),
        to=Order,
        editable=False,
        related_name='items',
        on_delete=models.DO_NOTHING
    )
    product = models.ForeignKey(
        verbose_name=_('product'),
        to=Product,
        editable=False,
        related_name='items',
        on_delete=models.DO_NOTHING
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_('quantity'),
        default=0
    )

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order items'

    def __str__(self):
        local = ''
        if self.order:
            local = "Order: {self.order.id} - "
        elif self.cart:
            local = "Cart: {self.cart.id} - "
        return local + f"Item: {self.id}"
