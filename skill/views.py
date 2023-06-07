from dataclasses import dataclass
import email
from msilib.schema import ListView
from pyexpat.errors import messages
from re import template
from tokenize import Name
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import views
from matplotlib.pyplot import title
from matplotlib.style import context
from skill.models import UserRegister
from django.contrib import messages
from .decorators import allowed_users, unauthenticated_user


from .models import Blog, Myskill,Contactinfo,Addvolunteers,MyVolunteerSearch


def homepage(request):

    return render(request,'home.html',{})


def adminhomepage(request):

    return render(request,'adminhome.html',{})

def search(request):

    if 'q' in request.GET :
        q= request.GET['q']
        
        item = Myskill.objects.filter(title__icontains=q)
        

    else: 
        item = Myskill.objects.all()

    title='AB+'
    desc="Hello I am Karim"
    descc="This is my email"

    context = {
        'title':title,
        'description':desc,
        'descc':descc,
        'data':item,
    }
    return render(request,'search.html',context)

def aboutpage(request):
    return render(request,'about.html',{})





   


def contactpage(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        query =  request.POST.get('comments')
        
        mydata = Contactinfo(cname=name, cemail=email,cquery=query)
        mydata.save()

    return render(request,'contact.html',{})


def create_blood_group(request):

    

    if request.method == 'POST':
        image = request.FILES['image']
        title = request.POST.get('title')
        desc =  request.POST.get('desc')
        descc= request.POST.get('descc')
        
        create_blood= Myskill(image=image, title=title,desc=desc,descc=descc)
        create_blood.save()
        messages.success(request,"Information Added Successfully")

    return render(request,'create_blood_group.html',{})


def userregistration(request):
    if request.method == 'POST':
        if request.POST.get('UserName') and request.POST.get('UserEmail') and request.POST.get('UserPassword') and request.POST.get('UserConPassword'):
            saverecord=UserRegister()
            saverecord.UserName=request.POST.get('UserName')
            saverecord.UserEmail=request.POST.get('UserEmail')
            saverecord.UserPassword=request.POST.get('UserPassword')
            saverecord.UserConPassword=request.POST.get('UserConPassword')
            saverecord.save()
            
            return redirect('userlogin')
            
         
        return render(request,'login.html')

        

    else: 
         return render(request,'SignUp.html')


def userlogin(request):
    if request.method=="POST":
       try:
            userdetails=UserRegister.objects.get(UserName=request.POST['UserName'],UserPassword=request.POST['UserPassword'])
            print("username=",userdetails)
            return render(request, 'home.html',{})
            

       except UserRegister.DoesNotExist as e:
            
            return HttpResponse("username/pass invalid")
   
    return render(request,'login.html',{})    
   
def addvolunteerpage(request):

    if request.method == "POST":
        Prod = Addvolunteers()
        Prod.Name = request.POST.get('Name',Name)
        Prod.Address = request.POST.get('Address')
        Prod.Email = request.POST.get('Email')
        Prod.BloodGroup = request.POST.get('BloodGroup')
        Prod.image= request.FILES['image']

   
        Prod.save()
        messages.success(request,"Volunteers information Added Successfully")
        return redirect('Volunteerslist')
    return render(request,'addvolunteer.html')

def useraddvolunteerpage(request):

    if request.method == "POST":
        Prod = Addvolunteers()
        Prod.Name = request.POST.get('Name',Name)
        Prod.Address = request.POST.get('Address')
        Prod.Email = request.POST.get('Email')
        Prod.BloodGroup = request.POST.get('BloodGroup')
        Prod.image= request.FILES['image']

   
        Prod.save()
        messages.success(request,"Volunteers information Added Successfully")
        return redirect('UserVolunteerlist')
    return render(request,'addvolunteer.html')


def Volunteerslist(request):
    Prods = Addvolunteers.objects.all()
    Context= {'Prods':Prods}
    return render(request,'volunteerslist.html',Context)

def EditVolunteerslist(request,pk):
    prod = Addvolunteers.objects.get(id=pk)

    if request.method == "POST":
        prod.Name= request.POST.get('Name')
        prod.Address= request.POST.get('Address')
        prod.BloodGroup= request.POST.get('BloodGroup')
        prod.Email= request.POST.get('Email')
        prod.image = request.FILES['image']
        prod.save()
        messages.success(request,"Donors information Updated Successfully")
        
        return redirect('Volunteerslist')
    context = {'prod':prod}
    return render(request,'EditVolunteerslist.html',context)

def DeleteVolunteerslist(request,pk):
    prod = Addvolunteers.objects.filter(id=pk)
    prod.delete()
    messages.success(request,"Information Deleted Successfully")
    return redirect('Volunteerslist')

def DeleteBloodlist(request,pk):
    prod = Myskill.objects.filter(id=pk)
    prod.delete()
    messages.success(request,"Information Deleted Successfully")
    return redirect('search')

def allblogpage(request):
    return render(request,'allblogpage.html')

def singleblogpage(request):
    return render(request,'singleblogpage.html')


def singleblogpage2(request):
    return render(request,'singleblogpage2.html')

def singleblogpage3(request):
    return render(request,'singleblogpage3.html')

def volunteersearch(request):

    if 'q' in request.GET :
        q= request.GET['q']
        
        items = MyVolunteerSearch.objects.filter(Address__icontains=q)
        

    else: 
        items = MyVolunteerSearch.objects.all()

    Name='Karim'
    Address='Banasree'
    Email="This is my email"
    BloodGroup="AB+"
    
    

    context = {
        'Name':Name,
        'Address':Address,
        'BloodGroup':BloodGroup,
        
        'Email':Email,
        'data':items,
    }
    return render(request,'volunteerslist.html',context)


def EditBloodbank(request,pk):
    prod = Myskill.objects.get(id=pk)

    if request.method == "POST":
        prod.title= request.POST.get('title')
        prod.desc= request.POST.get('desc')
        prod.descc= request.POST.get('descc')
        #prod.datetime= request.POST.get('datetime')
        prod.image = request.FILES['image']
        prod.save()

        messages.success(request,"Donors information Updated Successfully")

        return redirect("search")

    context = {'prod':prod}
    return render(request,'EditBloodbank.html',context)

def adminlogin(request):
    if request.method=="POST":
            from django.contrib import auth
           
            username1 = request.POST.get('username', False)
            password1 = request.POST.get('password')
            x=auth.authenticate(username=username1,password=password1)
            if x is None:
                return HttpResponse('username/password is invalid')
            else:
                #return render(request,'adminhome.html',{})
                return redirect('adminhomepage')

    return render(request, 'adminlogin.html')

def UserVolunteerlist(request):
     Prods = Addvolunteers.objects.all()
     Context= {'Prods':Prods}
     return render(request,'UserVolunteerlist.html',Context)

def useraddvolunteer(request):
     if request.method == "POST":
        Prod = Addvolunteers()
        Prod.Name = request.POST.get('Name',Name)
        Prod.Address = request.POST.get('Address')
        Prod.Email = request.POST.get('Email')
        Prod.BloodGroup = request.POST.get('BloodGroup')
        Prod.image= request.FILES['image']

   
        Prod.save()
        messages.success(request,"Volunteers information Added Successfully")
        return redirect('UserVolunteerlist')
     return render(request,'useraddvolunteer.html')

def usersearch(request):

     if 'q' in request.GET :
        q= request.GET['q']
        
        item = Myskill.objects.filter(title__icontains=q)
        

     else: 
        item = Myskill.objects.all()

     title='AB+'
     desc="Hello I am Karim"
     descc="This is my email"

     context = {
        'title':title,
        'description':desc,
        'descc':descc,
        'data':item,
    }
     return render(request,'usersearch.html',context)

def user_create_blood_group(request):
     if request.method == 'POST':
        image = request.FILES['image']
        title = request.POST.get('title')
        desc =  request.POST.get('desc')
        descc= request.POST.get('descc')
        
        create_blood= Myskill(image=image, title=title,desc=desc,descc=descc)
        create_blood.save()
        messages.success(request,"Information Added Successfully")

     return render(request,'user_create_blood_group.html',{})
