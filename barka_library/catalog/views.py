from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def books(request):
    return HttpResponse('<ul><li>The House in the Cerulean Sea</li><li>Project Hail Mary</li><li>A Man Called Ove</li><li>The Shadow of the Wind</li><li>The Seven Husbands of Evelyn Hugo</li></ul>')

def special(request):
    return HttpResponse('<div><li>The Midnight Libary</li><li>The Invisible Life of Addie LaRue</li></div>')