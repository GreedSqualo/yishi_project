from django import forms
from django.db.models import fields
from yishi.models import Products, commentP, star_rating

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('Pname', 'price', 'brand', 'description', 'Photo',)

class star_ratingForm(forms.ModelForm):
    country = forms.CharField(max_length=128)

    class Meta:
        model = star_rating
        fields = ('star_rating', 'country')
    

class commentPForm(forms.ModelForm):
    country = forms.CharField(max_length=128)

    class Meta:
        model = commentP
        fields = ('star_rating', 'country', )