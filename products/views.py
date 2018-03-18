from django.shortcuts import render
from rest_framework import generics
from . serializers import MainProductsSerializer, MiniProductsSerializer, ProductsCategorySerializer
from . models import MainProducts, ProductsMini, ProductsCategory
# Create your views here.

class ProductsView(generics.ListAPIView):
    queryset = MainProducts.objects.all()
    serializer_class = MainProductsSerializer

class MiniProductsView(generics.ListAPIView):
    queryset = ProductsMini.objects.all()
    serializer_class = MiniProductsSerializer

class ProductsCategoryView(generics.ListAPIView):
    queryset = ProductsCategory.objects.all()
    serializer_class = ProductsCategorySerializer