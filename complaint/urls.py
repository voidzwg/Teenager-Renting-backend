from .views import *
from django.urls import path

urlpatterns = [
    path('get_complaints/', get_complaints, name='get_complaints'),
    path('get_replied_complaints/', get_replied_complaints, name='get_replied_complaints'),
    path('get_ignored_complaints/', get_ignored_complaints, name='get_ignored_complaints'),
    path('submit_complaint/', submit_complaint, name='submit_complaint')
]