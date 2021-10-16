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
    if request.method == 'POST':
        country1 = request.POST.get('Country')
        keyword = request.POST.get('ProductName')
        print(country1, keyword)
    product_list = Products.objects.filter(Pname__icontains=keyword)
    star_list = []
    #for product in product_list:
        #stars = star_rating.objects.filter(Pname = product.Pname)
        #star = stars.filter(country = country1)
        #if not star :
        #    star_list.append(0.0)
        #star_list.append(star.star_rating)
    context_dict = {}
    context_dict['Products'] = product_list
    context_dict['star_ratings'] = star_list
    return render(request, 'yishi/result.html', context_dict)

def detail(request, Pname_slug):
    context_dict = {}
    try:
        product = Products.objects.get(slug=Pname_slug)
        context_dict['product'] = product
    except Products.DoesNotExist:
        context_dict['product'] = None
    return render(request, 'yishi/detail.html', context=context_dict)

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