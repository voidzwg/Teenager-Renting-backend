# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import io
from base64 import b64encode

from PIL import Image
from django.db import models
from django.http import JsonResponse


class Admins(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=18)
    password = models.CharField(max_length=18)

    class Meta:
        managed = False
        db_table = 'admins'

class Carts(models.Model):
    hid = models.ForeignKey('Houses', models.DO_NOTHING, db_column='hid')
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'carts'


class Complaints(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    tid = models.ForeignKey('Tickets', models.DO_NOTHING, db_column='tid')
    contents = models.TextField()
    pictures = models.TextField(blank=True, null=True)
    reply = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaints'


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
def house_serialize(house_list):
    data = []
    for i in house_list:
        picture = b64encode(i.pictures).decode('utf8')
        floor_plan = b64encode(i.floor_plan).decode('utf8')
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

class Orders(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    hid = models.ForeignKey(Houses, models.DO_NOTHING, db_column='hid')
    type = models.IntegerField(blank=True, null=True)
    paid = models.IntegerField(blank=True, null=True)
    order_time = models.DateTimeField()
    duration = models.IntegerField()
    amount = models.FloatField()
    details = models.TextField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orders'


class Tickets(models.Model):
    wid = models.ForeignKey('Workers', models.DO_NOTHING, db_column='wid', blank=True, null=True)
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    hid = models.ForeignKey(Houses, models.DO_NOTHING, db_column='hid')
    info = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    comment = models.IntegerField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickets'


class Users(models.Model):
    username = models.CharField(max_length=18)
    password = models.CharField(max_length=18)
    tel = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    avatar = models.TextField()

    class Meta:
        managed = False
        db_table = 'users'

def user_serialize(user_list):
    i = user_list
    picture = b64encode(i.avatar).decode('utf8')
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

class Workers(models.Model):
    username = models.CharField(max_length=18)
    password = models.CharField(max_length=18)
    name = models.CharField(max_length=30)
    tel = models.CharField(max_length=11, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workers'
