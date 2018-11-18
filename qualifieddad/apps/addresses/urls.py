from django.urls import path, include, re_path
from . import views
from apps.addresses.views import AddAddressView

app_name = 'addresses'

urlpatterns = [
    # re_path(r'^add_address/admin/$', AddAddressView.as_view(), name='add_address'),
    re_path(r'^add_address/$', views.add_address_to_user,
    name='add_address_to_user'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.address_delete,
    name='address_delete'),
    re_path(r'^(?P<pk>\d+)/update/$', views.address_update,
    name='address_update'),
]
