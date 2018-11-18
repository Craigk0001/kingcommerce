from django.urls import path, include, re_path
from apps.contact_pages import views

app_name = 'contact_pages'

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('hey', views.sign_up, name='hey'),
]
