from django.db import models

# Create your models here.
class MainSlider(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='media', blank=True)
    baner = models.CharField(max_length=50)

    def __str__(self):
        return self.text


class MiniSliderOfferIndividual(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title


class MiniSliderOfferRepair(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title


class MiniSliderOfferEngraving(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title


