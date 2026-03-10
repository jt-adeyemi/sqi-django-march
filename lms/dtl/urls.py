from django.urls import path

from . import views

urlpatterns = [
    path('', views.dtl_syntax_demo, name='dtl'),
    path('tech-world/', views.shopping_cart, name='shopping_cart'),
]