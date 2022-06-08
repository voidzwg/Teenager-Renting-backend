from .views import *
from django.urls import path

urlpatterns = [
    path('get_house_info/', get_house_info, name='get_house_info'),
    path('rent_house/', rent_house, name='rent_house'),
    path('add_house/', add_house, name='add_house'),
    path('stop_renting/', stop_renting, name='stop_renting'),
    path('del_house/', del_house, name='del_house')
]