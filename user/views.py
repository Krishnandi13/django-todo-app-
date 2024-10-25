from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def add_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        if username!='' and email!='' and password!='':
            user=User(
                username=username,
                email=email,
                password=password
            )
            user.save()
            return redirect('home')
        else:
          return render(request,'add_user.html')
    return render(request,'add_user.html')


def login_user(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
        # Return an 'invalid login' error message.
           
            return redirect('login_user')
    
    else:
        return render(request,'login_user.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')    