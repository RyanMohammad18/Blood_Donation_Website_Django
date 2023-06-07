from datetime import date
from distutils.command import upload
from tokenize import blank_re
from django.db import models
from matplotlib.pyplot import clabel

import datetime
import os

class Myskill(models.Model):
    image = models.ImageField(upload_to='skillimage')
    title = models.CharField(max_length=50,blank=False)
    desc = models.TextField(max_length=500,blank=True)
    descc=models.TextField(max_length=500,blank=True)
    datetime= models.DateTimeField(auto_now_add=True)


    def summary(self):
        return self.desc[0:100]

    def ssummary(self):
        return self.descc

    def __str__(self) :
        return self.title

class Contactinfo(models.Model):
    cname = models.CharField(max_length=50)
    cemail = models.EmailField(max_length=50)
    cquery = models.TextField(max_length=200)

    def __str__(self):
        return self.cname

class Blog(models.Model):
     image = models.ImageField(upload_to='skillimage/')
     title = models.CharField(max_length=50,blank=False)
     desc = models.TextField(max_length=500,blank=True)
     datetime= models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return self.title

class UserRegister(models.Model):
    UserName = models.TextField(max_length=50)
    UserEmail = models.EmailField(max_length=150)
    UserPassword = models.TextField(max_length=150)
    UserConPassword = models.TextField(max_length=150)
    class Meta:
        db_table="skill_userregister";


def filepath(request,filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s",(timeNow,old_filename)
    return os.path.join(request, filename)


class Addvolunteers(models.Model):
    Name = models.CharField(max_length=50,blank=False)
    Address= models.TextField(max_length=50)
    BloodGroup= models.TextField(max_length=50)
    Email= models.TextField(max_length=50)
    #image = models.ImageField(upload_to=filepath, blank=True, null=True)
    image = models.ImageField(upload_to='skillimage', blank=True, null=True)
    
    


class MyVolunteerSearch(models.Model):

    image = models.ImageField(upload_to='skillimage',blank=True,null=True)
    Name = models.CharField(max_length=50,blank=False)
    BloodGroup = models.TextField(max_length=500,blank=True)
    Address=models.TextField(max_length=500,blank=True)
    email=models.EmailField(max_length=500,blank=True)
    datetime= models.DateTimeField(auto_now_add=True)

 

    def summary(self):
        return self.Address[0:100]

    