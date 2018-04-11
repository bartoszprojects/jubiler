from . models import MainSlider, MiniSliderOfferEngraving, MiniSliderOfferRepair, MiniSliderOfferIndividual, \
    AboutInformations
from rest_framework import serializers

class MiniSliderOfferIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniSliderOfferIndividual
        fields = ('id','title', 'image')

class MiniSliderOfferRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniSliderOfferRepair
        fields = ('id','title', 'image')

class MiniSliderOfferEngravingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniSliderOfferEngraving
        fields = ('id','title', 'image')

class MainSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSlider
        fields = ('id','text', 'image', 'baner')

class AboutInformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutInformations
        fields = ('title', 'content')
