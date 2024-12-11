# Generated by Django 5.1.2 on 2024-11-22 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_cart_total_price_with_discount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total_price_without_discount',
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_price_with_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=13),
        ),
    ]