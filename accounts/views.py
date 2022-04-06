from django.shortcuts import redirect, render
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from .forms import *
from .decorators import *

# Create your views here.


def uregister(req):
    form = CustomerForm()
    
    if req.method == 'POST':
        form = CustomerForm(req.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data.get('first_name')
            
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            
            messages.success(req,'Account Created!')
            return redirect('user-login')
            
    context = {'form':form}
    return render(req,'customer/register.html',context)

def ulogin(req):
    
    if req.method == 'POST':
        
        contact =  req.POST.get('contact')
        password = req.POST.get('password')  
        
        user = authenticate(req, username=contact,password = password)
        
        if user is not None:
            login(req, user)
            return redirect('customer_products')
        else:
            messages.info(req, 'Mobile Number or Password is incorrect..')
     
    context = {}  
    return render(req,'customer/login.html',context)

@unauthenticated_user
def bregister(req):
    form = BusinessForm()
    
    if req.method == 'POST':
        form = BusinessForm(req.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data.get('first_name')
            
            group = Group.objects.get(name='business')
            user.groups.add(group)
            
            messages.success(req,'Business Account Created!')
            return redirect('business-login')
            
    context = {'form':form}
    return render(req,'accounts/register.html',context)



@unauthenticated_user
def blogin(req):
    
    if req.method == 'POST':
        context = {}  
        contact =  req.POST.get('contact')
        password = req.POST.get('password')  
        
        user = authenticate(req, username=contact,password = password)
        
        if user is not None:
            login(req, user)
            return redirect('products')
        else:
            messages.info(req, 'Mobile Number or Password is incorrect..')
     
    context = {}  
    return render(req,'accounts/login.html',context)
 
def userlogout(req):
    logout(req)
    return redirect('home')