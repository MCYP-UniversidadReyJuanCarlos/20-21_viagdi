# Generated by Django 3.1.7 on 2021-08-08 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0053_auto_20210807_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='untill',
            field=models.DateField(blank=True, default=datetime.datetime, help_text='Fecha de cese', null=True, verbose_name='Hasta'),
        ),
    ]
