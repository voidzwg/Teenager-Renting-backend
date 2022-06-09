import logging
from celery import shared_task
from datetime import datetime, timedelta, timezone
from time import time
from dateutil.relativedelta import relativedelta  # pip install python-dateutil
from .models import Orders

logger = logging.getLogger()
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
        pass

