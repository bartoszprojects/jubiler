from django.urls import path
from . views import ProductsView, MiniProductsView, ProductsCategoryView

urlpatterns = [
    path('mini_products', MiniProductsView.as_view()),
    path('all', ProductsView.as_view()),
    path('products_category', ProductsCategoryView.as_view())
]


