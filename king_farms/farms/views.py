from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'farms/home.html')


def profile(request):
    return render(request, 'farms/profile.html')


def services(request):
    return render(request, 'farms/services.html')


def help(request):
    return render(request, 'farms/help.html')