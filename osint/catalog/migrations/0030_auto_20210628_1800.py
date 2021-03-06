# Generated by Django 3.1.7 on 2021-06-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0029_auto_20210525_1335'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agent',
        ),
        migrations.DeleteModel(
            name='Ceo',
        ),
        migrations.DeleteModel(
            name='General_director',
        ),
        migrations.DeleteModel(
            name='President',
        ),
        migrations.DeleteModel(
            name='Secretary',
        ),
        migrations.DeleteModel(
            name='Stockholder',
        ),
        migrations.DeleteModel(
            name='Vicepresident',
        ),
        migrations.DeleteModel(
            name='Vocal',
        ),
        migrations.AlterField(
            model_name='entity',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='socialmediaaccount',
            name='url',
            field=models.CharField(blank=True, help_text='URL de la cuent de usuario', max_length=20, null=True, verbose_name='URL de la cuenta de usuario'),
        ),
    ]
