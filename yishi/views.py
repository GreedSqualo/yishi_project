from django.db.models.fields import NullBooleanField
from django.shortcuts import render
from django.http import HttpResponse
from yishi.models import Products,commentP,star_rating

def index(request):
    return render(request, 'yishi/index.html')

def about(request):
    return render(request, 'yishi/about.html')

def result(request):
    product_list = Products.objects.all()
    context_dict = {}
    context_dict['Products'] = product_list
    return render(request, 'yishi/result.html', context_dict)

def detail(request):
    return render(request, 'yishi/detail.html')