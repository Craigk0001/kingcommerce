from django.contrib import admin
from apps.images.models import Image

# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "pk")
    ordering = ("title",)

admin.site.register(Image, ImageAdmin)
