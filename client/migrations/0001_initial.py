# Generated by Django 4.0 on 2021-12-08 17:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('id_client', models.IntegerField(blank=True, max_length=7, unique=True, validators=[django.core.validators.RegexValidator(message='identification number (always ends with 01)', regex='\\d*(01)$')])),
                ('phone_number', models.IntegerField(blank=True, max_length=7, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('additional_numbers', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'ACTIVE'), ('not_active', 'NOT ACTIVE')], default='active', max_length=255)),
                ('type_of_client', models.CharField(choices=[('primary', 'первичный'), ('repeated', 'повторный'), ('external', 'внешний'), ('indirect', 'косвенный')], default='primary', max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('timezone', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский'), ('unknown', 'Неизвестно')], default='Неизвестно', max_length=255)),
            ],
        ),
    ]
