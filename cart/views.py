from base64 import b64encode
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from com.funcs import *
from .models import *

@csrf_exempt  # 跨域设置
def init(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        cart_list = Carts.objects.filter(uid=uid).select_related('hid')
        return house_serializes(cart_list)
    else:
        return JsonResponse({'error':1,'msg':"请求方式错误"})


@csrf_exempt  # 跨域设置
def submit(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        hid = request.POST.get('hid')
        if uid is None or hid is None:
            return JsonResponse({'error':2,'msg':"uid或hid为空"})
        try:
            uid = Users.objects.get(id=uid)
        except:
            return JsonResponse({'error':3,'msg':"用户不存在"})
        try:
            hid = Houses.objects.get(id=hid)
        except:
            return JsonResponse({'error':4,'msg':"房源不存在"})
        if hid.available == 0:
            return JsonResponse({'error':5,'msg':"该房源暂不可得或已被出租"})
        type= request.POST.get('type')
        order_time  = request.POST.get('order_time')
        start_time = request.POST.get('start_time')
        duration = request.POST.get('duration')
        amount = request.POST.get('amount')
        if order_time is None or start_time is None or duration is None or amount is None:
            return JsonResponse({'error':2,'msg':"其他非空参数为空"})
        details = request.POST.get('details')
        paid = 0
        status = 0
        try:
            order=Orders.objects.create(
                uid = uid,hid = hid,type =type,order_time=order_time,
                duration = duration,amount = amount,details = details,
                paid = paid,status = status,start_time=start_time
            )
        except:
            return JsonResponse({'error':6,'msg':"创建失败，原因未知，请看后端报错"})
        try:
            cart = Carts.objects.get(uid=uid,hid=hid)
            cart.delete()
        except:
            return JsonResponse({'error': 7, 'msg': "订单创建成功，但对应购物车删除失败，可能是不存在对应购物车"})
        return JsonResponse({'error':0,'msg':"提交订单成功，该房源已锁定",'订单id':order.id})
    else:
        return JsonResponse({'error':1,'msg':"请求方式错误"})
@csrf_exempt  # 跨域设置
def delete(request):
    uid = request.POST.get('uid')
    hid = request.POST.get('hid')
    if uid is None or hid is None:
        return JsonResponse({'error': 2, 'msg': "uid或hid为空"})
    try:
        uid = Users.objects.get(id=uid)
    except:
        return JsonResponse({'error': 3, 'msg': "用户不存在"})
    try:
        hid = Houses.objects.get(id=hid)
    except:
        return JsonResponse({'error': 4, 'msg': "房源不存在"})
    try:
        cart = Carts.objects.get(uid = uid,hid = hid)
    except:
        return JsonResponse({'error':1,'msg':"不存在该购物车"})
    try:
        cart.delete()
    except:
        return JsonResponse({'error':3,'msg':"删除失败，原因未知，请看后端报错"})
    return JsonResponse({'error':0,'msg':"删除成功"})