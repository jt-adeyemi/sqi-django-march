from django.urls import path

from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('special/', views.special, name='featured_books'),
]