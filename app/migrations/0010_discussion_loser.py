# Generated by Django 3.1.7 on 2021-08-15 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0009_auto_20210815_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='loser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loser', to=settings.AUTH_USER_MODEL),
        ),
    ]
