from django.db import models

# Create your models here.

class ProductsMini(models.Model):
    title = models.TextField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title




