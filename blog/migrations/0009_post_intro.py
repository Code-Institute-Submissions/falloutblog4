# Generated by Django 3.2.7 on 2021-09-20 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.CharField(default='Default', max_length=100),
        ),
    ]
