from django.urls import path
from . import views


urlpatterns = [
    path('library/dashboard/', views.dashboard, name='dashboard'),
]