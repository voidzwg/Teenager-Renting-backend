from .views import *
from django.urls import path

urlpatterns = [
    # 管理员房源管理页面
    path('create_contract/', create_contract, name='create_contract')
]