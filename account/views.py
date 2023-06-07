from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
def user_log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password= password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            print('user not found')   
   
    return render(request,'./auth/Login.html',{ })

