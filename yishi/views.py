from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.http import HttpResponse
from yishi.forms import ProductsForm, commentPForm, UserForm, UserProfileForm
from yishi.models import Products,commentP,star_rating,UserProfile

def index(request):
    return render(request, 'yishi/index.html')

def about(request):
    return render(request, 'yishi/about.html')

def result(request):
    if request.method == 'POST':
        country1 = request.POST.get('Country')
        keyword = request.POST.get('ProductName')
    product_list = Products.objects.filter(Pname__icontains=keyword)
    star_list = []
    for product in product_list:
        try:
            star = star_rating.objects.get(Pname = product.Pname, country=country1)
            star_list.append(star.star_rating)
        except:
            star_list.append(0.0)
    information = zip(product_list, star_list)
    context_dict = {}
    context_dict['Products'] = information
    context_dict['country'] = country1
    return render(request, 'yishi/result.html', context_dict)

def detail(request, Pname_slug):
    context_dict = {}
    try:
        product = Products.objects.get(slug=Pname_slug)
        comment_list = commentP.objects.filter(Pname=product.Pname)
        context_dict['product'] = product
        context_dict['comments'] = comment_list
    except Products.DoesNotExist :
        context_dict['product'] = None
    except commentP.DoesNotExist :
        context_dict['comments'] = None
    return render(request, 'yishi/detail.html', context=context_dict)

def add_product(request):
    form = ProductsForm()

    if request.method == 'POST':
        product_form = ProductsForm(request.POST)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            if 'file' in request.FILES:
                product.Photo = request.FILES['file']
            product.save()
            return redirect('/yishi/add_product/')
        else:
            print(product_form.errors)
    
    return render(request, 'yishi/add_product.html', {'form': form})

def post_commentP(request, Pname_slug):
    product = get_object_or_404(Products, slug=Pname_slug)
    if request.method == 'POST':
        comment_form = commentPForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.Pname = Products.objects.get(slug=Pname_slug)
            new_comment.save()
            return redirect(product)
        else:
            return HttpResponse('Form error')
    else:
        return HttpResponse('POST only')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'yishi/register.html', 
                context = {'user_form': user_form,'profile_form': profile_form,'registered': registered}
                )