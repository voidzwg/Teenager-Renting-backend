from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Orders
from com.funcs import *


# Create your views here.
@csrf_exempt
def create_contract(request):
    if request.method == 'GET':
        orders_list = Orders.objects.filter()
        return contract_serialize(orders_list)
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

