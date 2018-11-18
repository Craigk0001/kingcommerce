from django.contrib import admin
from apps.accounts.models import Phone

# Register your models here.


class PhoneAdmin(admin.ModelAdmin):
    list_display = ("user",)
    ordering = ("user",)

admin.site.register(Phone, PhoneAdmin)
