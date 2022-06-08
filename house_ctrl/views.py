from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Users, Houses, Orders
from com.funcs import *
from time import time, strptime, mktime
from datetime import datetime


# Create your views here.
@csrf_exempt
def get_house_info(request):
    if request.method == 'GET':
        houses_list = Houses.objects.filter()
        return house_list_serialize(houses_list)
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def rent_house(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        try:
            user = Users.objects.get(id=uid)
        except:
            print("In house_ctrl/rent_house: user is not exist")
            return JsonResponse({'errno': 1002, 'msg': "用户不存在"})
        hid = request.POST.get('hid')
        try:
            house = Houses.objects.get(id=hid)
        except:
            print("In house_ctrl/rent_house: house is not exist")
            return JsonResponse({'errno': 1002, 'msg': "房子不存在"})
        rent_type = request.POST.get('type')
        duration = request.POST.get('duration')
        order_time = datetime.fromtimestamp(int(time()))
        start_time = request.POST.get('start_time')
        if not start_time:
            start_time = order_time
        else:
            start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        if start_time < order_time:
            return JsonResponse({'errno': 1003, 'msg': "时间错误"})
        amount = request.POST.get('amount')
        details = request.POST.get('details')
        if not amount:
            amount = 0
        new_order = Orders(uid=user, hid=house, type=int(rent_type), paid=1,
                           status=0, order_time=order_time, start_time=start_time,
                           duration=int(duration), amount=amount, details=details)
        new_order.save()
        return JsonResponse({'errno': 0, 'msg': "租房成功"})
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def add_house(request):
    if request.method == 'POST':
        sp = request.POST.get('short_price')
        lp = request.POST.get('long_price')
        location = request.POST.get('location')
        area = request.POST.get('area')
        house_type = request.POST.get('type')
        fp = request.POST.get('floor_plan')
        pictures = request.POST.get('pictures')
        details = request.POST.get('details')
        if fp:
            fp = fp.encode(encoding="utf-8")
        else:
            fp = None
        if pictures:
            pictures = pictures.encode(encoding="utf-8")
        else:
            pictures = None
        if not details:
            details = None
        new_house = Houses(short_price=float(sp), long_price=float(lp), location=location,
                           area=float(area), available=1, type=int(house_type), floor_plan=fp,
                           pictures=pictures, details=details)
        new_house.save()
        return JsonResponse({'errno': 0, 'msg': "添加房源成功"})
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def stop_renting(request):
    if request.method == 'POST':
        hid = request.POST.get('houseid')
        try:
            house = Houses.objects.get(id=hid)
        except:
            print("In house_ctrl/stop_renting: house is not exist")
            return JsonResponse({'errno': 1002, 'msg': "房子不存在"})
        if house.available:
            house.available = 0
            try:
                house.pictures = set_b64_string(house.pictures.decode('utf-8')).encode(encoding='utf-8')
                house.floor_plan = set_b64_string(house.floor_plan.decode('utf-8')).encode(encoding='utf-8')
            except:
                pass
            house.save()
        return JsonResponse({'errno': 0, 'msg': "暂停出租成功"})
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def del_house(request):
    if request.method == 'POST':
        hid = request.POST.get('houseid')
        try:
            house = Houses.objects.get(id=hid)
        except:
            print("In house_ctrl/stop_renting: house is not exist")
            return JsonResponse({'errno': 1002, 'msg': "房子不存在"})
        house.delete()
        return JsonResponse({'errno': 0, 'msg': "删除房源成功"})
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

