# Generated by Django 3.1.4 on 2021-01-27 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_entity_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='logo',
        ),
    ]
