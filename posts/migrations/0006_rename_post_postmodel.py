# Generated by Django 3.2.4 on 2023-04-18 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjeddits', '0004_alter_subjeddit_slug'),
        ('posts', '0005_alter_post_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='PostModel',
        ),
    ]
