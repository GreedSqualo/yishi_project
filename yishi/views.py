from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponse
from yishi.forms import AdviceForm, BuyInfoForm, ProductsForm, commentPForm, UserForm, UserProfileForm
from yishi.models import BuyInfo, Products, commentB,commentP,star_rating,UserProfile
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json, string

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
    context_dict['country'] = json.dumps(country1)
    return render(request, 'yishi/result.html', context_dict)

def detail(request, Pname_slug, countryS):
    context_dict = {}
    punctuation_string = string.punctuation
    for i in punctuation_string:
        countryS = countryS.replace(i, '')
    try:
        product = Products.objects.get(slug=Pname_slug)
        comment_list = commentP.objects.filter(Pname=product.Pname, country=countryS)
        star = star_rating.objects.get(Pname = product.Pname, country=countryS)
        context_dict['product'] = product
        context_dict['comments'] = comment_list
        context_dict['rate'] = star.star_rating
        context_dict['n'] = star.n
    except Products.DoesNotExist :
        context_dict['product'] = None
    except commentP.DoesNotExist :
        context_dict['comments'] = None
    except star_rating.DoesNotExist:
        context_dict['rate'] = 0.0
        context_dict['n'] = 0
    context_dict['country'] = json.dumps(countryS)
    return render(request, 'yishi/detail.html', context=context_dict)

def add_product(request):
    if request.method == 'POST':
        product_form = ProductsForm(request.POST)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            if 'file' in request.FILES:
                product.Photo = request.FILES['file']
            product.save()
            messages.success(request, 'Thank you for adding a new product !')
            return redirect('/yishi/add_product/')
        else:
            print(product_form.errors) 
    else:
        product_form = ProductsForm()
    return render(request, 'yishi/add_product.html', context = {'product_form': product_form})

def post_commentP(request, Pname_slug):
    product = get_object_or_404(Products, slug=Pname_slug)
    if request.method == 'POST':
        comment_form = commentPForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.Pname = Products.objects.get(slug=Pname_slug)
            new_comment.save()
            countryC = request.POST['country']
            rate = request.POST['star_rating']
            rate = float(rate) 
            try:
                star_ratingP = star_rating.objects.get(Pname=product, country=countryC)
                print(star_ratingP.star_rating)
                star_ratingP.star_rating = (star_ratingP.star_rating * star_ratingP.n + rate)/(star_ratingP.n + 1)
                star_ratingP.n = star_ratingP.n + 1
                star_ratingP.save()
                print(star_ratingP.star_rating)
                print(star_ratingP.n)
            except star_rating.DoesNotExist :
                star_rating.objects.create(Pname=product, country=countryC, star_rating=rate, n=1)
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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('yishi:index'))
            else:
                return HttpResponse("The username or password is wrong.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login detail supplied.")
    else:
        return render(request, 'yishi/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('yishi:index'))

def advice(request):
    adviced = False
    if request.method == 'POST':
        advice_form = AdviceForm(request.POST)

        if advice_form.is_valid():
            advice = advice_form.save()
            advice.save()
            adviced = True
        else:
            print(advice_form.errors)
    else:
        advice_form = AdviceForm()
    return render(request, 'yishi/advice.html', context={'advice_form': advice_form, 'adviced': adviced})

@login_required
def profile(request):
    context_dict = {}
    try:
        currentUser = request.user
        users = User.objects.get( username=currentUser )
        userProfile = UserProfile.objects.get(user=users)
    except User.DoesNotExist:
        return HttpResponse("User don't find.")
    except UserProfile.DoesNotExist :
        return HttpResponse("Profile don't find.")

    if request.method == 'POST':
        # user_form = UserForm(request.POST)
        # profile_form = UserProfileForm(request.POST)
        users.username = request.POST['username']
        users.email = request.POST['email']
        users.password = request.POST['password']
        users.set_password(users.password)
        users.save()
        userProfile.dob = request.POST['dob']
        userProfile.gender = request.POST['gender']
        userProfile.nationality = request.POST['nationality']
        if 'picture' in request.FILES:
            userProfile.picture = request.FILES['picture']
        userProfile.save()
        return redirect("yishi:profile")

    elif request.method == "GET":
        user_form = UserForm()
        profile_form = UserProfileForm()
        context_dict['user'] = users
        context_dict['profile_form'] = profile_form
    context_dict['user'] = users
    context_dict['userProfile'] = userProfile
    return render(request, 'yishi/profile.html', context=context_dict)

@login_required
def buyTogether(request):
    context_dict = {}
    if request.method == 'POST':
        keyword = request.POST.get('KeyWord')
        try:
            BuyInfo_list = BuyInfo.objects.filter(Q(supermarket__icontains=keyword)|Q(position__icontains=keyword)|Q(postcode__icontains=keyword))
            context_dict['BuyInfos'] = BuyInfo_list
        except BuyInfo.DoesNotExist:
            context_dict['BuyInfos'] = None
    return render(request, 'yishi/buyTogether.html', context_dict)

@login_required
def add_BuyInfo(request):
    BuyInfo_form = BuyInfoForm()
    if request.method == 'POST':
        currentUser = request.user
        users = User.objects.get( username=currentUser )
        BuyInfo_form = BuyInfoForm(request.POST)
        if BuyInfo_form.is_valid():
            buyIn = BuyInfo_form.save(commit=False)
            buyIn.user = users
            print(request.user)
            print(buyIn.user)
            buyIn.save()
            messages.success(request, 'Thank you for post you order information !')
            return redirect('/yishi/buyTogether/')
        else:
            print(BuyInfo_form.errors) 
    else:
        BuyInfo_form = BuyInfoForm()
    return render(request, 'yishi/add_BuyInfo.html', context = {'BuyInfo_form': BuyInfo_form})

@login_required
def detailBI(request, id):
    context_dict = {}
    n = 0
    currentUser = request.user
    user = User.objects.get(username=currentUser)
    tag = False
    try:
        buyInf = BuyInfo.objects.get(id=id)
        commentB_List = commentB.objects.filter(Bid = buyInf)
        context_dict['BuyInfo'] = buyInf
        context_dict['comments'] = commentB_List
        for comm in commentB_List:
            n = n + 1
            if user == comm.user:
                tag = True
        if user == buyInf.user:
            tag = True
    except commentB.DoesNotExist:
        context_dict['comments'] = None
    except BuyInfo.DoesNotExist:
        context_dict['BuyInfo'] = None
    context_dict['tag'] = tag
    context_dict['n'] = n
    return render(request, 'yishi/detailBI.html', context = context_dict)

def post_commentB(request, id):