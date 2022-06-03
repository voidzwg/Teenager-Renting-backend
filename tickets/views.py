from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Tickets
import pytz


# Create your views here.
@csrf_exempt
def get_tickets(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        data = []

        def sort():
            tb = ['status', '-date']
            return tb

        tickets_list = Tickets.objects.filter(uid=uid).order_by(*sort())
        for ticket in tickets_list:
            json = {
                "wid": ticket.wid,
                "hid": ticket.hid,
                "info": ticket.info,
                "status": ticket.status,
                "date": ticket.date
            }

    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
