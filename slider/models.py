from django.db import models

# Create your models here.
class MainSlider(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='media', blank=True)
    baner = models.CharField(max_length=50)

    def __str__(self):
        return self.text


