from django.shortcuts import render
from rest_framework import generics
from . serializers import MainProductsSerializer, MiniProductsSerializer, ProductsCategorySerializer, ProductsImagesSerializer
from . models import MainProducts, ProductsMini, ProductsCategory, ProductsImages

class ProductsView(generics.ListAPIView):
    queryset = MainProducts.objects.all()
    serializer_class = MainProductsSerializer

    def get(self, request, format=None):
        if request.GET.get('index') and request.GET.get('limit'):
            index = int(request.GET.get('index'))
            limit = int(request.GET.get('limit'))
            queryset = MainProducts.objects.all()[index: index + limit]
        else:
            queryset = self.get_queryset()
        serialized_queryset = MainProductsSerializer(queryset, many=True)

        return Response(serialized_queryset.data)

class MiniProductsView(generics.ListAPIView):
    queryset = ProductsMini.objects.all()
    serializer_class = MiniProductsSerializer

class ProductsCategoryView(generics.ListAPIView):
    queryset = ProductsCategory.objects.all()
    serializer_class = ProductsCategorySerializer

class ProductsImagesView(generics.ListAPIView):
    queryset = ProductsImages.objects.all()
    serializer_class = ProductsImagesSerializer

class ProductDetail(generics.RetrieveAPIView):
        queryset = MainProducts.objects.all()
        serializer_class = MainProductsSerializer
class MiniProductDetail(generics.RetrieveAPIView):
    queryset = ProductsMini.objects.all()
    serializer_class = MiniProductsSerializer

    def get_object(self):
        return ProductsMini.objects.get(id=self.kwargs.get("pk"))
