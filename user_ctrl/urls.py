from .views import *
from django.urls import path

urlpatterns = [
    path('update_info/', update_info, name='update_info'),
    path('get_users_info/', get_users_info, name='get_users_info'),
    path('del_user/', del_user, name='del_user'),
    path('get_workers_info/', get_workers_info, name='get_workers_info'),
    path('add_worker/', add_worker, name='add_worker'),
    path('del_worker/', del_worker, name='del_worker')
]