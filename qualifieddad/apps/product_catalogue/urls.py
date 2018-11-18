from django.urls import path, include, re_path
from apps.product_catalogue import views

app_name = 'product_catalogue'

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', views.product_overview, name='product'),
    re_path(r'^category/(?P<pk>\d+)/$', views.category, name='category'),
    re_path(r'^review/(?P<pk>\d+)/$', views.review, name='review'),
    re_path(r'^review_helpfulness/(?P<pk>\d+)/$', views.review_helpfulness, name='review_helpfulness'),
]
