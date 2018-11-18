from django.urls import path, include, re_path
from apps.cart import views

app_name = 'cart'

urlpatterns = [
    re_path('my_cart', views.cart, name='cart'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.item_delete,
    name='item_delete'),
]
