from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def events(request):
    return HttpResponse('<section><h1>Upcoming Events</h1><li>Seminar</li></section>')