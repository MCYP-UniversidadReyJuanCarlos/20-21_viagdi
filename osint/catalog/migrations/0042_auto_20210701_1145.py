# Generated by Django 3.1.7 on 2021-07-01 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0041_auto_20210630_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='allow_comments',
            field=models.BooleanField(default=True, verbose_name='allow comments'),
        ),
        migrations.AddField(
            model_name='individual',
            name='allow_comments',
            field=models.BooleanField(default=True, verbose_name='allow comments'),
        ),
    ]
