from django.contrib import admin
from apps.addresses.models import Address

# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    list_display = ("address_line1",)
    ordering = ("address_line1",)

admin.site.register(Address, AddressAdmin)
