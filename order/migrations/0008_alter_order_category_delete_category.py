# Generated by Django 5.0.6 on 2024-06-11 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_order_is_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='category',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
