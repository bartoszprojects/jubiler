from django.urls import path
from . views import ProductsView, MiniProductsView, ProductsCategoryView, ProductDetail

urlpatterns = [
    path('mini_products', MiniProductsView.as_view()),
    path('all', ProductsView.as_view()),
    path('products_category', ProductsCategoryView.as_view()),
    path('product_details/<int:pk>', ProductDetail.as_view())
]


