# Generated by Django 3.2.4 on 2023-04-18 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_rename_post_postmodel'),
        ('subjeddits', '0004_alter_subjeddit_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subjeddit',
            new_name='SubjedditModel',
        ),
    ]
