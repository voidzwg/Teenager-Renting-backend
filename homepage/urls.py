from .views import *
from django.urls import path

urlpatterns = [
    path('', init),
    path('get_house/', get_house),
    path('get_data/', get_data)
]
