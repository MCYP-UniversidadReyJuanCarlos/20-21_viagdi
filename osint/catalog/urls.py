from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^entities/$', views.EntityListView.as_view(), name='entities'),
    url(r'^entity/(?P<pk>\d+)$', views.EntityDetailView.as_view(), name='entity-detail'),
    url(r'^administrators/$', views.AdministratorListView.as_view(), name='administrators'),
    url(r'^administrator/(?P<pk>\d+)$', views.AdministratorDetailView.as_view(), name='administrator-detail'),
    url(r'^business/(?P<pk>\d+)$', views.BusinessDetailView.as_view(), name='business-detail'),
    url(r'^individuals/$', views.IndividualListView.as_view(), name='individuals'),
    url(r'^individual/(?P<pk>\d+)$', views.IndividualDetailView.as_view(), name='individual-detail'),
    # url(r'^Social Media Accounts/$', views.SocialMediaAccountListView.as_view(), name='socialmediaaccounts'),
    url(r'^Social Media Account/(?P<pk>\d+)$', views.SocialMediaAccountDetailView.as_view(), name='socialmediaaccount-detail'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^myentities/$', views.RegisteredEntitiesByUserListView.as_view(), name='my-borrowed'),
    url(r'^myindividuals/$', views.RegisteredIndividualsByUserListView.as_view(), name='my-registered'),
    url(r'^entity/create/$', views.EntityCreate.as_view(), name='entity_create'),
    url(r'^entity/(?P<pk>\d+)/update/$', views.EntityUpdate.as_view(), name='entity_update'),
    url(r'^entity/(?P<pk>\d+)/delete/$', views.EntityDelete.as_view(), name='entity_delete'),
    url(r'^administrator/create/$', views.AdministratorCreate.as_view(), name='administrator-create'),
    url(r'^administrator/(?P<pk>\d+)/update/$', views.AdministratorUpdate.as_view(), name='administrator_update'),
    url(r'^administrator/(?P<pk>\d+)/delete/$', views.AdministratorDelete.as_view(), name='administrator_delete'),
    url(r'^business/create/$', views.BusinessCreate.as_view(), name='business-create'),
    url(r'^business/(?P<pk>\d+)/update/$', views.BusinessUpdate.as_view(), name='business-update'),
    url(r'^business/(?P<pk>\d+)/delete/$', views.BusinessDelete.as_view(), name='business-delete'),
    url(r'^individual/create/$', views.IndividualCreate.as_view(), name='individual-create'),
    url(r'^individual/(?P<pk>\d+)/update/$', views.IndividualUpdate.as_view(), name='individual-update'),
    url(r'^individual/(?P<pk>\d+)/delete/$', views.IndividualDelete.as_view(), name='individual-delete'),
    url(r'^socialmediaaccount/create/$', views.SocialMediaAccountCreate.as_view(), name='socialmediaaccount-create'),
    url(r'^socialmediaaccount/(?P<pk>\d+)/update/$', views.SocialMediaAccountUpdate.as_view(), name='socialmediaaccount-update'),
    url(r'^socialmediaaccount/(?P<pk>\d+)/delete/$', views.SocialMediaAccountDelete.as_view(), name='socialmediaaccount-delete'),
    url(r'^email/create/$', views.EmailCreate.as_view(), name='email-create'),
    url(r'^email/(?P<pk>\d+)/update/$', views.EmailUpdate.as_view(), name='email-update'),
    url(r'^email/(?P<pk>\d+)/delete/$', views.EmailDelete.as_view(), name='email-delete'),
    url(r'^address/create/$', views.AddressCreate.as_view(), name='address-create'),
    url(r'^address/(?P<pk>\d+)/update/$', views.AddressUpdate.as_view(), name='address-update'),
    url(r'^address/(?P<pk>\d+)/delete/$', views.AddressDelete.as_view(), name='address-delete'),
    url(r'^vehicle/create/$', views.VehicleCreate.as_view(), name='vehicle-create'),
    url(r'^vehicle/(?P<pk>\d+)/update/$', views.VehicleUpdate.as_view(), name='vehicle-update'),
    url(r'^vehicle/(?P<pk>\d+)/delete/$', views.VehicleDelete.as_view(), name='vehicle-delete'),


# añadir form para registro
]
