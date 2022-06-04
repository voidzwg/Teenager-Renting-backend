from base64 import b64encode
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

@csrf_exempt  # 跨域设置
def init(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        cart_list = Carts.objects.filter(uid=uid).select_related('hid')
        data = []
        for i in cart_list:
            try:
                picture =  b64encode(i.hid.pictures).decode('utf8')
            except:
                picture = None
            try:
                floor_plan = b64encode(i.hid.floor_plan).decode('utf8')
            except:
                floor_plan = None
            p_tmp = {
                "id": i.hid.id,
                "short_price": i.hid.short_price,
                "long_price": i.hid.long_price,
                "area": i.hid.area,
                "location": i.hid.location,
                "type": i.hid.type,
                "available": i.hid.available,
                "floor_plan": floor_plan,
                "pictures": picture,
                "detail": i.hid.details
            }
            data.append(p_tmp)
        return JsonResponse(data,safe = False)
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
            Orders.objects.create(
                uid = uid,hid = hid,type =type,order_time=order_time,
                duration = duration,amount = amount,details = details,
                paid = paid,status = status,start_time=start_time
            )
        except:
            return JsonResponse({'error':6,'msg':"创建失败，原因未知，请看后端报错"})
        hid.available = 0
        hid.save()
        return JsonResponse({'error':0,'msg':"提交订单成功，该房源已锁定"})
    else:
        return JsonResponse({'error':1,'msg':"请求方式错误"})
@csrf_exempt  # 跨域设置
def delete(request):
    uid = request.POST.get('uid')
    hid = request.POST.get('hid')
    if uid is None or hid is None:
        return JsonResponse({'error': 2, 'msg': "uid或hid为空"})
    try:
        cart = Carts.objects.filter(uid = uid,hid = hid)
    except:
        return JsonResponse({'error':1,'msg':"不存在该购物车"})
    try:
        cart.delete()
    except:
        return JsonResponse({'error':3,'msg':"删除失败，原因未知，请看后端报错"})
    return JsonResponse({'error':0,'msg':"删除成功"})