from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def restaurant(request):
    return HttpResponse('What would you like to eat from our Menu?')

def sport(request):
    return HttpResponse('Which sport would you like to see?')