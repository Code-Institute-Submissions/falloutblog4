# Generated by Django 3.2.7 on 2021-09-21 02:24

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, null=True, verbose_name='image'),
        ),
    ]