from django.db import models

# Create your models here.

class ProductsMini(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True)

    class Meta:
        verbose_name = 'Galeria produktów - Strona Główna'
        verbose_name_plural = 'Galeria produktów - Strona Główna'

    def __str__(self):
        return self.title

class MainProducts(models.Model):
    title = models.CharField(max_length=50, blank=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title

class ProductsCategory(models.Model):
    title = models.CharField(max_length=50, default='title')
    category = models.ManyToManyField(MainProducts, related_name='category', default='', null=True, blank=True)

    def __str__(self):
        return self.title


