# Generated by Django 5.0.6 on 2024-06-11 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='phone_number',
            new_name='poster_phone_number',
        ),
    ]