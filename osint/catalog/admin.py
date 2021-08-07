import json

from django.contrib import admin

# Register your models here.

from .models import *

# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields


# class AdministratorClassInline(admin.TabularInline):
#     model = Administrator

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    # list_display = ('name', 'nif')
    # list_filter = ('name', 'nif')
    # fields = [('name', 'nif')]
    # AdministratorClassInline.extra = 0
    # inlines = [AdministratorClassInline]
    pass

# class BusinessClassInline(admin.TabularInline):
#     model = Business

@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'charge')
    # list_filter = ('name', 'charge')
    # fields = [('name', 'nif')]
    # BusinessClassInline.extra = 0
    # inlines = [BusinessClassInline]
    # pass

@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = ('nif', 'status') #, 'borrower')
    # list_display = ('nif', 'denomination', 'status')
    # list_filter = ('nif', 'denomination', 'status', 'province', 'age', 'social_capital', 'sector')
    # fields = [('nif', 'denomination'), 'status']
    # fieldsets = (
    #     ('Availability', {
    #         'fields': ('status','borrower')
    #     }),
    # )
    pass

@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    # list_display = ('surname1', 'borrower')
    # fieldsets = (
    #     ('Availability', {
    #         'fields': ('surname1','borrower')
    #     }),
    # )
    pass

@admin.register(SocialMediaAccount)
class SocialMediaAccountAdmin(admin.ModelAdmin):

    pass

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):

    pass

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    pass

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    pass


