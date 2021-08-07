from django.db import models

# Create your models here.

from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Business(models.Model):
    denomination = models.CharField('Nombre', max_length=200, help_text='Nombre de la entidad del administrador')
    nif = models.CharField('NIF/CIF', max_length=20, help_text='NIF/CIF de la entidad del administrador')
    charge = models.CharField('Cargo', max_length=20, help_text='Cargo que desempeña en la entidad', null=True, blank=True)
    from_date = models.DateField('Desde', null=True, blank=True)

    def __str__(self):
        return self.denomination

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de entity
        """
        return reverse('business-detail', args=[str(self.id)])


class Administrator(models.Model):
    name = models.CharField('Name', max_length=50, help_text='Nombre completo')
    charge = models.CharField('Charge', max_length=30, help_text='Cargo en la entidad')
    start_date = models.DateField('Desde', help_text='Fecha en la que empezó con el cargo', null=True, blank=True)
    untill = models.DateField('Hasta', help_text='Fecha de cese', null=True, blank=True)
    other_entities = models.ManyToManyField(Business, help_text='Otra entidad del administrador', null=True, blank=True)


    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de entity
        """
        return reverse('administrator-detail', args=[str(self.id)])




class Entity(models.Model):

    BUSINESS_SORTS = (
        ('SL', 'Sociedad Limitada'),
        ('SLNE', 'Sociedad Limitada Nueva Empresa'),
        ('SLL', 'Sociedad Limitada Laboral'),
        ('SA', 'Sociedad Anónima'),
        ('SAL', 'Sociedad Anónima Laboral'),
        ('SC', 'Sociedad Colectiva'),
        ('SCom', 'Sociedad Comanditaria Simple'),
        ('SCoop', 'Sociedad Cooperativa')
    )

    STATUS_SORTS = (
        ('Activa', 'Activa'),
        ('Inactiva', 'Cese de Actividad (inactiva)'),
        ('Disuelta', 'Disolución'),
        ('En Liquidación', 'Liquidación'),
        ('Extinguida', 'Extinción'),
        ('Suspensión de pagos', 'Suspensión de pagos'),
        ('Quiebra/Bancarrota', 'Quiebra/Bancarrota')
    )

    nif = models.CharField('NIF/CIF', max_length=20, help_text='NIF/CIF de la entidad')
    denomination = models.CharField('Denominación', max_length=200, help_text='Nombre de la entidad')
    old_denomination = models.CharField('Denominación Antigua', max_length=200, null=True)
    province = models.CharField('Provincia', max_length=50)
    status = models.CharField('Status', max_length=50, choices=STATUS_SORTS, default='a',
                              help_text='Estado de la entidad')
    age = models.CharField('Fecha de Constitución', max_length=50)
    registered_office = models.CharField('Domicilio Social Actual', max_length=200)
    # registered_office = models.OneToOneField(Map, help_text='Domicilio Social actual', max_length=200, on_delete=models.CASCADE)
    fiscal_domicile = models.CharField('Domicilio Fiscal Actual', max_length=200, null=True)
    social_capital = models.DecimalField('Capital Scial', decimal_places=3, max_digits=12)
    business_name = models.CharField('Razón Social', max_length=5, choices=BUSINESS_SORTS,
                                     default='SL', help_text='Razón Social')
    phone_number = models.IntegerField('Teléfono')
    # web = models.CharField('Web', max_length=200)
    web = models.URLField('Web', null=True, blank=True)
    sector = models.CharField('Sector', max_length=50)
    corporate_email = models.CharField('Email Corporativo', max_length=50, null=True)
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    # number_of_agents = models.IntegerField('Número de vocales', null=True,
    #                                        help_text='Número de vocales de la entidad')
    # number_of_stockholders = models.IntegerField('Número de accionistas', null=True,
    #                                              help_text='Número de vocales de la accionistas')
    Administradores = models.ManyToManyField(Administrator, help_text='Administración de la entidad', max_length=50)
    logo = models.ImageField(upload_to="images/", null=True, blank=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=10, null=True, blank=True)
    longitud = models.DecimalField(max_digits=12, decimal_places=10, null=True, blank=True)
    borrower = models.ManyToManyField(User)
    # borrower = models.ManyToManyField(User, help_text='Analista asociado a esta entidad', null=True, blank=True, max_length=50)
    # allow_comments = models.BooleanField('allow comments', default=True)


    def __str__(self):
        return self.nif

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de entity
        """
        return reverse('entity-detail', args=[str(self.id)])

    class Meta:
        ordering = ['denomination']

class SocialMediaAccount(models.Model):

    MEDIA = (
        ('Twitter', 'Twitter'),
        ('Instagram', 'Instagram'),
        ('Linkedin', 'Linkedin'),
        ('Whatsapp', 'Whatsapp'),
        ('Facebook', 'Facebook')
    )

    user_id = models.CharField('ID de la cuenta de usuario', max_length=50, null=True, help_text='ID de la cuent de usuario')
    email = models.CharField('Email Asociado', max_length=50, null=True, help_text='Email asociado')
    user_name = models.CharField('Nombre de usuario', max_length=20, help_text='Nombre de usuario')
    social_media = models.CharField('Red social', max_length=20, help_text='Red social', choices=MEDIA, default=None)
    url = models.CharField('URL de la cuenta de usuario', help_text='URL de la cuent de usuario', null=True, blank=True, max_length=200)
    followers = models.IntegerField('Seguidores')
    following = models.IntegerField('Seguidos')

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de entity
        """
        return reverse('socialmediaaccount-detail', args=[str(self.id)])

    class Meta:
        ordering = ['social_media']

class Email(models.Model):
    email = models.CharField('Email', max_length=50, null=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de entity
        """
        return reverse('email-detail', args=[str(self.id)])

    class Meta:
        ordering = ['email']

class Address(models.Model):
    address = models.CharField('Dirección', max_length=50, null=True)

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de entity
        """
        return reverse('address-detail', args=[str(self.id)])

    class Meta:
        ordering = ['address']

class Vehicle(models.Model):
    type = models.CharField('Tipo de vehículo', max_length=50, null=True)
    number_plate = models.CharField('Matrícula', max_length=50, null=True)
    brand = models.CharField('Marca', max_length=50, null=True)
    model = models.CharField('Modelo', max_length=50, null=True)
    colour = models.CharField('Color', max_length=50, null=True)
    first_date_plate = models.DateField('Primera matriculación', null=True, blank=True)

    def __str__(self):
        return self.number_plate

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de entity
        """
        return reverse('vehicle-detail', args=[str(self.id)])

    class Meta:
        ordering = ['number_plate']

class Individual(models.Model):

    user_dni = models.CharField('DNI', max_length=20, help_text='DNI de la persona', null=True, blank=True)
    name = models.CharField('Nombre', max_length=20, help_text='Nombre de la persona')
    surname1 = models.CharField('Primer Apellido', max_length=20, help_text='Primer apellido de la persona')
    surname2 = models.CharField('Segundo Apellido', max_length=20, help_text='Segundo apellido de la persona', null=True, blank=True)
    age = models.IntegerField('Edad')
    nationatility = models.CharField('Nacionalidad', max_length=20, help_text='Nacionalidad de la persona')
    home_address = models.CharField(Address, max_length=60, help_text='Dirección de residencia', null=True, blank=True)
    home_address_latitude = models.DecimalField(max_digits=12, decimal_places=10, null=True, blank=True, help_text='Latitud de su última residencia conocida')
    home_address_longitud = models.DecimalField(max_digits=12, decimal_places=10, null=True, blank=True, help_text='Longitud de su última residencia conocida')
    other_addresses = models.ManyToManyField(Address, max_length=20, help_text='Otras direcciones conocidas', blank=True)
    professional_status = models.CharField('Estatus Laboral', max_length=20, help_text='Estatus laboral del individuo', default='Inactivo')
    charge = models.CharField('Cargo laboral', max_length=20, help_text='Cargo que desempeña laboralmente', null=True, blank=True)
    # heritage = models.IntegerField('Patrimonio')
    social_accounts = models.ManyToManyField(SocialMediaAccount, help_text='Cuentas en redes sociales', max_length=50, blank=True)
    # ip_adresses = models.ManyToManyField('Direcciones IP', help_text='Direcciones IP asociadas', max_length=50, null=True, blank=True)
    email_accounts = models.ManyToManyField(Email, help_text='Cuentas de email', max_length=50, blank=True)
    phone = models.PositiveBigIntegerField('Número de teléfono', null=True, blank=True)
    vehicles = models.ManyToManyField(Vehicle, help_text='Vehículos de su propiedad', max_length=50, blank=True)
    borrower = models.ManyToManyField(User)
    # borrower = models.ManyToManyField(User, help_text='Analista asociado a este individuo', null=True, blank=True, max_length=50)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    # allow_comments = models.BooleanField('allow comments', default=True)
    pub_date = models.DateTimeField('Date published', default=timezone.now)


    def __str__(self):
        return self.surname1

    class Meta:
        ordering = ['surname1']

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de entity
        """
        return reverse('individual-detail', args=[str(self.id)])


