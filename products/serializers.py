from . models import ProductsMini, MainProducts, ProductsCategory
from rest_framework import serializers

class MainProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainProducts
        fields = ('id','title', 'image', 'desc')

class MiniProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsMini
        fields = ('id','title', 'image')

class ProductsCategorySerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=True)
    class Meta:
        model = ProductsCategory
        fields = ('id','title', 'product')
