from rest_framework import serializers

from apps.order_item.models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ('id', 'cart', 'order', 'product', 'quantity', 'total')

    def get_total(self, obj):
        return float(obj.product.price) * int(obj.quantity)
