# Generated by Django 3.2.4 on 2023-04-03 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjeddits', '0002_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjeddit',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
