# Generated by Django 5.0.6 on 2024-06-11 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_poster_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]