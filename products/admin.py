from django.contrib import admin
from . models import ProductsMini, MainProducts, ProductsCategory, ProductsImages

admin.site.register(ProductsMini)
admin.site.register(ProductsCategory)

class ImageInline(admin.StackedInline):
    model = ProductsImages
    fields = ['image',]

class MainProductsAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

admin.site.register(MainProducts, MainProductsAdmin)