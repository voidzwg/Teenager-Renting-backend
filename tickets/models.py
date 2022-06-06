# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Tickets(models.Model):
    wid = models.ForeignKey('Workers', models.DO_NOTHING, db_column='wid', blank=True, null=True)
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    hid = models.ForeignKey('Houses', models.DO_NOTHING, db_column='hid')
    info = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    materials_pic = models.TextField(blank=True, null=True)
    materials_text = models.TextField(blank=True, null=True)
    comment = models.IntegerField(blank=True, null=True)
    pictures = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickets'


class Users(models.Model):
    username = models.CharField(max_length=18)
    password = models.CharField(max_length=18)
    avatar = models.TextField(blank=True, null=True)
    tel = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


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
