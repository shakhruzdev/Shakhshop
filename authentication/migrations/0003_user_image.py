# Generated by Django 5.1.2 on 2024-10-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_managers_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='static/img/user/default_user.svg', upload_to='user/images/'),
        ),
    ]
