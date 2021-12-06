from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify, title
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
        if self.price < 0:
            self.price = 0.01
        super(Products, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Products'

class star_rating(models.Model):
    star_rating = models.FloatField(max_length=128, default=0.0)
    Pname = models.ForeignKey(Products, on_delete=models.CASCADE)
    country = models.CharField(max_length=128)
    n = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.n < 0 :
            self.n = 1
        if self.star_rating < 0 :
            self.star_rating = 0.01
        super(star_rating, self).save(*args, **kwargs)

class commentP(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    star_rating = models.FloatField(max_length=128)
    content = models.TextField(max_length=512)
    country = models.CharField(max_length=128)
    Pname = models.ForeignKey(Products, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.star_rating < 0 :
            self.star_rating = 0.01
        super(commentP, self).save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        if self.dob > timezone.now() :
            self.dob = timezone.now()
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

class Advice(models.Model):
    STATE_OF_ADVICE = (
        ('ACTIVE', 'active'),
        ('DEALED', 'dealed'),
        ('UNACCEPTED', 'unaccepted')
    )
    title = models.CharField(max_length=128, blank=False)
    content = models.TextField(max_length=1024, blank=False)
    state = models.CharField(max_length=128, choices=STATE_OF_ADVICE, default='ACTIVE')

class BuyInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    supermarket = models.CharField(max_length=128, blank=True)
    position = models.CharField(max_length=128, blank=True)
    time = models.DateField(blank=True)
    postcode = models.CharField(max_length=128, blank=True)
    describsion = models.TextField(max_length=512, blank=False)

    def get_absolute_url(self):
        return reverse('yishi:detailBI', args=[self.id])

class commentB(models.Model):
    Bid = models.ForeignKey('BuyInfo', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=512)

    class Meta:
        verbose_name_plural = 'commentBs'
