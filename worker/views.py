from django.views.decorators.csrf import csrf_exempt
from com.funcs import *
from .models import Workers, Tickets


# Create your views here.
@csrf_exempt
def get_worker_info(request):
    if request.method == 'POST':
        wid = request.POST.get('workerid')
        print('wid', wid)
        print('type', type(wid))
        try:
            worker = Workers.objects.get(id=int(wid))
        except:
            print("In worker/get_worker_info: no such worker")
            return JsonResponse({'errno': 1002, 'msg': "师傅不存在"})
        return worker_serialize([worker])
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def select_tickets(request):
    if request.method == 'POST':
        wid = request.POST.get('workerid')
        try:
            worker = Workers.objects.get(id=int(wid))
        except:
            print("In worker/select_tickets: no such worker")
            return JsonResponse({'errno': 1002, 'msg': "师傅不存在"})
        tickets_list = Tickets.objects.filter(wid=wid)
        return ticket_serialize_full(tickets_list)
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def submit_materials(request):
    if request.method == 'POST':
        tid = request.POST.get('ticketid')
        pic = request.POST.get('materials_pic')
        text = request.POST.get('materials_text')
        try:
            ticket = Tickets.objects.get(id=tid)
        except:
            print("In worker/submit_materials: no such ticket")
            return JsonResponse({'errno': 1002, 'msg': "工单不存在"})
        if not pic and not text:
            print("In worker/submit_materials: no submit")
            return JsonResponse({'errno': 1003, 'msg': "提交内容不能为空"})
        if ticket.status == 2 or ticket.status == 3:
            ticket.status = 3
        elif ticket.status == 1:
            return JsonResponse({'errno': 1004, 'msg': "系统错误：无效提交"})
        else:
            return JsonResponse({'errno': 1005, 'msg': "审核已完成，无需提交"})
        if pic:
            pic = pic.encode(encoding='utf-8')
        else:
            pic = None
        if not text:
            text = None
        ticket.materials_pic = pic
        ticket.materials_text = text
        try:
            ticket.pictures = set_b64_string(ticket.pictures.decode('utf-8')).encode(encoding='utf-8')
        except:
            pass
        ticket.save()
        return JsonResponse({'errno': 0, 'msg': "提交成功"})
    return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

