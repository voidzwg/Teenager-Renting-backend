from .views import *
from django.urls import path

urlpatterns = [
    path('get_house/',get_house),
    path('get_user/',get_user),
    path('search/',search),
    path('add_cart/',add_cart)
]