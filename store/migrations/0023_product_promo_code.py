# Generated by Django 5.1.2 on 2024-12-05 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_remove_product_is_trending'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='promo_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
