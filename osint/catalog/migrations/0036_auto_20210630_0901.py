# Generated by Django 3.1.7 on 2021-06-30 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0035_auto_20210630_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/static/images/'),
        ),
    ]
