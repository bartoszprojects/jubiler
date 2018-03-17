from django.shortcuts import render
from rest_framework import generics
from . serializers import MainProductsSerializer, MiniProductsSerializer
from . models import MainProducts, ProductsMini
# Create your views here.

class ProductsView(generics.ListAPIView):
    queryset = MainProducts.objects.all()
    serializer_class = MainProductsSerializer

class MiniProductsView(generics.ListAPIView):
    queryset = ProductsMini.objects.all()
    serializer_class = MiniProductsSerializer