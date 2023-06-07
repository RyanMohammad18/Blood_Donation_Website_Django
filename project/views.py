

from django.shortcuts import render


from django import views

def homepage(request):
    return render(request,'home.html',{})
