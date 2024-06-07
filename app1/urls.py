from django.urls import path
from .views import *


urlpatterns = [
    path('', Default,name='Default'),
    path('first/', first,name='first'),
    path('table/', table,name='table'),
    path('category/', CategoryTable,name='category'),
    path('form/', form,name='form'),
    path('Cform/', Cform,name='Cform'),
    path('update/', update,name='update'),
    path('index/', index,name='index'),
    path('product/', allproduct,name='allproduct'),
    path('register/', register,name='register'), 
    path('login/', Login,name='Login'), 
]
