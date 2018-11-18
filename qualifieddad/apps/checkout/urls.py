from django.urls import path, include, re_path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('test', views.test, name='test'),
]
