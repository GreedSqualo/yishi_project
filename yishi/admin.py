from django.contrib import admin
from yishi.models import Products, commentP, star_rating

# Register your models here.

admin.site.register(Products)
admin.site.register(commentP)
admin.site.register(star_rating)