from django.shortcuts import render

# Create your views here.
from .models import *


def init(request):
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


def get_house(request):
    if request.method == 'GET':
        houses = Houses.objects.all()
        return house_serialize(houses)
    else:
        return JsonResponse({'error': 1, 'msg': '请求方式错误'})

def get_data(request):
    if request.method == 'GET':
        tickets=Tickets.objects.filter(status=3).count()
        complaints = Complaints.objects.filter(reply__isnull=False).count()
        orders = Orders.objects.filter(status=1).count()
        return JsonResponse({'tickets':tickets,'order':orders,'complaints':complaints})
    else:
        return JsonResponse({'error': 1, 'msg': '请求方式错误'})