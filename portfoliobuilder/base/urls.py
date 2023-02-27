from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create_portfolio, name='create'),
    path('display/', views.display_portfolio, name='display'),
]
