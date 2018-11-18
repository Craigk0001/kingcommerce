from django.contrib import admin
from apps.shipping.models import ShippingZone, ShippingMethod, ShippingClass, MethodClass, EstimatedDelivery

# Register your models here.


class ShippingZoneAdmin(admin.ModelAdmin):
    list_display = ("name", "regions", "pk")
    ordering = ("name",)

class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "pk")
    ordering = ("name",)

class ShippingClassAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "pk")
    ordering = ("name",)

class MethodClassAdmin(admin.ModelAdmin):
    list_display = ("flat_rate_calculation", "pk")
    ordering = ("flat_rate_calculation",)

class EstimatedDeliveryAdmin(admin.ModelAdmin):
    list_display = ("name", "days_minimum", "days_maximum", "pk")
    ordering = ("name",)

admin.site.register(ShippingZone, ShippingZoneAdmin)
admin.site.register(ShippingMethod, ShippingMethodAdmin)
admin.site.register(ShippingClass, ShippingClassAdmin)
admin.site.register(MethodClass, MethodClassAdmin)
admin.site.register(EstimatedDelivery, EstimatedDeliveryAdmin)
