# Generated by Django 5.0 on 2024-11-20 01:24

import apps.users.managers
import apps.users.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid email address', regex='^[a-zA-Z0-9._]+@[a-z]+\\.com$')], verbose_name='email address')),
                ('full_name', models.CharField(default='', max_length=100, validators=[django.core.validators.RegexValidator(message='The name must contain only letters', regex='^[a-zá-ùA-ZÁ-Ù]+((?:[\\s][a-zá-ùA-ZÁ-Ù]+)?)+$'), django.core.validators.MinLengthValidator(limit_value=2, message='The name must contain more that two letters')], verbose_name='full name')),
                ('cpf', models.CharField(max_length=14, null=True, unique=True, validators=[apps.users.validators.valid_cpf_validator, django.core.validators.RegexValidator(message='The CPF must contain 11 numbers', regex='^[0-9]{11}$')], verbose_name='CPF')),
                ('date_of_birth', models.DateField(null=True, validators=[apps.users.validators.legal_age_validator], verbose_name='date of birth')),
                ('phone_number', models.CharField(default='', max_length=20, validators=[django.core.validators.RegexValidator(message="The telephone number must contain only numbers and be in the format: 'DDD9XXXXXXXX'", regex='^[0-9]{11}$')], verbose_name='phone number')),
                ('is_admin', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='admin status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', apps.users.managers.UserManager()),
            ],
        ),
    ]