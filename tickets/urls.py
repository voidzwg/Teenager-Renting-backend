from .views import *
from django.urls import path

urlpatterns = [
    # 我的报修页面
    path('get_tickets/', get_tickets, name='get_tickets')
]