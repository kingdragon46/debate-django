# Generated by Django 3.1.7 on 2021-08-14 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210814_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='User Created On'),
        ),
    ]
