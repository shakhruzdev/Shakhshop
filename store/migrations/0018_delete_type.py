# Generated by Django 5.1.2 on 2024-11-23 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_remove_product_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Type',
        ),
    ]
