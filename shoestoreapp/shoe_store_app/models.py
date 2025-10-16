from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Accessory(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accessory_detail', kwargs={'pk': self.id})

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    price =models.IntegerField()
    size = models.IntegerField()
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    accessory = models.ManyToManyField(Accessory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shoe_detail', kwargs={'shoe_id': self.id})