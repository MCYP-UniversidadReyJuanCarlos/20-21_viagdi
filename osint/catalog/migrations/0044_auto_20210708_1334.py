# Generated by Django 3.1.7 on 2021-07-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0043_remove_individual_professional_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediaaccount',
            name='url',
            field=models.CharField(blank=True, help_text='URL de la cuent de usuario', max_length=200, null=True, verbose_name='URL de la cuenta de usuario'),
        ),
    ]