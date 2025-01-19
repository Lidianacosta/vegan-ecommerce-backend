# Generated by Django 5.0 on 2025-01-18 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bytea_image', '0004_alter_byteaimage_content_type_and_more'),
        ('category', '0003_remove_category_main_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='main_image',
            field=models.OneToOneField(blank=True, help_text='image that will be displayed on the home page.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_main_image', to='bytea_image.byteaimage', verbose_name='main image'),
        ),
        migrations.AddField(
            model_name='category',
            name='secondary_image',
            field=models.OneToOneField(blank=True, help_text='image that will be displayed on the category page.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_secondary_image', to='bytea_image.byteaimage', verbose_name='secondary image'),
        ),
    ]
