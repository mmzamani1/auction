from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
import requests
from django.contrib import admin
from .models import *

admin.site.register(Item)

base_url = 'myapp'
base_url2 = 'login-form-20'

def index(request):
    """for i in range(3):
        response = requests.get('https://randomuser.me/api')
        image = response.json()['results'][0]['picture']['large']
        name = response.json()['results'][0]['name']['first']
        
        items = Item.objects.create(image=image, name=name)"""
    items = Item.objects.all()
    
    return render(request, f'{base_url}/index.html', {
        'items': items
    })

def login_page(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        
        user = authenticate(request, username=username, password=password)
        print(user)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
            
        else:
            return render(request, f'{base_url}/login.html')
        
    else:
        return render(request, f'{base_url}/login.html')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['Username']
        email = request.POST['Email']
        password = request.POST['Password']
        password2 = request.POST['Password2']
        fname = request.POST['Firstname']
        lname = request.POST['Lastname']

        if password == password2:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.first_name = fname
            user.last_name = lname
            user.save()
        else: 
            messages.error(request, 'Passwords Do Not Match')
            return HttpResponseRedirect('signup')
            
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, f'{base_url}/signup.html')
    
    else:
        return render(request, f'{base_url}/signup.html')
    
def post_item(request):
    return render(request, f'{base_url}/post-item.html')

def about_page(request):
    return render(request, f'{base_url}/about.html')

def gallery(request):
    return render(request, f'{base_url}/gallery.html')
