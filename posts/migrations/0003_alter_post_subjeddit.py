# Generated by Django 3.2.4 on 2023-04-03 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjeddits', '0003_subjeddit_slug'),
        ('posts', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subjeddit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='subjeddits.subjeddit'),
        ),
    ]
