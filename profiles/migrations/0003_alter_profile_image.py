# Generated by Django 3.2.23 on 2024-02-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_ggty4q', upload_to='images/'),
        ),
    ]
