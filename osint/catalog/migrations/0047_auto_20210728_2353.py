# Generated by Django 3.1.7 on 2021-07-28 21:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0046_auto_20210728_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individual',
            name='allow_comments',
        ),
        migrations.RemoveField(
            model_name='individual',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='individual',
            name='borrower',
        ),
        migrations.AddField(
            model_name='individual',
            name='borrower',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
