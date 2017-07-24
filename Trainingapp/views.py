from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .forms import registrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction



def home(request):
    return render(request,'app1/home.html')

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = registrationForm(request.POST)
        print form
        if form.is_valid():
            user = form.save()
            # user.refresh_from_db()
            username = form.cleaned_data.get('username')
            # user.profile.bith_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return render(request,'app1/home.html',{'user':user})
    else:
        form = registrationForm()
    return render(request,'app1/registration.html',{'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render(request, 'app1/home.html', {'user': user})
            else:
                return render(request, 'app1/login.html', {'error_message': 'user is disabled/not active'})
        else:
            return render(request, 'app1/login.html', {'error_message': 'Invalid login'})
    return render(request, 'app1/login.html')


def logout(request):
    logout(request)
    form = registrationForm(request.POST or None)
    return render(request, 'app1/login.html',{'form':form})



# Create your views here.
