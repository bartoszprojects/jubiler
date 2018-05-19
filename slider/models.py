from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class MainSlider(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='media', blank=True)
    baner = models.CharField(max_length=50)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Strona Główna - Zdjęcie Główne'
        verbose_name_plural = 'Strona Główna - Zdjęcie Główne'


class MiniSliderOfferIndividual(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Strona Główna - Slajder: Biżuteria na zamówienie'
        verbose_name_plural = 'Strona Główna - Slajder: Biżuteria na zamówienie'


class MiniSliderOfferRepair(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Strona Główna - Slajder: Naprawa biżuterii'
        verbose_name_plural = 'Strona Główna - Slajder: Naprawa biżuterii'



class MiniSliderOfferEngraving(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Strona Główna - Slajder: Obróbka i grawerowanie'
        verbose_name_plural = 'Strona Główna - Slajder: Obróbka i grawerowanie'


class AboutInformations(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField('contents')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Podstrona: O firmie'
        verbose_name_plural = 'Podstrona: O firmie'



class Service(models.Model):
    title = models.CharField(max_length=100, default=0)
    content = RichTextUploadingField('contents', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Podstrona: Oferta'
        verbose_name_plural = 'Podstrona: Oferta'

class ServiceImages(models.Model):
    image = models.ImageField(upload_to='media', blank=True)
    title = models.CharField(max_length=25, default=0)
    service = models.ForeignKey(Service, related_name='service_images', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Podstrona: Oferta - dodawanie zdjęć'
        verbose_name_plural = 'Podstrona: Oferta - dodawanie zdjęć'

