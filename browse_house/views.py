import random
from base64 import b64encode

from django.http import JsonResponse

from .models import *
# Create your views here.
def init(request):
    house_list = Houses.objects.all()
    data = []
    for i in house_list[0:50]:
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
            "pictures": picture,
            "detail": i.details
        }
        data.append(p_tmp)
    return JsonResponse(data,safe = False)