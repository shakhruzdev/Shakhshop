# Generated by Django 5.1.2 on 2024-10-18 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='img/user/default_user.png', upload_to='user/images/'),
        ),
    ]
