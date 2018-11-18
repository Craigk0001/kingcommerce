from django.urls import path, include, re_path
from . import views
from apps.accounts.views import UserAddressView, UserSecurityView

app_name = 'user_account'

urlpatterns = [
    path('profile', views.user_profile, name='profile'),
    path('addresses', UserAddressView.as_view(), name='user_address'),
    path('security', UserSecurityView.as_view(), name='security'),
    path('change_name', views.change_name_view, name='change_name'),
]
