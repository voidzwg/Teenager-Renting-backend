from .views import *
from django.urls import path

urlpatterns = [
    path('get_cart/', get_cart),
    path('get_user/', get_user),
    path('get_house/', get_house),
]