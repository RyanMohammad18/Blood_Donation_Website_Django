
from django.urls import path
from .views import user_log
from unicodedata import name



urlpatterns = [
    path('',user_log,name='login')
  

]


  
    
