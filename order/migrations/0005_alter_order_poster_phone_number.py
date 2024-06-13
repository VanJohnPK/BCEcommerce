# Generated by Django 5.0.6 on 2024-06-11 06:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_rename_phone_number_order_poster_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='poster_phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be 10 digits long and start with '1'.", regex='^1\\d{9}$')]),
        ),
    ]