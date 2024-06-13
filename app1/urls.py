from django.urls import path
from .views import *


urlpatterns = [
    path('', index,name='index'),
    path('default/', Default,name='Default'),
    path('first/', first,name='first'),
    path('table/', table,name='table'),
    path('category/', CategoryTable,name='category'),
    path('form/', form,name='form'),
    path('Cform/', Cform,name='Cform'),
    path('update/', update,name='update'),
    path('product/', allproduct,name='allproduct'),
    path('register/', register,name='register'), 
    path('login/', Login,name='Login'), 
    path('logout/', logout,name='logout'), 
    path('catproduct/<int:id>', catproduct,name='catproduct'), 
    path('proDetails/<int:id>', proDetails,name='proDetails'), 
    path('profile/', profile,name='profile'), 
]
