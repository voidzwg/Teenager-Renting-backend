import re


# 检查电话和邮箱格式
# 两者均为空字符串返回3
# 电话不合法返回1
# 邮箱不合法返回2
# 合法返回0
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

