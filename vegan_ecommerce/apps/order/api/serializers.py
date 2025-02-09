from rest_framework import serializers

from apps.order.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'status', 'zip_code', 'state', 'city',
                  'neigborhood', 'street', 'number', 'created_at')
