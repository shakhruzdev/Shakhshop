# Generated by Django 5.1.2 on 2024-12-02 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_card_qr_code_card_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='qr_code',
        ),
        migrations.RemoveField(
            model_name='card',
            name='uuid',
        ),
    ]
