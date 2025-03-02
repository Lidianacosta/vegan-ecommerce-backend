# Generated by Django 5.0 on 2024-11-25 11:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=255, null=True, unique=True, verbose_name='slug')),
                ('description', models.TextField(default='', verbose_name='description')),
                ('main_image', models.ImageField(blank=True, help_text='image that will be displayed on the home page.', null=True, upload_to='category/main_image/%Y/%m', verbose_name='main image')),
                ('secondary_image', models.ImageField(blank=True, help_text='image that will be displayed on the category page.', null=True, upload_to='category/secondary_image/%Y/%m', verbose_name='secondary image')),
            ],
        ),
    ]
