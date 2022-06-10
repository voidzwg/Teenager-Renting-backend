from __future__ import absolute_import, unicode_literals
from teen_renting.celery import app
from celery import shared_task
from datetime import datetime, timedelta, timezone
from time import time, sleep
from dateutil.relativedelta import relativedelta  # pip install python-dateutil
from .models import Orders
from com.funcs import my_send_email

tz = timezone(timedelta(hours=+8))


@shared_task
def auto_update_paid():
    now_date = datetime.fromtimestamp(int(time()), tz=tz)
    orders_list = Orders.objects.filter(status=1, type=1)
    for order in orders_list:
        n = order.duration
        i = 1
        start = order.start_time
        end = start + relativedelta(months=n)
        if start <= now_date <= end:
            while i <= n:
                if now_date == start + relativedelta(months=i):
                    order.paid = 0
                    print("Set " + str(order.uid.name) +
                          "'s order to unpaid in the No." + str(n) + " month")
                    order.save()
                    return
                i += 1
            print("Not " + str(order.uid.name) + "'s pay day")


@shared_task
def send_email():
    now_date = datetime.fromtimestamp(int(time()), tz=tz)
    orders_list = Orders.objects.filter(status=1, type=1)
    for order in orders_list:
        n = order.duration
        i = 0
        start = order.start_time
        end = start + relativedelta(months=n)
        if start <= now_date <= end:
            while i < n:
                if now_date == start + relativedelta(months=i) + relativedelta(weeks=3)\
                        and order.paid == 0:
                    my_send_email([order.uid.email])
                    return
                i += 1


@shared_task
def test(x):
    print("this is a test", x)
    return "this is a test " + str(x)


@shared_task
def test_beat(string):
    print("this is a test", string)

