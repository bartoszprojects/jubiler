from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class ProductsMini(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True)

    class Meta:
        verbose_name = 'Galeria produktów - Strona Główna'
        verbose_name_plural = 'Galeria produktów - Strona Główna'

    def __str__(self):
        return self.title


class ProductsCategory(models.Model):
    title = models.CharField(max_length=50, default='title')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kategorie produktów'
        verbose_name_plural = 'Kategorie produktów'


class MainProducts(models.Model):
    title = models.CharField(max_length=50, blank=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='media', blank=True)
    image_thumbnail = ImageSpecField(source='image',processors=[ResizeToFill(500,500)],format='JPEG',options={'quality':60})
    category = models.ManyToManyField(ProductsCategory, related_name='category', default='', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Produkty'
        verbose_name_plural = 'Produkty'