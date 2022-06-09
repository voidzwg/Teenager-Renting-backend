from imp import reload

from django.core import mail
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import *
from com.funcs import *
from teen_renting.settings import *


def init(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        if uid is None:
            return JsonResponse({'error': 2, 'msg': "参数传入错误"})
        order_list = Orders.objects.filter(uid=uid).order_by('-order_time').order_by('paid')
        if order_list.count() == 0:
            return JsonResponse({'error': 0, 'msg': "订单为空"})
        return order_serialize(order_list)
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})


def get_unpaid(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        if uid is None:
            return JsonResponse({'error': 2, 'msg': "参数传入错误"})
        order_list = Orders.objects.filter(uid=uid, paid=0).order_by('-order_time').order_by('paid')
        if order_list.count() == 0:
            return JsonResponse({'error': 0, 'msg': "订单为空"})
        return order_serialize(order_list)
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})


def get_paid(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        if uid is None:
            return JsonResponse({'error': 2, 'msg': "参数传入错误"})
        order_list = Orders.objects.filter(uid=uid, paid=1).order_by('-order_time').order_by('paid')
        if order_list.count() == 0:
            return JsonResponse({'error': 0, 'msg': "订单为空"})
        return order_serialize(order_list)
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})


def pay(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        oid = request.POST.get('oid')
        if uid is None or oid is None:
            return JsonResponse({'error': 2, 'msg': "参数传入错误"})
        try:
            order = Orders.objects.get(uid=uid, id=oid)
        except:
            return JsonResponse({'error': 3, 'msg': "不存在此订单，可能是参数传入错误"})
        if order.paid == 1:
            return JsonResponse({'error': 4, 'msg': "该订单已支付"})
        else:
            order.paid = 1
            order.save()
            return JsonResponse({'error': 0, 'msg': "支付成功"})
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})


def delete(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        oid = request.POST.get('oid')
        if uid is None or oid is None:
            return JsonResponse({'error': 2, 'msg': "参数传入错误"})
        try:
            order = Orders.objects.get(uid=uid, id=oid)
        except:
            return JsonResponse({'error': 3, 'msg': "不存在此订单，可能是参数传入错误"})
        hid = order.hid
        status = order.status
        try:
            order.delete()
        except:
            return JsonResponse({'error': 4, 'msg': "删除失败，原因未知，请看后端报错"})
        if status != 2:       # 意思是，如果该订单删除前已被取消，则删除时不需要再释放房源
            hid.available = 1
            hid.save()
        return JsonResponse({'error': 0, 'msg': "删除成功"})
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})


def cancel(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        oid = request.POST.get('oid')
        if uid is None or oid is None:
            return JsonResponse({'error': 2, 'msg': "参数传入错误"})
        try:
            order = Orders.objects.get(uid=uid, id=oid)
        except:
            return JsonResponse({'error': 3, 'msg': "不存在此订单，可能是参数传入错误"})
        if order.status == 2:
            return JsonResponse({'error': 4, 'msg': "该订单已取消"})
        else:
            #修改状态
            order.status = 2
            order.save()
            return JsonResponse({'error': 0, 'msg': "取消成功,该房源已解锁"})
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})

def renew(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        oid = request.POST.get('oid')
        time = request.POST.get('time')
        if uid is None or oid is None:
            return JsonResponse({'error': 2, 'msg': "参数传入错误"})
        try:
            order = Orders.objects.get(uid=uid, id=oid)
        except:
            return JsonResponse({'error': 3, 'msg': "不存在此订单，可能是参数传入错误"})
        if order.type == 0:
            return JsonResponse({'error': 4, 'msg': "短租订单不可续约"})
        try:
            order.duration += time
            order.save()
        except:
            return JsonResponse({'error': 5, 'msg': "未知错误"})
        return JsonResponse({'error': 0, 'msg': "续约成功"})
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})

def send_email(request):
    if request.method == 'GET':
        subject = '收租提醒'  #主题
        from_email = EMAIL_FROM  # 发件人，在settings.py中已经配置
        to_email = ['2874820539@qq.com','20373830@buaa.edu.cn']  #邮件接收者列表
        # 发送的消息
        message = '青年租房网站提醒您：该缴租金啦！,点击进入网站 http://localhost:8000/'  # 发送普通的消息使用的时候message
        #meg_html = '<a href="http://localhost:8000/">点击跳转</a>'  # 发送的是一个html消息 需要指定
        send_mail(subject=subject, message=message, from_email=from_email,recipient_list=to_email)
        return HttpResponse('OK,邮件已经发送成功!')
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})

def send_alone_email(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        user = Users.objects.get(id=uid)
        email = user.email
        subject = '收租提醒'  # 主题
        from_email = EMAIL_FROM  # 发件人，在settings.py中已经配置
        to_email = [email]  # 邮件接收者列表
        # 发送的消息
        message = '青年租房网站提醒您：该缴租金啦！,点击进入网站 http://localhost:8000/'  # 发送普通的消息使用的时候message
        # meg_html = '<a href="http://localhost:8000/">点击跳转</a>'  # 发送的是一个html消息 需要指定
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_email)
        return HttpResponse('OK,邮件已经发送成功!')
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})