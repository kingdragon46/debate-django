# Generated by Django 3.1.7 on 2021-08-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20210815_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='debates',
            field=models.IntegerField(default=0, verbose_name='Debates'),
        ),
    ]