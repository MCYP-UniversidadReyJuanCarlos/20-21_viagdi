# Generated by Django 3.1.7 on 2021-07-28 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0045_auto_20210718_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='allow_comments',
        ),
        migrations.RemoveField(
            model_name='entity',
            name='notes',
        ),
    ]