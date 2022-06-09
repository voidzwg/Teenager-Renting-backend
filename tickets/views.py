from django.views.decorators.csrf import csrf_exempt
from .models import Tickets, Users, Houses
from com.funcs import *


# Create your views here.
@csrf_exempt
def get_tickets(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        uid = Users.objects.get(id=uid)
        tickets_list = Tickets.objects.filter(uid=uid).order_by(*sort_tickets_by_status_and_date())
        return ticket_serialize(tickets_list)
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def get_checked_tickets(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        uid = Users.objects.get(id=uid)
        tickets_list = Tickets.objects.filter(uid=uid, status=4).order_by(*sort_tickets_by_date())
        return ticket_serialize(tickets_list)
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def get_finished_tickets(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        uid = Users.objects.get(id=uid)
        tickets_list = Tickets.objects.filter(uid=uid, status=3).order_by(*sort_tickets_by_date())
        return ticket_serialize(tickets_list)
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def get_processing_tickets(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        uid = Users.objects.get(id=uid)
        tickets_list = Tickets.objects.filter(uid=uid, status=2).order_by(*sort_tickets_by_date())
        return ticket_serialize(tickets_list)
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def get_pending_tickets(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        uid = Users.objects.get(id=uid)
        tickets_list = Tickets.objects.filter(uid=uid, status=1).order_by(*sort_tickets_by_date())
        return ticket_serialize(tickets_list)
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def submit_ticket(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        hid = request.POST.get('hid')
        info = request.POST.get('info')
        pictures = request.POST.get('pictures')
        if pictures:
            pictures = pictures.encode(encoding='utf-8')
        else:
            pictures = None
        try:
            user = Users.objects.get(id=uid)
        except:
            return JsonResponse({'errno': 1005, 'msg': "用户不存在"})
        try:
            house = Houses.objects.get(id=hid)
        except:
            return JsonResponse({'errno': 1005, 'msg': "房子不存在"})
        new_ticket = Tickets(uid=user, hid=house, info=info, pictures=pictures, status=1, comment=5)
        new_ticket.save()
        return JsonResponse({'errno': 0, 'msg': "申请成功"})
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def comment(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        tid = request.POST.get('tid')
        score = request.POST.get('score')
        details = request.POST.get('details')
        if uid is None or tid is None:
            return JsonResponse({'errno': 1, 'msg': "没有uid或tid"})
        if score is None:
            return JsonResponse({'errno': 2, 'msg': "没有score"})
        if not (1 <= int(score) <= 5):
            return JsonResponse({'errno': 3, 'msg': "score不合法"})
        try:
            ticket = Tickets.objects.get(id=tid, uid=uid)  # tid 改为 id
        except:
            return JsonResponse({'errno': 4, 'msg': "无此工单"})
        try:
            ticket.comment = score
            ticket.details = details
            ticket.pictures = set_b64_bin(ticket.pictures)  # 处理图片 by zwg
            ticket.materials_pic = set_b64_bin(ticket.materials_pic)
            ticket.save()
        except:
            return JsonResponse({'errno': 5, 'msg': "评价失败"})
        return JsonResponse({'errno': 0, 'msg': "评价成功"})
    return JsonResponse({'errno': 1, 'msg': "请求方式错误"})
