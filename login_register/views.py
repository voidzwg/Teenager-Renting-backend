from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from com.funcs import *
from .models import *

# Create your views here.
@csrf_exempt  # 跨域设置
def register(request):  # 继承请求类
    if request.method == 'POST':  # 判断请求方式是否为 POST（要求POST方式）
        username = request.POST.get('username')  # 获取请求数据
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        email = request.POST.get('email')
        name = request.POST.get('name')
        if username is None or password_2 is None or password_1 is None or name is None or email is None:
            return JsonResponse({'errno': 2, 'msg': "参数不全"})
        if not check_user_username(username):
            return JsonResponse({'errno': 3, 'msg': "用户名不合法"})
        if password_1 != password_2:  # 若两次输入的密码不同，则返回错误码errno和描述信息msg
            return JsonResponse({'errno': 4, 'msg': "两次输入的密码不同"})
        try:
            user = Users.objects.get(username=username)
        except:
            None
        else:
            return JsonResponse({'errno': 5, 'msg': "用户名已存在"})
        if not check_password(password_1):
            return JsonResponse({'errno': 6, 'msg': "密码不合法"})
        if not check_email(email):
            return JsonResponse({'errno': 7, 'msg': "邮箱不合法"})
        # 数据库存取：新建 User 对象，赋值用户名和密码并保存
        new_user = Users(username=username, password=password_1, name=name, email=email)
        new_user.save()  # 一定要save才能保存到数据库中
        return JsonResponse({'errno': 0, 'msg': "注册成功"})
    else:
        return JsonResponse({'errno': 1, 'msg': "请求方式错误"})


@csrf_exempt  # 跨域设置
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # 获取请求数据
        password = request.POST.get('password')
        if username is None or password is None:
            return JsonResponse({'errno': 2, 'msg': "用户名或密码为空"})
        type = 0
        if check_user_username(username):
            type = 1
        elif check_worker_username(username):
            type = 2
        elif check_admin_username(username):
            type = 3
        if type == 0:
            return JsonResponse({'errno': 3, 'msg': "用户名不合法"})
        try:
            if type == 1:
                user = Users.objects.get(username=username)
            elif type == 2:
                worker = Workers.objects.get(username=username)
            elif type == 3:
                admin = Admins.objects.get(username=username)
        except:
            return JsonResponse({'errno': 4, 'msg': "用户不存在！"})
        if type == 1:
            if user.password == password:  # 判断请求的密码是否与数据库存储的密码相同
                return JsonResponse({'errno': 0, 'msg': "登录成功",'id':user.id,'type':type})
            else:
                return JsonResponse({'errno': 5, 'msg': "密码错误"})
        elif type == 2:
            if worker.password == password:  # 判断请求的密码是否与数据库存储的密码相同
                return JsonResponse({'errno': 0, 'msg': "登录成功",'id':worker.id,'type':type})
            else:
                return JsonResponse({'errno': 5, 'msg': "密码错误"})
        elif type == 3:
            if admin.password == password:  # 判断请求的密码是否与数据库存储的密码相同
                return JsonResponse({'errno': 0, 'msg': "登录成功", 'id': admin.id, 'type': type})
            else:
                return JsonResponse({'errno': 5, 'msg': "密码错误"})
    else:
        return JsonResponse({'errno': 1, 'msg': "请求方式错误"})
