from django.db import models

# Create your models here.

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    price =models.IntegerField()
    size = models.IntegerField()
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    product_url = models.URLField(max_length=200)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    