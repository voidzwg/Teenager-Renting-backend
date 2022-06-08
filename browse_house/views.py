from django.db.models import Q
from .models import *
from com.funcs import *
import re

def get_house(request):
    if request.method == 'GET':
        hid = request.GET.get('hid')
        if hid == None:
            return JsonResponse({'error': 2, 'msg': '无uid传入'})
        try:
            house = Houses.objects.get(id=hid)
        except:
            return JsonResponse({'error': 3, 'msg': '无此用户'})
        return house_serialize(house)
    else:
        return JsonResponse({'error': 1, 'msg': '请求方式错误'})


def get_user(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        if uid == None:
            return JsonResponse({'error':2,'msg':'无uid传入'})
        try:
            user = Users.objects.get(id=uid)
        except:
            return JsonResponse({'error':3,'msg':'无此用户'})
        return user_serialize(user)
    else:
        return JsonResponse({'error':1,'msg':'请求方式错误'})


def search(request):
    if request.method == 'GET':
        keywords = request.GET.get('keywords')
        if keywords is None or re.match(r"\s*",keywords):
            keywords = ''
        type = request.GET.get('type')
        rent = request.GET.get('rent')
        if rent is None:
            rent = 0
        price = request.GET.getlist('price')
        keywords.strip()
        text = re.sub(r"\d+\.?\d*", "", keywords)
        house_list = Houses.objects.filter(location__icontains=text).filter(type=type)
        list = []
        if len(price)== 2 :
            if rent == 1:
                for i in house_list:
                    if float(price[0]) <= i.short_price <= float(price[1]):
                        list.append(i)
            else:
                for i in house_list:
                    if float(price[0]) <= i.long_price <= float(price[1]):
                        list.append(i)
        elif len(price) == 1:
            if rent == 1:
                for i in house_list:
                    if i.short_price <= float(price[0]):
                        list.append(i)
            else:
                for i in house_list:
                    if i.long_price <= float(price[0]):
                        list.append(i)
        return house_serializes(list)
    else:
        return JsonResponse({'error': 1, 'msg': '请求方式错误'})

def add_cart(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        hid = request.POST.get('hid')
        if uid is None or hid is None:
            return JsonResponse({'error': 2, 'msg': 'uid或hid为空'})
        try:
            user = Users.objects.get(id=uid)
        except:
            return JsonResponse({'error':3,'msg':'无此用户'})
        try:
            house = Houses.objects.get(id=hid)
        except:
            return JsonResponse({'error': 4, 'msg': '无此房源'})
        try:
            cart = Carts.objects.get(uid=user,hid=house)
        except:
            None
        else:
            return JsonResponse({'error': 5, 'msg': '购物车已存在该房源'})
        try:
            Carts.objects.create(uid=user,hid=house)
        except:
            return JsonResponse({'error': 6, 'msg': '加入失败，原因未知，请看后端报错'})
        return JsonResponse({'error': 0, 'msg': '添加成功'})
    else:
        return JsonResponse({'error': 1, 'msg': '请求方式错误'})