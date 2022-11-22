from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def app(request):
    return render(request, 'app.html')

def videos(request):
    return render(request, 'videos.html')

def readme(request):
    return render(request, 'readme.html')
