from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class Products(models.Model):
    Pname = models.CharField(max_length=512, primary_key=True, unique=True)
    price = models.FloatField(max_length=256)
    brand = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)    
    date = models.DateTimeField(auto_now=True)
    Photo = models.ImageField(upload_to='images', default='NoImage.jpg')

    class Meta:
        verbose_name_plural = 'Products'

class star_rating(models.Model):
    star_rating = models.FloatField(max_length=128, default=0.0)
    Pname = models.ForeignKey(Products, on_delete=models.CASCADE)
    country = models.CharField(max_length=128)

class commentP(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    star_rating = models.FloatField(max_length=128)
    content = models.TextField(max_length=512)
    country = models.CharField(max_length=128)
    Pname = models.ForeignKey(Products, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'commentPs'
