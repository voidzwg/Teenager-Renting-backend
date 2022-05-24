# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admins(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=18)
    password = models.CharField(max_length=18)

    class Meta:
        managed = False
        db_table = 'admins'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Carts(models.Model):
    id = models.ForeignKey('Houses', models.DO_NOTHING, db_column='id')
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    duration = models.IntegerField()
    amount = models.FloatField()
    details = models.TextField(blank=True, null=True)

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
