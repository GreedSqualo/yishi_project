from django.urls import path
from yishi import views

app_name = 'yishi'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('result/', views.result, name='result'),
    path('detail/', views.detail, name='detail'),
]
