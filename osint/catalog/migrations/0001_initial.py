# Generated by Django 3.1.4 on 2021-01-07 13:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre completo', max_length=50, verbose_name='Name')),
                ('charge', models.CharField(help_text='Cargo en la entidad', max_length=30, verbose_name='Charge')),
                ('start_date', models.DateField(help_text='Fecha en la que empezó con el cargo', verbose_name='Desde')),
                ('untill', models.DateField(help_text='Fecha de cese', verbose_name='Hasta')),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre completo', max_length=50, verbose_name='Name')),
                ('start_date', models.DateField(help_text='Fecha en la que empezó con el cargo', verbose_name='Desde')),
                ('untill', models.DateField(help_text='Fecha de cese', verbose_name='Hasta')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre de la entidad del administrador', max_length=200, verbose_name='Nombre')),
                ('nif', models.CharField(help_text='NIF/CIF de la entidad del administrador', max_length=20, verbose_name='NIF/CIF')),
            ],
        ),
        migrations.CreateModel(
            name='Ceo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre completo', max_length=50, verbose_name='Name')),
                ('start_date', models.DateField(help_text='Fecha en la que empezó con el cargo', verbose_name='Desde')),
                ('untill', models.DateField(help_text='Fecha de cese', verbose_name='Hasta')),
            ],
        ),
        migrations.CreateModel(
            name='General_director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre completo', max_length=50, verbose_name='Name')),
                ('start_date', models.DateField(help_text='Fecha en la que empezó con el cargo', verbose_name='Desde')),
                ('untill', models.DateField(help_text='Fecha de cese', verbose_name='Hasta')),
            ],
        ),
        migrations.CreateModel(
            name='President',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre completo', max_length=50, verbose_name='Name')),
                ('start_date', models.DateField(help_text='Fecha en la que empezó con el cargo', verbose_name='Desde')),
                ('untill', models.DateField(help_text='Fecha de cese', verbose_name='Hasta')),
            ],
        ),
        migrations.CreateModel(
            name='Secretary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre completo', max_length=50, verbose_name='Name')),
                ('start_date', models.DateField(help_text='Fecha en la que empezó con el cargo', verbose_name='Desde')),
                ('untill', models.DateField(help_text='Fecha de cese', verbose_name='Hasta')),
            ],
        ),
        migrations.CreateModel(
            name='Stockholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre completo', max_length=50, verbose_name='Name')),
                ('start_date', models.DateField(help_text='Fecha en la que empezó con el cargo', verbose_name='Desde')),
                ('untill', models.DateField(help_text='Fecha de cese', verbose_name='Hasta')),
            ],
        ),
        migrations.CreateModel(
            name='Vicepresident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre completo', max_length=50, verbose_name='Name')),
                ('start_date', models.DateField(help_text='Fecha en la que empezó con el cargo', verbose_name='Desde')),
                ('untill', models.DateField(help_text='Fecha de cese', verbose_name='Hasta')),
            ],
        ),
        migrations.CreateModel(
            name='Vocal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre completo', max_length=50, verbose_name='Name')),
                ('start_date', models.DateField(help_text='Fecha en la que empezó con el cargo', verbose_name='Desde')),
                ('untill', models.DateField(help_text='Fecha de cese', verbose_name='Hasta')),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nif', models.CharField(help_text='NIF/CIF de la entidad', max_length=20, verbose_name='NIF/CIF')),
                ('denomination', models.CharField(help_text='Nombre de la entidad', max_length=200, verbose_name='Denominación')),
                ('old_denomination', models.CharField(max_length=200, null=True, verbose_name='Denominación Antigua')),
                ('province', models.CharField(max_length=50, verbose_name='Provincia')),
                ('status', models.CharField(choices=[('a', 'Activa'), ('i', 'Cese de Actividad (inactiva)'), ('d', 'Disolución'), ('l', 'Liquidación'), ('e', 'Extinción'), ('sp', 'Suspensión de pagos'), ('b', 'Quiebra/Bancarrota')], default='a', help_text='Estado de la entidad', max_length=2, verbose_name='Status')),
                ('age', models.CharField(max_length=50, verbose_name='Fecha de Constitución')),
                ('registered_office', models.CharField(max_length=200, verbose_name='Domicilio Social Actual')),
                ('fiscal_domicile', models.CharField(max_length=200, null=True, verbose_name='Domicilio Fiscal Actual')),
                ('social_capital', models.DecimalField(decimal_places=3, max_digits=12, verbose_name='Capital Scial')),
                ('business_name', models.CharField(choices=[('SL', 'Sociedad Limitada'), ('SLNE', 'Sociedad Limitada Nueva Empresa'), ('SLL', 'Sociedad Limitada Laboral'), ('SA', 'Sociedad Anónima'), ('SAL', 'Sociedad Anónima Laboral'), ('SC', 'Sociedad Colectiva'), ('SCom', 'Sociedad Comanditaria Simple'), ('SCoop', 'Sociedad Cooperativa')], default='SL', help_text='Razón Social', max_length=5, verbose_name='Razón Social')),
                ('phone_number', models.IntegerField(verbose_name='Teléfono')),
                ('web', models.CharField(max_length=200, verbose_name='Web')),
                ('sector', models.CharField(max_length=50, verbose_name='Sector')),
                ('corporate_email', models.CharField(max_length=50, null=True, verbose_name='Email Corporativo')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published')),
                ('number_of_agents', models.IntegerField(help_text='Número de vocales de la entidad', null=True, verbose_name='Número de vocales')),
                ('number_of_stockholders', models.IntegerField(help_text='Número de vocales de la accionistas', null=True, verbose_name='Número de accionistas')),
                ('Administradores', models.ManyToManyField(help_text='Administración de la entidad', max_length=50, to='catalog.Administrator')),
            ],
        ),
        migrations.AddField(
            model_name='administrator',
            name='entities',
            field=models.ManyToManyField(help_text='Otra entidad del administrador', null=True, to='catalog.Business'),
        ),
    ]
