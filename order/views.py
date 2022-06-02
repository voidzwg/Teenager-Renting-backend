from base64 import b64encode
from django.http import JsonResponse
from .models import *


def init(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        order_list = Orders.objects.filter(uid=uid).order_by('-order_time').order_by('paid')
        return order_serialize(order_list)
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})


def get_unpaid(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        order_list = Orders.objects.filter(uid=uid, paid=0).order_by('-order_time').order_by('paid')
        return order_serialize(order_list)
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})


def get_paid(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        order_list = Orders.objects.filter(uid=uid, paid=1).order_by('-order_time').order_by('paid')
        return order_serialize(order_list)
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})


def pay(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        oid = request.POST.get('oid')
        try:
            order = Orders.objects.get(uid=uid, id=oid)
        except:
            return JsonResponse({'error': 2, 'msg': "不存在此订单，可能是参数传入错误"})
        if order.paid == 1:
            return JsonResponse({'error': 3, 'msg': "该订单已支付"})
        else:
            order.paid = 1
            order.save()
            return JsonResponse({'error': 0, 'msg': "支付成功"})
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})


def delete(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        oid = request.POST.get('oid')
        try:
            Orders.objects.get(uid=uid, id=oid).delete()
        except:
            return JsonResponse({'error': 2, 'msg': "不存在此订单，可能是参数传入错误"})
        return JsonResponse({'error': 0, 'msg': "删除成功"})
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})

def cancel(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        oid = request.POST.get('oid')
        try:
            order = Orders.objects.get(uid=uid, id=oid)
        except:
            return JsonResponse({'error': 2, 'msg': "不存在此订单，可能是参数传入错误"})
        if order.status == 2:
            return JsonResponse({'error': 3, 'msg': "该订单已取消"})
        else:
            order.status = 2
            order.save()
            return JsonResponse({'error': 0, 'msg': "取消成功"})
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})