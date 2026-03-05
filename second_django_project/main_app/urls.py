from django.urls import path

from . import views

urlpatterns = [
    path('restaurant/', views.restaurant , name='restaurant'),
     path('sport-channel/', views.sport, name='sport-channel')
]