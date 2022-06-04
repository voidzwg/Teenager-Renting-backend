
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt  # 跨域设置
def get_cart(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        cart_list = Carts.objects.filter(uid=uid).select_related('hid')
        return house_serializes(cart_list)
    else:
        return JsonResponse({'error': 1, 'msg': "请求方式错误"})


def get_house(request):
    if request.method == 'GET':
        houses = Houses.objects.all()
        return house_serializes(houses)
    else:
        return JsonResponse({'error': 1, 'msg': '请求方式错误'})



