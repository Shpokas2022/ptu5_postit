# Generated by Django 4.1.3 on 2022-11-24 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postit_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created_at'),
        ),
    ]
