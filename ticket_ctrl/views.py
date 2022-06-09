from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tickets, Workers, Complaints
from com.funcs import *


# Create your views here.
@csrf_exempt
def get_ticket_info(request):
    if request.method == 'GET':
        ticket_list = Tickets.objects.filter()
        return ticket_serialize_full(ticket_list)
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def create_ticket(request):
    if request.method == 'POST':
        tid = request.POST.get('ticketid')
        wid = request.POST.get('workerid')
        date = request.POST.get('date')  # 传入date类型参数，例如"2022-6-25"
        try:
            ticket = Tickets.objects.get(id=tid)
        except:
            print("In ticket_ctrl_ctrl/create_ticket: ticket is not exist")
            return JsonResponse({'errno': 1002, 'msg': "投诉不存在"})
        try:
            worker = Workers.objects.get(id=wid)
        except:
            print("In ticket_ctrl_ctrl/create_ticket: worker is not exist")
            return JsonResponse({'errno': 1002, 'msg': "师傅不存在"})
        ticket.wid = worker
        ticket.date = date
        if ticket.status == 1:
            ticket.status = 2
        elif ticket.status == 2 or ticket.status == 3:
            return JsonResponse({'errno': 1005, 'msg': "工单正在处理"})
        else:
            return JsonResponse({'errno': 1005, 'msg': "工单已处理完毕"})
        ticket.pictures = set_b64_bin(ticket.pictures)
        ticket.materials_pic = set_b64_bin(ticket.materials_pic)
        ticket.save()
        return JsonResponse({'errno': 0, 'msg': "生成工单成功"})
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def get_complaints(request):
    if request.method == 'GET':
        complaints_list = Complaints.objects.filter()
        return complaint_serialize(complaints_list)
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def reply_complaint(request):
    if request.method == 'POST':
        cid = request.POST.get('complaintid')
        reply = request.POST.get('reply')
        if not reply:
            return JsonResponse({'errno': 1003, 'msg': "回复不能为空"})
        complaint = Complaints.objects.get(id=cid)
        complaint.reply = reply
        complaint.pictures = set_b64_bin(complaint.pictures)
        complaint.save()
        return JsonResponse({'errno': 0, 'msg': "回复成功"})
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def check_ticket(request):
    if request.method == 'POST':
        tid = request.POST.get('ticketid')
        try:
            ticket = Tickets.objects.get(id=tid)
        except:
            print("In ticket_ctrl_ctrl/check_ticket: ticket is not exist")
            return JsonResponse({'errno': 1002, 'msg': "工单不存在"})
        if ticket.status == 3:
            ticket.status = 4
            ticket.pictures = set_b64_bin(ticket.pictures)
            ticket.materials_pic = set_b64_bin(ticket.materials_pic)
            ticket.save()
            return JsonResponse({'errno': 0, 'msg': "审核成功"})
        elif ticket.status == 4:
            return JsonResponse({'errno': 1004, 'msg': "工单已完成"})
        return JsonResponse({'errno': 1004, 'msg': "工单尚未完成"})
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

