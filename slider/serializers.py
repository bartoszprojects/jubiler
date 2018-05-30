from . models import MainSlider, MiniSliderOfferEngraving, MiniSliderOfferRepair, MiniSliderOfferIndividual, \
    AboutInformations, Service, ServiceImages
from rest_framework import serializers

class MiniSliderOfferIndividualSerializer(serializers.ModelSerializer):
    image_thumbnail = serializers.ImageField()
    class Meta:
        model = MiniSliderOfferIndividual
        fields = ('id','title', 'image', 'image_thumbnail')

class MiniSliderOfferRepairSerializer(serializers.ModelSerializer):
    image_thumbnail = serializers.ImageField()
    class Meta:
        model = MiniSliderOfferRepair
        fields = ('id','title', 'image', 'image_thumbnail')

class MiniSliderOfferEngravingSerializer(serializers.ModelSerializer):
    image_thumbnail = serializers.ImageField()
    class Meta:
        model = MiniSliderOfferEngraving
        fields = ('id','title', 'image', 'image_thumbnail')

class MainSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSlider
        fields = ('id','text', 'image', 'baner')

class AboutInformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutInformations
        fields = ('title', 'content')

class ServiceSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Service
        use_url = True
        fields = ('id','title','images','content')
        read_only_fields = ('images',)
    def get_images(self,obj):
        return [img.image.url for img in obj.service_images.all()]

class ServiceImageSerializer(serializers.ModelSerializer):
    service_images = ServiceSerializer(many=True)
    class Meta:
        model = ServiceImages
        fields = ('id','service_images', 'title', 'image')




