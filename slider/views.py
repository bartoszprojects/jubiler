import base64
from django.core.files.base import ContentFile

from django.shortcuts import render
from rest_framework import generics
from rest_framework import views
from rest_framework import views
from rest_framework.response import Response
from django.core.mail import send_mail, EmailMessage
from .serializers import MiniSliderOfferIndividualSerializer, MainSliderSerializer, \
    AboutInformationsSerializer, ServiceSerializer, ServiceImageSerializer, ContactSerializer
from .models import MiniSliderOfferIndividual, MiniSliderOfferRepair, MiniSliderOfferEngraving, MainSlider, \
    AboutInformations, Service, ServiceImages


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


class ServiceSerializerData(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceImagesSerializerData(generics.ListAPIView):
    queryset = ServiceImages.objects.all()
    serializer_class = ServiceImageSerializer


class ContactSerializerData(generics.ListCreateAPIView):
    queryset = ''
    serializer_class = ContactSerializer

    def post(self, request, format=None):
        serializer = ContactSerializer(many=True)
        data = request.data.copy()

        # Convert base64 to ImageField instance
        base64_image = data.get('image')
        if base64_image:
            format, imgstr = base64_image.split(';base64,')
            ext = format.split('/')[-1]
            # Convert base64 to ImageField
            image = ContentFile(base64.b64decode(imgstr), name='temp.' + ext) # You can save this as file instance.
            data['image'] = image

        postserializer = ContactSerializer(data=data)
        if postserializer.is_valid():
            postserializer.save()
            data = postserializer.validated_data
            image = data.get('image')
            form_name = data['name']
            form_email = data['email']
            form_phone = data.get('phone_number', '')
            form_message = data['message']
            form_subject = "Wiadomość od klienta ze strony slojewski.pl"
            form_all = "Email klienta: " + form_email + "\n" + "Telefon klienta: " + \
                       form_phone + "\n" + "\n" + "Treść wiadomości:" + "\n" + form_message

            mail = EmailMessage(form_name, form_all, form_email, ['bartosz.projects1@gmail.com','theoden77@o2.pl', 'itsawesome17@gmail.com'])
            if image:
                mail.attach(image.name, image.read(), image.content_type)

            # Send an email
            mail.send()
            return Response(postserializer.data)

        return Response(serializer.data)
