from . models import ProductsMini, MainProducts, ProductsCategory, ProductsImages
from rest_framework import serializers




class MainProductsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)
    to_product = serializers.SerializerMethodField()
    class Meta:
        model = MainProducts
        use_url = True
        read_only_fields = ('to_product',)
        fields = ('id','title','desc','category','to_product')
    def get_to_product(self, obj):
        return [img.image.url for img in obj.to_product.all()]

class ProductsCategorySerializer(serializers.ModelSerializer):
    category = MainProductsSerializer(many=True, read_only=True)
    class Meta:
        model = ProductsCategory
        fields = ('id', 'title', 'category',)

class ProductsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsImages
        fields = ('id', 'title', 'image')

class MiniProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsMini
        fields = ('id','title', 'image')

