from django.urls import path
from yishi import views

app_name = 'yishi'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('result/', views.result, name='result'),
    path('detail/<slug:Pname_slug>', views.detail, name='detail'),
    path('add_product/', views.add_product, name='add_product')
]
