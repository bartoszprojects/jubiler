from . models import ProductsMini, MainProducts, ProductsCategory
from rest_framework import serializers



class MainProductsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)
    image_thumbnail = serializers.ImageField()
    class Meta:
        model = MainProducts
        fields = ('id','title','image','image_thumbnail','desc','category',)

class ProductsCategorySerializer(serializers.ModelSerializer):
    category = MainProductsSerializer(many=True, read_only=True)
    class Meta:
        model = ProductsCategory
        fields = ('id', 'title', 'category',)

class MiniProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsMini
        fields = ('id','title', 'image')

