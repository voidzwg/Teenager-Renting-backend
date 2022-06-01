from .views import *
from django.urls import path

urlpatterns = [
    path('',init),
    path('submit/',submit),
    path('delete/',delete)
]