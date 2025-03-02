# Generated by Django 5.0 on 2025-02-09 20:28

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('order', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='quantity')),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='cart.cart', verbose_name='cart')),
                ('order', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='order.order', verbose_name='order')),
                ('product', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='product.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order items',
            },
        ),
    ]
