import re
from datetime import datetime, timezone, timedelta


# 检查电话和邮箱格式
# 两者均为空字符串返回3
# 电话不合法返回1
# 邮箱不合法返回2
# 合法返回0
from django.http import JsonResponse


def check_info(tel, email):
    if tel == "" and email == "":
        return 3
    if check_tel(tel) is not True:
        return 1
    if check_email(email) is not True:
        return 2

    return 0


# 检查电话格式
# 空字符串和11位纯数字合法，返回True
# 其他情况非法，返回False
def check_tel(tel):
    if tel == "":
        return True
    if tel.isalnum() and len(tel) == 11:
        return True
    return False


# 检查邮箱格式
# 空字符串合法，返回True
def check_email(email):
    if email == "":
        return True
    ex_email = re.compile(r'^[\w]+@[\w.]+[com|net|cn]')
    result = ex_email.match(email)
    if result:
        return True
    return False


# 检查年龄
# 0-125合法，返回True
def check_age(age):
    if age.isalnum():
        num_age = int(age)
        if 0 <= num_age <= 125:
            return True
    return False


# 检查性别
# 1和0合法，返回True
def check_sex(sex):
    if sex.isalnum():
        num_sex = int(sex)
        if num_sex == 1 or num_sex == 0:
            return True
    return False


# 检查用户的username
# 仅由字母数字下划线组成为合法，返回True
def check_user_username(username):
    ex_username = re.compile(r'^[\w]+\Z')
    result = ex_username.match(username)
    if result:
        return True
    else:
        return False


# 检查师傅的username
# '#'加字母数字下划线为合法，返回True
def check_worker_username(username):
    ex_username = re.compile(r'^#[\w]+\Z')
    result = ex_username.match(username)
    if result:
        return True
    else:
        return False


# 检查password
# 必须包含字母和数字，否则为非法，返回False
def check_password(password):
    check_alpha = True
    check_digit = True
    for ch in password:
        if '0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            if '0' <= ch <= '9':
                check_digit = False
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                check_alpha = False
        else:
            check_alpha = check_digit = True
            break
    if check_alpha or check_digit:
        return False
    return True


# 修正从数据库中取出的图片编码字符串
#
# 传入参数：base64编码（字符串形式）
# 功能：将形如"b'base64code'"的字符串更改为"base64"的格式，其余字符串不受影响
# 传出参数：修正后的字符串
def set_b64_string(photo_spl):
    if photo_spl[0] == 'b' and photo_spl[1] == "'":
        str_list = photo_spl.split("'")
        photo = str_list[1]
    else:
        photo = photo_spl
    return photo


def house_serializes(house_list):
    data = []
    for i in house_list:
        try:
            picture = i.pictures.decode('utf8')
            picture = set_b64_string(picture)
        except:
            picture = None
        try:
            floor_plan = i.floor_plan.decode('utf8')
            floor_plan = set_b64_string(floor_plan)
        except:
            floor_plan = None
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


def house_serialize(house):
    i=house
    try:
        picture = i.pictures.decode('utf8')
        picture = set_b64_string(picture)
    except:
        picture = None
    try:
        floor_plan = i.floor_plan.decode('utf8')
        floor_plan = set_b64_string(floor_plan)
    except:
        floor_plan = None
    data = {
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
    return JsonResponse(data,safe = False)


def house_list_serialize(houses_list):
    data = []
    for house in houses_list:
        try:
            pictures = set_b64_string(house.pictures.decode('utf-8'))
        except:
            pictures = None
        try:
            floor_plan = set_b64_string(house.floor_plan.decode('utf-8'))
        except:
            floor_plan = None
        json_data = {
            "id": house.id,
            "short_price": house.short_price,
            "long_price": house.long_price,
            "area": house.area,
            "location": house.location,
            "type": house.type,
            "available": house.available,
            "floor_plan": floor_plan,
            "pictures": pictures,
            "details": house.details
        }
        data.append(json_data)
    return JsonResponse(data, safe=False)


def user_serialize(user_list):
    i = user_list
    try:
        picture = i.avatar.decode('utf8')
        picture = set_b64_string(picture)
    except:
        picture = None
    data = {
        'username': i.username,
        "avatar": picture,
        'name':i.name,
        'age':i.age,
        'sex':i.sex,
        'email':i.email,
        'tel':i.tel,
    }
    return JsonResponse(data, safe=False)


def order_serialize(order_list):
    data = []
    for i in order_list:
        try:
            picture = i.hid.pictures.decode('utf8')
            picture = set_b64_string(picture)
        except:
            picture =None
        p_tmp = {
            'oid': i.id,
            'hid': i.hid.id,
            'paid': i.paid,
            "type": i.type,
            "pictures": picture,
            'order_time': i.order_time,
            'start_time': i.start_time,
            'duration': i.duration,
            'amount': i.amount,
            'status': i.status,
            'details': i.details
        }
        data.append(p_tmp)
    return JsonResponse(data, safe=False)


def order_ctrl_serialize(order_list):
    data = []
    tz = timezone(timedelta(hours=+8))
    for i in order_list:
        start_time = i.start_time
        print(start_time.astimezone(tz))
        p_tmp = {
            'oid': i.id,
            'uid': i.uid.id,
            'hid': i.hid.id,
            'paid': i.paid,
            "type": i.type,
            'order_time': i.order_time.astimezone(tz),
            'start_time': i.start_time.astimezone(tz),
            'duration': i.duration,
            'amount': i.amount,
            'status': i.status,
            'details': i.details
        }
        data.append(p_tmp)
    return JsonResponse(data, safe=False)


def ticket_serialize(tickets_list):
    data = []
    for ticket in tickets_list:
        try:
            materials_pic = set_b64_string(ticket.materials_pic.decode("utf-8"))
        except:
            materials_pic = None
        try:
            pictures = set_b64_string(ticket.pictures.decode("utf-8"))
        except:
            pictures = None
        if ticket.wid is None:
            wid = None
        else:
            wid = ticket.wid.id
        json_data = {
            "wid": wid,
            "hid": ticket.hid.id,
            "info": ticket.info,
            "status": ticket.status,
            "date": ticket.date,
            "materials_pic": materials_pic,
            "materials_text": ticket.materials_text,
            "comment": ticket.comment,
            "pictures": pictures,
            "details": ticket.details
        }
        data.append(json_data)
    return JsonResponse(data, safe=False)


def ticket_serialize_full(tickets_list):
    data = []
    for ticket in tickets_list:
        try:
            materials_pic = set_b64_string(ticket.materials_pic.decode("utf-8"))
        except:
            materials_pic = None
        try:
            pictures = set_b64_string(ticket.pictures.decode("utf-8"))
        except:
            pictures = None
        if ticket.wid is None:
            wid = None
        else:
            wid = ticket.wid.id
        json_data = {
            'id': ticket.id,
            'uid': ticket.uid.id,
            "wid": wid,
            "hid": ticket.hid.id,
            "info": ticket.info,
            "status": ticket.status,
            "date": ticket.date,
            "materials_pic": materials_pic,
            "materials_text": ticket.materials_text,
            "comment": ticket.comment,
            "pictures": pictures,
            "details": ticket.details
        }
        data.append(json_data)
    return JsonResponse(data, safe=False)


def complaint_serialize(complaints_list):
    data = []
    for complaint in complaints_list:
        try:
            pictures = set_b64_string(complaint.pictures.decode("utf-8"))
        except:
            pictures = None
        json_data = {
            'id': complaint.id,
            'uid': complaint.uid.id,
            'tid': complaint.tid.id,
            'contents': complaint.contents,
            'pictures': pictures,
            'reply': complaint.reply
        }
        data.append(json_data)
    return JsonResponse(data, safe=False)


def sort_tickets_by_date():
    tb = ['-date']
    return tb


def sort_tickets_by_date_and_status():
    tb = ['status', '-date']
    return tb

