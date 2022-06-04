from .views import *
from django.urls import path

urlpatterns = [
    path('',init),
    path('get_paid/',get_paid),
    path('get_unpaid',get_unpaid),
    path('pay/',pay),
    path('cancel/',cancel),
    path('delete/',delete),
]