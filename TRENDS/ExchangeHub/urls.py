from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

urlpatterns = [
    path('', views.home, name='home'),
    path('ExchangeHub/', views.ExchangeHub, name='ExchangeHub'),
    path('login/', views.ExchangeHub, name='login'),  # Optional if you're not using a custom view
    path('loading/', views.loading, name='loading'),
    path('home/', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),
    path('contacts/', views.contacts, name='contacts'),
    path('sell/', views.sell, name='sell'),
    path('settings/', views.settings, name='settings'),
    path('moreinfo/', views.moreinfo, name='moreinfo'),
]

