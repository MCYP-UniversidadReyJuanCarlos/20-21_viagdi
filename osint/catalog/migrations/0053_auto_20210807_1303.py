# Generated by Django 3.1.7 on 2021-08-07 11:03

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0052_auto_20210807_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='home_address',
            field=models.CharField(blank=True, help_text='Dirección de residencia', max_length=60, null=True, verbose_name=catalog.models.Address),
        ),
    ]
