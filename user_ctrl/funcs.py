import re


def check_info(tel, email):
    if tel == "" and email == "":
        return 3
    if check_tel(tel) is not True:
        return 1
    if check_email(email) is not True:
        return 2

    return 0


def check_tel(tel):
    if tel == "":
        return True
    if tel.isalnum() and len(tel) == 11:
        return True
    return False


def check_email(email):
    if email == "":
        return True
    ex_email = re.compile(r'^[\w]+@[\w.]+[com|net|cn]')
    result = ex_email.match(email)
    if result:
        return True
    return False


def check_age(age):
    if age.isalnum():
        num_age = int(age)
        if 0 <= num_age <= 125:
            return True
    return False


def check_sex(sex):
    if sex.isalnum():
        num_sex = int(sex)
        if num_sex == 1 or num_sex == 0:
            return True
    return False


def check_user_username(username):
    ex_username = re.compile(r'^[\w]+\Z')
    result = ex_username.match(username)
    if result:
        return True
    else:
        return False


def check_worker_username(username):
    ex_username = re.compile(r'^#[\w]+\Z')
    result = ex_username.match(username)
    if result:
        return True
    else:
        return False


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

