from .views import *
from django.urls import path

urlpatterns = [
    path('get_user/', get_user),
    path('get_house/', get_house),
    path('get_data/', get_data)
]
