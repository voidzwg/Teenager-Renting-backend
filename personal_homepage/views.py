from base64 import b64encode
from typing import List, Any

from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils.baseconv import base64
from django.views.decorators.csrf import csrf_exempt
from .models import *
import io
from PIL import Image

# Create your views here.
def init(request):
    uid = request.POST.get('id')

    cart_list = Carts.objects.filter(uid=uid)
    house_list = []
    for c in cart_list:
        id = c.hid.id
        temp=Houses.objects.get(id=id)
        house_list.append(temp)
    data = []
    for i in house_list:
        picture =  b64encode(i.pictures).decode('utf8')
        floor_plan = b64encode(i.floor_plan).decode('utf8')
        p_tmp = {
            "id": i.id,
            "short_price": i.short_price,
            "long_price": i.long_price,
            "area": i.area,
            "location": i.location,
            "type": i.type,
            "available": i.available,
            "floor_plan": floor_plan,
            "picyures": picture,
            "detail": i.details
        }
        data.append(p_tmp)
    return JsonResponse(data,safe = False)




