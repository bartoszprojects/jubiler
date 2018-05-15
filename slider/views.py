from django.shortcuts import render
from rest_framework import generics
from . serializers import MiniSliderOfferIndividualSerializer, MainSliderSerializer, \
    AboutInformationsSerializer, ServiceSerializer, ServiceImageSerializer
from . models import MiniSliderOfferIndividual, MiniSliderOfferRepair, MiniSliderOfferEngraving, MainSlider, AboutInformations, Service, ServiceImages

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

class AboutInformationsSerializerData(generics.ListAPIView):
    queryset = AboutInformations.objects.all()
    serializer_class = AboutInformationsSerializer

class ServiceSerializerData(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceImagesSerializerData(generics.ListAPIView):
    queryset = ServiceImages.objects.all()
    serializer_class = ServiceImageSerializer

