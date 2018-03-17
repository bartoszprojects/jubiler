from . models import ProductsMini, MainProducts
from rest_framework import serializers

class MainProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainProducts
        fields = ('id','title', 'image', 'desc')

class MiniProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsMini
        fields = ('id','title', 'image')

