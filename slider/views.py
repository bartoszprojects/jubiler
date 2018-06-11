from django.shortcuts import render
from rest_framework import generics
from rest_framework import views
from rest_framework import views
from rest_framework.response import Response
import sendgrid
import os
from sendgrid.helpers.mail import *

from . serializers import MiniSliderOfferIndividualSerializer, MainSliderSerializer, \
    AboutInformationsSerializer, ServiceSerializer, ServiceImageSerializer, ContactSerializer
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
        postserializer = ContactSerializer(data=request.data)
        if postserializer.is_valid():
            postserializer.save()
            data = postserializer.data
            print (postserializer.data)
            form_name = data['name']
            form_email = data['email']
            form_phone = data['phone']
            form_message = data['message']
            print ('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            print (form_message)

            sg = sendgrid.SendGridAPIClient(apikey="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")



            from_email = Email("test@example.com")
            to_email = Email("bartosz.projects1@gmail.com")
            subject = "Sending with SendGrid is Fun"
            content = Content("text/plain", "and easy to do anywhere, even with Python")
            first_name = Content("text/plain", 'hehehe')
            mail = Mail(from_email=from_email, subject=subject, to_email=to_email, content=content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            print(response.body)
            print(response.headers)



            print ('-----------------------')
            return Response(postserializer.data)

        return Response(serializer.data)


