from django.db import models
from django.db.models.fields import EmailField
from django.db.models.fields.files import ImageField
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.

class Products(models.Model):
    Pname = models.CharField(max_length=512, primary_key=True, unique=True)
    price = models.FloatField(max_length=256)
    brand = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)    
    date = models.DateTimeField(auto_now=True)
    Photo = models.ImageField(upload_to='images', default='NoImage.jpg')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('yishi:detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.Pname)
        super(Products, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Products'

class star_rating(models.Model):
    star_rating = models.FloatField(max_length=128, default=0.0)
    Pname = models.ForeignKey(Products, on_delete=models.CASCADE)
    country = models.CharField(max_length=128)
    n = models.IntegerField(default=0)

class commentP(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    star_rating = models.FloatField(max_length=128)
    content = models.TextField(max_length=512)
    country = models.CharField(max_length=128)
    Pname = models.ForeignKey(Products, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'commentPs'

class UserProfile(models.Model):
    GENDER_OF_USER = (
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
        ('OTHER', 'Other'),
        ('SECRETE','Secrete'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', default='NoImage.jpg')
    dob = models.DateField(blank=True)
    gender = models.CharField(max_length=128, choices=GENDER_OF_USER, default='SECRETE')
    nationality = models.CharField(max_length=128)

    def __str__(self):
        return self.user.username
