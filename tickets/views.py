from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Tickets, Users, Houses
from com.funcs import *


# Create your views here.
@csrf_exempt
def get_tickets(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        uid = Users.objects.get(id=uid)
        tickets_list = Tickets.objects.filter(uid=uid).order_by(*sort_tickets_by_date_and_status())
        return ticket_serialize(tickets_list)
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def get_checked_tickets(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        uid = Users.objects.get(id=uid)
        tickets_list = Tickets.objects.filter(uid=uid, status=4).order_by(*sort_tickets_by_date())
        return ticket_serialize(tickets_list)
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def get_finished_tickets(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        uid = Users.objects.get(id=uid)
        tickets_list = Tickets.objects.filter(uid=uid, status=3).order_by(*sort_tickets_by_date())
        return ticket_serialize(tickets_list)
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def get_processing_tickets(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        uid = Users.objects.get(id=uid)
        tickets_list = Tickets.objects.filter(uid=uid, status=2).order_by(*sort_tickets_by_date())
        return ticket_serialize(tickets_list)
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def get_pending_tickets(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        uid = Users.objects.get(id=uid)
        tickets_list = Tickets.objects.filter(uid=uid, status=1).order_by(*sort_tickets_by_date())
        return ticket_serialize(tickets_list)
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def submit_ticket(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        hid = request.POST.get('hid')
        info = request.POST.get('info')
        pictures = request.POST.get('pictures')
        if pictures == "":
            pictures = None
        else:
            pictures = pictures.encode(encoding='utf-8')
        uid = Users.objects.get(id=uid)
        hid = Houses.objects.get(id=hid)
        new_ticket = Tickets(uid=uid, hid=hid, info=info, pictures=pictures, status=1, comment=5)
        new_ticket.save()
        return JsonResponse({'errno': 0, 'msg': "申请成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
