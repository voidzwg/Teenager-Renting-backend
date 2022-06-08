from django.views.decorators.csrf import csrf_exempt
from com.funcs import *
from .models import Workers, Tickets, Complaints, Users
from functools import cmp_to_key


# Create your views here.
@csrf_exempt
def get_complaints(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        complaints_list = Complaints.objects.filter(uid=uid)
        complaints_list = sorted(complaints_list, key=cmp_to_key(sort_complaints_by_reply))
        return complaint_serialize(complaints_list)
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def get_replied_complaints(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        complaints = Complaints.objects.filter(uid=uid)
        complaints_list = []
        for complaint in complaints:
            if complaint.reply:
                complaints_list.append(complaint)
        return complaint_serialize(complaints_list)
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def get_ignored_complaints(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        complaints = Complaints.objects.filter(uid=uid)
        complaints_list = []
        for complaint in complaints:
            if not complaint.reply:
                complaints_list.append(complaint)
        return complaint_serialize(complaints_list)
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def submit_complaint(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        tid = request.POST.get('tid')
        contents = request.POST.get('contents')
        pictures = request.POST.get('pictures')
        try:
            user = Users.objects.get(id=uid)
        except:
            return JsonResponse({'errno': 1002, 'msg': "用户不存在"})
        try:
            ticket = Tickets.objects.get(id=tid)
        except:
            return JsonResponse({'errno': 1002, 'msg': "工单不存在"})
        if not contents:
            return JsonResponse({'errno': 1003, 'msg': "投诉内容不能为空"})
        if pictures:
            pictures = pictures.encode(encoding='utf-8')
        else:
            pictures = None
        new_complaint = Complaints(uid=user, tid=ticket, contents=contents, pictures=pictures)
        new_complaint.save()
        return JsonResponse({'errno': 0, 'msg': "提交投诉成功"})
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

