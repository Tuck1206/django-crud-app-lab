from django.db import models
from django.urls import reverse
# Create your models here.

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    price =models.IntegerField()
    size = models.IntegerField()
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shoe_detail', kwargs={'shoe_id': self.id})

class Accessories(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shoe_detail', kwargs={'pk': self.id})