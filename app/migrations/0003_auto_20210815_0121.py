# Generated by Django 3.1.7 on 2021-08-14 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210814_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claim',
            name='parent',
        ),
        migrations.AlterField(
            model_name='claim',
            name='type',
            field=models.CharField(choices=[('1', 'For Motion'), ('2', 'Against Motion')], max_length=50, null=True, verbose_name='User Type'),
        ),
    ]
