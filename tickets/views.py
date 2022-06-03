from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Tickets
from com.funcs import *


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
            materials_pic = set_b64_string(ticket.materials_pic.decode("utf-8"))
            pictures = set_b64_string(ticket.pictures.decode("utf-8"))
            json_data = {
                "wid": ticket.wid,
                "hid": ticket.hid,
                "info": ticket.info,
                "status": ticket.status,
                "date": ticket.date,
                "materials_pic": materials_pic,
                "materials_text": ticket.materials_text,
                "comment": ticket.comment,
                "pictures": pictures,
                "details": ticket.details
            }
            data.append(json_data)
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

