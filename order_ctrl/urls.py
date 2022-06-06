from .views import *
from django.urls import path

urlpatterns = [
    # 管理员订单管理页面
    path('get_order_info/', get_order_info, name='get_order_info'),
    path('check_order/', check_order, name='check_order'),
    path('del_order/', del_order, name='del_order')
]