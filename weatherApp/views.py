from django.shortcuts import render


base_url = "weather/"

def homePage(request):

    
    
    return render(request, f"{base_url}/home.html")