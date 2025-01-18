# Generated by Django 5.0 on 2025-01-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bytea_image', '0003_remove_byteaimage_image_byteaimage_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='byteaimage',
            name='content_type',
            field=models.CharField(default='', max_length=50, verbose_name='content-type'),
        ),
        migrations.AlterField(
            model_name='byteaimage',
            name='image_data',
            field=models.BinaryField(verbose_name='image data'),
        ),
        migrations.AlterField(
            model_name='byteaimage',
            name='image_name',
            field=models.CharField(default='', max_length=255, verbose_name='image name'),
        ),
    ]
