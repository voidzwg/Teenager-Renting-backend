from .views import *
from django.urls import path

urlpatterns = [
    # 管理员房源管理页面
    path('get_ticket_info/', get_ticket_info, name='get_ticket_info'),
    path('create_ticket/', create_ticket, name='create_ticket'),
    path('get_complaints/', get_complaints, name='get_complaints'),
    path('reply_complaint/', reply_complaint, name='reply_complaint'),
    path('check_ticket/', check_ticket, name='check_ticket')
]