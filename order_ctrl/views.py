from django.views.decorators.csrf import csrf_exempt
from .models import Orders
from com.funcs import *


# Create your views here.
@csrf_exempt
def get_order_info(request):
    if request.method == 'GET':
        orders_list = Orders.objects.filter()
        return order_ctrl_serialize(orders_list)
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def approved(request):
    if request.method == 'POST':
        oid = request.POST.get('orderid')
        try:
            order = Orders.objects.get(id=oid)
        except:
            print("In order_ctrl/approved: order is not exist")
            return JsonResponse({'errno': 1002, 'msg': "订单不存在"})
        if order.status == 0:
            order.status = 1
            order.save()
            return JsonResponse({'errno': 0, 'msg': "审核成功"})
        return JsonResponse({'errno': 1003, 'msg': "订单已审核或取消"})
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def disapproved(request):
    if request.method == 'POST':
        oid = request.POST.get('orderid')
        try:
            order = Orders.objects.get(id=oid)
        except:
            print("In order_ctrl/disapproved: order is not exist")
            return JsonResponse({'errno': 1002, 'msg': "订单不存在"})
        if order.status == 0:
            order.status = 3
            order.save()
            return JsonResponse({'errno': 0, 'msg': "审核成功"})
        return JsonResponse({'errno': 1003, 'msg': "订单已审核或取消"})
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def del_order(request):
    if request.method == 'POST':
        oid = request.POST.get('orderid')
        try:
            order = Orders.objects.get(id=oid)
        except:
            print("In order_ctrl/check_order: order is not exist")
            return JsonResponse({'errno': 1002, 'msg': "订单不存在"})
        order.delete()
        return JsonResponse({'errno': 0, 'msg': "删除成功"})
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

