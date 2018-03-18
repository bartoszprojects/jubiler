from django.shortcuts import render
from rest_framework import generics
from . serializers import MiniSliderOfferIndividualSerializer, MainSliderSerializer
from . models import MiniSliderOfferIndividual, MiniSliderOfferRepair, MiniSliderOfferEngraving, MainSlider
# Create your views here.

class MiniSliderOfferIndividualData(generics.ListAPIView):
    queryset = MiniSliderOfferIndividual.objects.all()
    serializer_class = MiniSliderOfferIndividualSerializer

class MiniSliderOfferEngravingData(generics.ListAPIView):
    queryset = MiniSliderOfferEngraving.objects.all()
    serializer_class = MiniSliderOfferIndividualSerializer

class MiniSliderOfferRepairData(generics.ListAPIView):
    queryset = MiniSliderOfferRepair.objects.all()
    serializer_class = MiniSliderOfferIndividualSerializer

class MainSliderData(generics.ListAPIView):
    queryset = MainSlider.objects.all()
    serializer_class = MainSliderSerializer