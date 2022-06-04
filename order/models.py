# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from base64 import b64encode

from django.db import models
from django.http import JsonResponse

class Users(models.Model):
    username = models.CharField(max_length=18)
    password = models.CharField(max_length=18)
    tel = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Houses(models.Model):
    short_price = models.FloatField()
    long_price = models.FloatField()
    location = models.CharField(max_length=254, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    available = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    floor_plan = models.TextField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'houses'


class Orders(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    hid = models.ForeignKey(Houses, models.DO_NOTHING, db_column='hid')
    type = models.IntegerField(blank=True, null=True)
    paid = models.IntegerField(blank=True, null=True)
    order_time = models.DateTimeField()
    start_time = models.DateTimeField()
    duration = models.IntegerField()
    amount = models.FloatField()
    details = models.TextField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orders'

def order_serialize(order_list):
    data = []
    for i in order_list:
        try:
            picture = b64encode(i.hid.pictures).decode('utf8')
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