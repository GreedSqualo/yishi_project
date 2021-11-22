from django import forms
from django.db.models import fields
from yishi.models import Products, UserProfile, commentP, star_rating, Advice, BuyInfo, commentB
from django.contrib.auth.models import User

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
        fields = ('star_rating', 'country', 'content')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('dob', 'picture', 'gender', 'nationality',)

class AdviceForm(forms.ModelForm):
    class Meta:
        model = Advice
        fields = ('title', 'content', 'state',)

class BuyInfoForm(forms.ModelForm):
    class Meta:
        model = BuyInfo
        fields = ('supermarket', 'position', 'postcode', 'time', 'describsion',)

class commentBForm(forms.ModelForm):
    class Meta:
        model = commentB
        fields = ('content', )