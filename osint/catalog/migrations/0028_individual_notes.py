# Generated by Django 3.1.7 on 2021-05-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0027_auto_20210424_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='notes',
            field=models.ManyToManyField(blank=True, help_text='Anotaciones adicionales', max_length=100, null=True, to='catalog.Note'),
        ),
    ]
