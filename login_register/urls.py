from .views import *
from django.urls import path

urlpatterns = [
    path('', hello),
    path('login', login),
    path('register', register),
    path('user/<int:id>/',detail)
]