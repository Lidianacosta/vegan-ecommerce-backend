# Generated by Django 5.0 on 2025-01-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bytea_image', '0002_byteaimage_image_name_alter_byteaimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='byteaimage',
            name='image',
        ),
        migrations.AddField(
            model_name='byteaimage',
            name='content_type',
            field=models.CharField(default='', max_length=50),
        ),
    ]
