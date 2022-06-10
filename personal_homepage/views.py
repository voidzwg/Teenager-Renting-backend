

from .models import *
from com.funcs import *
# Create your views here.

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


def get_cart(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        cart_list = Carts.objects.filter(uid=uid).select_related('hid')
        house_list = []
        for i in cart_list:
            house_list.append(i.hid)
        return house_serializes(house_list)
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})


def get_house(request):
    if request.method == 'GET':
        houses = Houses.objects.all()
        return house_serializes(houses)
    else:
        return JsonResponse({'error': 1, 'msg': '请求方式错误'})


def update_password(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        origin = request.POST.get('oldPass')
        newly1 = request.POST.get('newPass1')
        newly2 = request.POST.get('newPass2')
        if uid is None:
            return JsonResponse({'error': 2, 'msg': '无uid传入'})
        try:
            user = Users.objects.get(id=uid)
        except:
            return JsonResponse({'error': 3, 'msg': '无此用户'})
        if user.password != origin:
            return JsonResponse({'error': 4, 'msg': '原密码错误，禁止更新', 'true': user.password, 'false': origin})
        if check_password(newly1) is not True & check_password(newly2) is not True:
            return JsonResponse({'error': 5, 'msg': "新密码格式错误"})
        if newly1 != newly2:
            return JsonResponse({'error': 6, 'msg': "两次密码不一致，请检查后重新输入"})
        user.password = newly1
        user.avatar = set_b64_bin(user.avatar)
        user.save()
        return JsonResponse({'error': 0, 'msg': "修改成功"})
    else:
        return JsonResponse({'error': 1, 'msg': '请求方式错误'})


def update_avatar(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        avatar = request.POST.get('avatar')
        if avatar:
            avatar = avatar.encode(encoding='UTF-8')
        try:
            user = Users.objects.get(id=uid)
        except:
            return JsonResponse({'error': 2, 'msg': '无此用户'})
        user.avatar = avatar
        user.save()
        return JsonResponse({'error': 0, 'msg': '更新头像成功'})
    else:
        return JsonResponse({'error': 1, 'msg': '请求方式错误'})

