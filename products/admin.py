from django.contrib import admin
from . models import ProductsMini, MainProducts, ProductsCategory, ProductsImages
# Register your models here.

admin.site.register(ProductsMini)
admin.site.register(MainProducts)
admin.site.register(ProductsCategory)
admin.site.register(ProductsImages)