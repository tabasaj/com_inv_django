from django.shortcuts import render, redirect

def home(request):
    
    return render(request, 'home.html', {'url': 'home'})

def about_us(request):
    
    return render(request, 'about_us.html', {'url': 'about_us', 'title': 'About Us'})

def programs(request):
    
    return render(request, 'programs.html', {'url': 'programs', 'title': 'Programs'})

def projects(request):
    
    return render(request, 'projects.html', {'url': 'projects', 'title': 'Projects'})

def wew(request):

    return render(request, 'asd.html')