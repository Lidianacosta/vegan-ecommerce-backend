# Generated by Django 5.0 on 2025-01-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bytea_image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='byteaimage',
            name='image_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='byteaimage',
            name='image',
            field=models.ImageField(upload_to='bytea_image'),
        ),
    ]
