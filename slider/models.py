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
        verbose_name = 'Strona Główna - Slajder: Na zamówienie'
        verbose_name_plural = 'Strona Główna - Slajder: Na zamówienie'


class MiniSliderOfferRepair(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Strona Główna - Slajder: Naprawa'
        verbose_name_plural = 'Strona Główna - Slajder: Naprawa'


class MiniSliderOfferEngraving(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Strona Główna - Slajder: Grawerowanie'
        verbose_name_plural = 'Strona Główna - Slajder: Grawerowanie'


class AboutInformations(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField('contents')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Podstrona O firmie'
        verbose_name_plural = 'Podstrona O firmie'




