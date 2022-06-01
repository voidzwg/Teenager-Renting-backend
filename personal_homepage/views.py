from base64 import b64encode
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
@csrf_exempt  # 跨域设置
def init(request):
    uid = request.POST.get('id')
    cart_list = Carts.objects.filter(uid=uid).select_related('hid')
    data = []
    for i in cart_list[0:5]:
        picture =  b64encode(i.hid.pictures).decode('utf8')
        floor_plan = b64encode(i.hid.floor_plan).decode('utf8')
        p_tmp = {
            "id": i.hid.id,
            "short_price": i.hid.short_price,
            "long_price": i.hid.long_price,
            "area": i.hid.area,
            "location": i.hid.location,
            "type": i.hid.type,
            "available": i.hid.available,
            "floor_plan": floor_plan,
            "pictures": picture,
            "detail": i.hid.details
        }
        data.append(p_tmp)
    return JsonResponse(data,safe = False)




