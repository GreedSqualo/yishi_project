from django.db.models.fields import NullBooleanField
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from yishi.forms import ProductsForm
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

def add_product(request):
    form = ProductsForm()

    if request.method == 'POST':
        product_form = ProductsForm(request.POST)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            if 'file' in request.FILES:
                product.Photo = request.FILES.get('file')
            product.save()
            return redirect('/yishi/add_product/')
        else:
            print(product_form.errors)
    
    return render(request, 'yishi/add_product.html', {'form': form})