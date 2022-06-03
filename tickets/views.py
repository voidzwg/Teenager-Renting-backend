from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def get_tickets(request):
    if request.method == 'GET':
        id = request.GET.get('uid')

    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

