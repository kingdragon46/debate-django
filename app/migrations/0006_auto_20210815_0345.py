# Generated by Django 3.1.7 on 2021-08-14 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210815_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='for_discussion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discs', to='app.discussion'),
        ),
    ]
