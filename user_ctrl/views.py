from base64 import b64encode, b64decode

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_ctrl.funcs import *
from .models import Users, Workers


# Create your views here.
# begin of 用户管理页面
@csrf_exempt
def update_info(request):
    if request.method == 'POST':
        id = request.POST.get('userid')
        username = request.POST.get('username')
        tel = request.POST.get('phoneNum')
        email = request.POST.get('email')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        check = check_info(tel, email)
        if check == 3:
            return JsonResponse({'errno': 1010, 'msg': "电话和邮箱至少有一个不为空"})
        elif check == 1:
            return JsonResponse({'errno': 1002, 'msg': "电话格式错误"})
        elif check == 2:
            return JsonResponse({'errno': 1004, 'msg': "邮箱格式错误"})
        if check_user_username(username) is not True:
            return JsonResponse({'errno': 1003, 'msg': "用户名格式错误"})
        if check_age(age) is not True:
            return JsonResponse({'errno': 1005, 'msg': "年龄错误"})
        if check_sex(sex) is not True:
            return JsonResponse({'errno': 1006, 'msg': "性别错误"})
        try:
            user = Users.objects.get(id=id)
        except:
            print("In user_ctrl/update_info: no such user")
            return JsonResponse({'errno': 1007, 'msg': "用户不存在"})
        else:
            user.email = email
            user.username = username
            user.tel = tel
            user.age = int(age)
            user.sex = int(sex)
            user.save()
            return JsonResponse({'errno': 0, 'msg': "修改成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def get_users_info(request):
    if request.method == 'GET':
        data = []
        user_list = Users.objects.filter()
        for user in user_list:
            json_data = {
                "id": user.id,
                "username": user.username,
                "tel": user.tel,
                "email": user.email,
                "name": user.name,
                "age": user.age,
                "sex": user.sex
            }
            data.append(json_data)
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def del_user(request):
    if request.method == 'POST':
        id = request.POST.get('userid')
        try:
            user = Users.objects.get(id=id)
        except:
            print("In user_ctrl/del_user: no such user")
            return JsonResponse({'errno': 1007, 'msg': "用户不存在"})
        else:
            user.delete()
            return JsonResponse({'errno': 0, 'msg': "删除成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def get_workers_info(request):
    if request.method == 'GET':
        data = []
        worker_list = Workers.objects.filter()
        for worker in worker_list:
            photo = b64encode(worker.photo).decode('utf8')
            json_data = {
                "id": worker.id,
                "username": worker.username,
                "tel": worker.tel,
                "name": worker.name,
                "photo": photo,
                "description": worker.description
            }
            data.append(json_data)
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def add_worker(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        name = request.POST.get('name')
        tel = request.POST.get('phoneNum')
        photo = request.POST.get('photo')
        description = request.POST.get('description')
        if check_worker_username(username) is not True:
            return JsonResponse({'errno': 1003, 'msg': "用户名格式错误"})
        if check_tel(tel) is not True:
            return JsonResponse({'errno': 1002, 'msg': "电话格式错误"})
        if check_password(password) is not True:
            return JsonResponse({'errno': 1009, 'msg': "密码格式错误"})
        try:
            Workers.objects.get(username=username)
        except:
            pass
        else:
            print("In user_ctrl/add_worker: worker is existed")
            return JsonResponse({'errno': 1008, 'msg': "用户已存在"})
        bytes_photo = b64decode(photo)
        new_worker = Workers(username=username, password=password, name=name,
                             tel=tel, photo=bytes_photo, description=description)
        new_worker.save()
        return JsonResponse({'errno': 0, 'msg': "添加成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})


@csrf_exempt
def del_worker(request):
    if request.method == 'POST':
        id = request.POST.get('workerid')
        try:
            worker = Workers.objects.get(id=id)
        except:
            print("In user_ctrl/del_worker: no such worker")
            return JsonResponse({'errno': 1007, 'msg': "用户不存在"})
        else:
            worker.delete()
            return JsonResponse({'errno': 0, 'msg': "删除成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
# end of 用户管理页面

