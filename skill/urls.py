from unicodedata import name
from django.urls import path
from django import views


urlpatterns = [
   path('',views.homepage,name='homepage'),
   path('about/',views.aboutpage,name='aboutpage'),
   path('login/',views.loginpage,name='loginpage'),
   path('contact/',views.contactpage,name='contactpage'),
   
   
]