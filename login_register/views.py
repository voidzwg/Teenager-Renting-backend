from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Users

# Create your views here.
@csrf_exempt  # 跨域设置
def register(request):  # 继承请求类
    if request.method == 'POST':  # 判断请求方式是否为 POST（要求POST方式）
        username = request.POST.get('username')  # 获取请求数据
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        name = request.POST.get('name')
        if password_1 != password_2:  # 若两次输入的密码不同，则返回错误码errno和描述信息msg
            return JsonResponse({'errno': 1002, 'msg': "两次输入的密码不同"})
        else:
            if not username.isalnum():
                return JsonResponse({'errno': 1003, 'msg': "用户名不合法"})
            try:
                user = Users.objects.get(username=username)
            except:
                None
            else:
                return JsonResponse({'errno': 1004, 'msg': "用户名已存在"})
            flag1=0;flag2=0;len=0;
            for a in password_1:
                len+=1
                if a.isalpha():
                    flag1 = 1
                if a.isdigit():
                    flag2 = 1
            if flag1 == 0 or flag2 == 0:
                return JsonResponse({'errno': 1005, 'msg': "密码不合法"})
            # 数据库存取：新建 Author 对象，赋值用户名和密码并保存
            new_user = Users(username=username, password=password_1, name=name)
            new_user.save()  # 一定要save才能保存到数据库中
            return JsonResponse({'errno': 0, 'msg': "注册成功"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})

@csrf_exempt  # 跨域设置
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # 获取请求数据
        password = request.POST.get('password')
        if username is None or password is None:
            return JsonResponse({'errno': 2003, 'msg': "用户名或密码为空"})
        try:
            user = Users.objects.get(username=username)
        except:
            return JsonResponse({'errno': 1006, 'msg': "用户不存在！"})
        if user.password == password:  # 判断请求的密码是否与数据库存储的密码相同
            request.session['username'] = username  # 密码正确则将用户名存储于session（django用于存储登录信息的数据库位置）
            return JsonResponse({'errno': 0, 'msg': "登录成功"})
        else:
            return JsonResponse({'errno': 1002, 'msg': "密码错误"})
    else:
        return JsonResponse({'errno': 1001, 'msg': "请求方式错误"})
