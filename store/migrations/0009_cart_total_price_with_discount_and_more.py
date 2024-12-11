# Generated by Django 5.1.2 on 2024-11-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_card_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_price_with_discount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_price_without_discount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
