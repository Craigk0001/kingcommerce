from django.urls import path, include, re_path
from apps.core_pages import views

app_name = 'core_pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us', views.about_us, name='about_us'),

]
