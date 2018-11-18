from django.contrib import admin
from apps.cart.models import Cart, CartSelection
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ("pk",)
    ordering = ("pk",)

class CartSelectionAdmin(admin.ModelAdmin):
    list_display = ("pk",)
    ordering = ("pk",)

admin.site.register(Cart, CartAdmin)
admin.site.register(CartSelection, CartSelectionAdmin)
