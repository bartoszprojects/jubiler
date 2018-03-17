from . models import MainSlider, MiniSliderOfferEngraving, MiniSliderOfferRepair, MiniSliderOfferIndividual
from rest_framework import serializers

class MiniSliderOfferIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiniSliderOfferIndividual
        fields = ('id','title', 'image')

class MainSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSlider
        fields = ('id','text', 'image', 'baner')
