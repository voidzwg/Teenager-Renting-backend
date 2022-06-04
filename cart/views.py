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
            picture =  b64encode(i.hid.pictures).decode('utf8')
            floor_plan = b64encode(i.hid.floor_plan).decode('utf8')
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
        uid = Users.objects.get(id=uid)
        hid = request.POST.get('hid')
        hid = Houses.objects.get(id=hid)
        type= request.POST.get('type')
        order_time  = request.POST.get('order_time')
        duration = request.POST.get('duration')
        amount = request.POST.get('amount')
        details = request.POST.get('details')
        paid = 0
        status = 0
        Orders.objects.create(
            uid = uid,hid = hid,type =type,order_time=order_time,
            duration = duration,amount = amount,details = details,
            paid = paid,status = status
        )
        return JsonResponse({'error':0,'msg':"提交订单成功"})
    else:
        return JsonResponse({'error':1,'msg':"请求方式错误"})
@csrf_exempt  # 跨域设置
def delete(request):
    uid = request.POST.get('uid')
    hid = request.POST.get('hid')
    try:
        Carts.objects.get(uid = uid,hid = hid).delete()
    except:
        return JsonResponse({'error':1,'msg':"删除失败"})
    return JsonResponse({'error':0,'msg':"删除成功"})