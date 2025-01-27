# Generated by Django 5.0 on 2025-01-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, unique=True, verbose_name='name')),
                ('slug', models.SlugField(null=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Mark',
                'verbose_name_plural': 'Marks',
            },
        ),
    ]
