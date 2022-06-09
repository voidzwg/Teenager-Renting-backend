from .views import *
from django.urls import path

urlpatterns = [
    path('get_tickets/', get_tickets, name='get_tickets'),
    path('get_checked_tickets/', get_checked_tickets, name='get_checked_tickets'),
    path('get_finished_tickets/', get_finished_tickets, name='get_finished_tickets'),
    path('get_processing_tickets/', get_processing_tickets, name='get_processing_tickets'),
    path('get_pending_tickets/', get_pending_tickets, name='get_pending_tickets'),
    path('submit_ticket/', submit_ticket, name='submit_ticket'),
    path('comment/', comment, name='comment')
]