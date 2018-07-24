from django.urls import path
from . views import ProductsView, MiniProductsView, ProductsCategoryView, ProductDetail, MiniProductDetail, ProductsImagesView

urlpatterns = [
    path('mini_products', MiniProductsView.as_view()),
    path('all', ProductsView.as_view()),
    path('products_category', ProductsCategoryView.as_view()),
    path('product_details/<int:pk>', ProductDetail.as_view()),
    path('mini_product_details/<int:pk>', MiniProductDetail.as_view()),
    path('products_images', ProductsImagesView.as_view()),
]
