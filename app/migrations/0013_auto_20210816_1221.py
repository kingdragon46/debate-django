# Generated by Django 3.1.7 on 2021-08-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_discussion_is_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Deleted'),
        ),
        migrations.AddField(
            model_name='comment',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Deleted'),
        ),
        migrations.AddField(
            model_name='discussion',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Deleted'),
        ),
    ]
