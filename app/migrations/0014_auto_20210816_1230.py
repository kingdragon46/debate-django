# Generated by Django 3.1.7 on 2021-08-16 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210816_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='p1dislike',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='P1 likes'),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='p1like',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='P1 likes'),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='p2dislike',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='P2 likes'),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='p2like',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='P2 likes'),
        ),
    ]
