
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('', include('apps.core_pages.urls', namespace='core_pages')),
    path('admin/', admin.site.urls),
    path('account/', include('apps.accounts.urls', namespace='user_account')),
    path('contact_us/', include('apps.contact_pages.urls', namespace='contact_pages')),
    path('accounts/', include('allauth.urls')),
    path('checkout/', include('apps.checkout.urls', namespace='checkout')),
    path('product/', include('apps.product_catalogue.urls', namespace='product_catalogue')),
    path('addresses/', include('apps.addresses.urls', namespace='address')),
    path('cart/', include('apps.cart.urls', namespace='cart')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
