from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
import requests
from django.template.response import TemplateResponse
from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Item)
admin.site.register(Categorylist)

base_url = 'auction'

def template(request):
    
    category_list =  Categorylist.objects.all()
    
    return TemplateResponse(request, 'auctions/template.html', {
        'category_list': category_list,
    })

def index(request):
    
    """response = requests.get('https://fakestoreapi.com/products')
    for i in range(5, 8):
        
        title = response.json()[i]['title']
        starting_bid = response.json()[i]['price']
        category_name = response.json()[i]['category']
        description = response.json()[i]['description']
        image = response.json()[i]['image']
        
        category = Categorylist.objects.get(name=category_name)
        
        users = User.objects.all()
        for user in users :
            if user.is_authenticated:
                user = request.user
        
        items = Item.objects.get_or_create(user=user, title=title, starting_bid=starting_bid, category=category, description=description, image=image)"""
        

    
        
    items = Item.objects.all()
    category_list =  Categorylist.objects.all()
    
    return render(request, f'{base_url}/index.html', {
        'items': items,
        'category_list': category_list,
    })

def login_page(request):
    category_list =  Categorylist.objects.all()
    
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        
        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
            
        else:
            return render(request, f'{base_url}/login.html', {
                'category_list': category_list,
            })
        
    else:
        return render(request, f'{base_url}/login.html', {
            'category_list': category_list,
        })

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def signup_view(request):
    
    category_list =  Categorylist.objects.all()
    
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
        return render(request, f'{base_url}/signup.html',{
            'category_list': category_list,
        })
    
def post_item(request):
    if request.method == 'POST':
        title = request.POST['Title']
        starting_bid = request.POST['Starting-Bid']
        category_name = request.POST['Category']
        description = request.POST['Description']
        image = request.POST['Image-URL']
        
        category = Categorylist.objects.get(name=category_name)
        
        users = User.objects.all()
        for user in users :
            if user.is_authenticated:
                user = request.user
    
        items = Item.objects.create(user=user, title=title, starting_bid=starting_bid, category=category, description=description, image=image)
        
        return HttpResponseRedirect(reverse("index"))
        
    elif request.method == 'GET':
        
        category_list = Categorylist.objects.all()
        
        return render(request, f'{base_url}/post-item.html', {
            'category_list': category_list,
        })

def about_page(request):
    
    category_list =  Categorylist.objects.all()
    
    return render(request, f'{base_url}/about.html',{
        'category_list': category_list,
    })
