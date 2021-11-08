from django.urls import path
from yishi import views

app_name = 'yishi'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('result/', views.result, name='result'),
    path('detail/<slug:Pname_slug>/', views.detail, name='detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('post_commentP/<slug:Pname_slug>/', views.post_commentP, name='post_commentP'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('advice/', views.advice, name='advice'),
    path('profile/', views.profile, name='profile'),
    path('buyTogether/', views.buyTogether, name='buyTogether'),
]
