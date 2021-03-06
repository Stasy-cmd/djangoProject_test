# Generated by Django 4.0 on 2021-12-08 17:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LegalEntity',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('id_client', models.IntegerField(blank=True, max_length=7, unique=True, validators=[django.core.validators.RegexValidator(message='identification number (always ends with 01)', regex='\\d*(02)$')])),
                ('name_short', models.CharField(max_length=255)),
                ('name_full', models.TextField()),
                ('inn', models.IntegerField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="KPP number must be entered in the format: '999999999999999'. You need to enter 15 digits", regex='\\d{15}')])),
                ('kpp', models.IntegerField(blank=True, max_length=9, validators=[django.core.validators.RegexValidator(message="KPP number must be entered in the format: '999999999'. You need to enter 9 digits", regex='\\d{9}')])),
            ],
        ),
    ]
