
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from unicodedata import name
from skill import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'),
    path('home/',views.homepage,name='homepage'),
    path('adminhome/',views.adminhomepage,name='adminhomepage'),
    path('about/',views.aboutpage,name='aboutpage'),
    path('search/',views.search,name='search'),
    path('usersearch/',views.usersearch,name='usersearch'),
    path('DeleteBloodlist/<str:pk>',views.DeleteBloodlist,name='DeleteBloodlist'),
    path('signup/',views.userregistration,name='userregistrationpage'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('login/',views.userlogin,name='userlogin'),
    path('contact/',views.contactpage,name='contactpage'),
    ##path('login/',include('account.urls')),
    path('addvolunteer/',views.addvolunteerpage,name='addvolunteerpage'),
    path('volunteerslist/',views.Volunteerslist,name='Volunteerslist'),
    path('UserVolunteerlist/',views.UserVolunteerlist,name='UserVolunteerlist'),
    path('useraddvolunteer/',views.useraddvolunteer,name='useraddvolunteer'),
    path('EditVolunteerslist/<str:pk>',views.EditVolunteerslist,name='EditVolunteerslist'),
    path('DeleteVolunteerslist/<str:pk>',views.DeleteVolunteerslist,name='DeleteVolunteerslist'),
    path('create_blood_group',views.create_blood_group,name='create_blood_group'),
    path('user_create_blood_group',views.user_create_blood_group,name='user_create_blood_group'),
    path('allblogpage',views.allblogpage,name='allblogpage'),
    path('singleblogpage',views.singleblogpage,name='singleblogpage'),
    path('singleblogpage2',views.singleblogpage2,name='singleblogpage2'),
    path('singleblogpage3',views.singleblogpage3,name='singleblogpage3'),
    path('EditBloodbank/<str:pk>',views.EditBloodbank,name='EditBloodbank'),
  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

