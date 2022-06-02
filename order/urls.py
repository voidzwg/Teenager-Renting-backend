from .views import *
from django.urls import path

urlpatterns = [
    path('',init),
    path('pay/',pay),
    path('delete/',delete)
]