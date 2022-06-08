from .views import *
from django.urls import path

urlpatterns = [
    path('get_worker_info/', get_worker_info, name='get_worker_info'),
    path('select_tickets/', select_tickets, name='select_tickets'),
    path('submit_materials/', submit_materials, name='submit_materials')
]