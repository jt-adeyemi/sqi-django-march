from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def learn(request):
    return HttpResponse('Ready to learn? Click Here')

def create(request):
    return HttpResponse('Become a creator today')