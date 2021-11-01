from django.contrib import admin
from yishi.models import Products, commentP, star_rating, UserProfile, Advice

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Pname',)}

admin.site.register(Products, ProductAdmin)
admin.site.register(commentP)
admin.site.register(star_rating)
admin.site.register(UserProfile)
admin.site.register(Advice)