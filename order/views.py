from base64 import b64encode
from django.http import JsonResponse
from .models import *


def init(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        if uid is None:
            return JsonResponse({'error': 2, 'msg': "参数传入错误"})
        order_list = Orders.objects.filter(uid=uid).order_by('-order_time').order_by('paid')
        if order_list.count() == 0:
            return JsonResponse({'error': 0, 'msg': "订单为空"})
        return order_serialize(order_list)
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})


def get_unpaid(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        if uid is None:
            return JsonResponse({'error': 2, 'msg': "参数传入错误"})
        order_list = Orders.objects.filter(uid=uid, paid=0).order_by('-order_time').order_by('paid')
        if order_list.count() == 0:
            return JsonResponse({'error': 0, 'msg': "订单为空"})
        return order_serialize(order_list)
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})


def get_paid(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        if uid is None:
            return JsonResponse({'error': 2, 'msg': "参数传入错误"})
        order_list = Orders.objects.filter(uid=uid, paid=1).order_by('-order_time').order_by('paid')
        if order_list.count() == 0:
            return JsonResponse({'error': 0, 'msg': "订单为空"})
        return order_serialize(order_list)
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})


def pay(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        oid = request.POST.get('oid')
        if uid is None or oid is None:
            return JsonResponse({'error': 2, 'msg': "参数传入错误"})
        try:
            order = Orders.objects.get(uid=uid, id=oid)
        except:
            return JsonResponse({'error': 3, 'msg': "不存在此订单，可能是参数传入错误"})
        if order.paid == 1:
            return JsonResponse({'error': 4, 'msg': "该订单已支付"})
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
        if uid is None or oid is None:
            return JsonResponse({'error': 2, 'msg': "参数传入错误"})
        try:
            order = Orders.objects.get(uid=uid, id=oid)
        except:
            return JsonResponse({'error': 3, 'msg': "不存在此订单，可能是参数传入错误"})
        hid = order.hid
        status = order.status
        try:
            order.delete()
        except:
            return JsonResponse({'error': 4, 'msg': "删除失败，原因未知，请看后端报错"})
        if status != 2:       # 意思是，如果该订单删除前已被取消，则删除时不需要再释放房源
            hid.available = 1
            hid.save()
        return JsonResponse({'error': 0, 'msg': "删除成功"})
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})

def cancel(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        oid = request.POST.get('oid')
        if uid is None or oid is None:
            return JsonResponse({'error': 2, 'msg': "参数传入错误"})
        try:
            order = Orders.objects.get(uid=uid, id=oid)
        except:
            return JsonResponse({'error': 3, 'msg': "不存在此订单，可能是参数传入错误"})
        if order.status == 2:
            return JsonResponse({'error': 4, 'msg': "该订单已取消"})
        else:
            #修改状态
            order.status = 2
            order.save()
            #释放房源
            hid = order.hid
            hid.available = 1
            hid.save()
            return JsonResponse({'error': 0, 'msg': "取消成功,该房源已解锁"})
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})