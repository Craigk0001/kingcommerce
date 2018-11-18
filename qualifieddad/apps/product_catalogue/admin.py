from django.contrib import admin
from apps.product_catalogue.models import (
ProductPost,
Product,
Options,
Category,
Values,
GalleryImage,
Review,
ReviewHelpfulness,
Attribute,
AttributeValue,
Variation,
)

# Register your models here.


class ProductPostAdmin(admin.ModelAdmin):
    list_display = ("title", "pk")
    ordering = ("title",)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "pk")
    ordering = ("name",)

class OptionsAdmin(admin.ModelAdmin):
    list_display = ("name", "staff_name")
    ordering = ("name",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    ordering = ("name",)

class ValuesAdmin(admin.ModelAdmin):
    list_display = ("name", "option")
    ordering = ("name",)

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("priority",)
    ordering = ("priority",)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("content",)
    ordering = ("content",)

class ReviewHelpfulnessAdmin(admin.ModelAdmin):
    list_display = ("created",)
    ordering = ("created",)

class AttributeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)

class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)

class VariationAdmin(admin.ModelAdmin):
    list_display = ("id",)
    ordering = ("id",)


admin.site.register(ProductPost, ProductPostAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Options, OptionsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Values, ValuesAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewHelpfulness, ReviewHelpfulnessAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(AttributeValue, AttributeValueAdmin)
admin.site.register(Variation, VariationAdmin)
