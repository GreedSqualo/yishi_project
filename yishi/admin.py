from django.contrib import admin
from yishi.models import Products, commentP, star_rating

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Pname',)}

admin.site.register(Products, ProductAdmin)
admin.site.register(commentP)
admin.site.register(star_rating)