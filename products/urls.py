from django.urls import path
from . views import ProductsView, MiniProductsView

urlpatterns = [
    path('mini_products', MiniProductsView.as_view()),
    path('all', ProductsView.as_view())
]


