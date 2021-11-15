from django.contrib import admin
from yishi.models import BuyInfo, Products, commentB, commentP, star_rating, UserProfile, Advice

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('Pname',)}

admin.site.register(Products, ProductAdmin)
admin.site.register(commentP)
admin.site.register(star_rating)
admin.site.register(UserProfile)
admin.site.register(Advice)
admin.site.register(BuyInfo)
admin.site.register(commentB)