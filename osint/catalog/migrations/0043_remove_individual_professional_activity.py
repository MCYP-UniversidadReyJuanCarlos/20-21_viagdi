# Generated by Django 3.1.7 on 2021-07-08 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0042_auto_20210701_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individual',
            name='professional_activity',
        ),
    ]
