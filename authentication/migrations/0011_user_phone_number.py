# Generated by Django 5.1.2 on 2024-11-27 13:56

import authentication.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=13, null=True, unique=True, validators=[authentication.utils.validate_uz_phone_number]),
        ),
    ]