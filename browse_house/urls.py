from .views import *
from django.urls import path
from haystack.views import SearchView
urlpatterns = [
    path('get_house/',get_house),
    path('get_user/',get_user),
    path('search/',search)
]