from django.db.models import Q

from .models import *


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
        keywords.strip()
        import re
        num = re.findall(r"\d+\.?\d*",keywords)
        text = re.sub(r"\d+\.?\d*","",keywords)
        house_list = Houses.objects.filter(location__icontains=text)
        for i in num:
            house_list = house_list | Houses.objects.filter(Q(area=i)|Q(long_price=i)|Q(short_price=i))
        return house_serializes(house_list)
    else:
        return JsonResponse({'error': 1, 'msg': '请求方式错误'})
