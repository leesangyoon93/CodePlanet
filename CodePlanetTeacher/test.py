# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class MainsClassroom(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    classname = models.CharField(db_column='className', max_length=255)  # Field name made lowercase.
    classinfo = models.CharField(db_column='classInfo', max_length=255)  # Field name made lowercase.
    studentcount = models.IntegerField(db_column='studentCount')  # Field name made lowercase.
    teacher = models.ForeignKey('MainsTeacher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mains_classroom'


class MainsTeacher(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    corporation = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    is_active = models.IntegerField()
    is_admin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mains_teacher'


class Tbemailwhitelist(models.Model):
    clemail = models.CharField(db_column='clEmail', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbemailwhitelist'


class Tbgameinfo(models.Model):
    clidx = models.AutoField(db_column='clIdx', primary_key=True)  # Field name made lowercase.
    clid = models.ForeignKey('Tbuser', models.DO_NOTHING, db_column='clId')  # Field name made lowercase.
    clchapter = models.IntegerField(db_column='clChapter')  # Field name made lowercase.
    clstage = models.IntegerField(db_column='clStage')  # Field name made lowercase.
    clgrade = models.CharField(db_column='clGrade', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbgameinfo'


class Tbgameinfo2(models.Model):
    clid = models.IntegerField(db_column='clId')  # Field name made lowercase.
    clchapter = models.IntegerField(db_column='clChapter')  # Field name made lowercase.
    clstage = models.IntegerField(db_column='clStage')  # Field name made lowercase.
    clgrade = models.CharField(db_column='clGrade', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbgameinfo2'


class Tbgamelog(models.Model):
    clidx = models.AutoField(db_column='clIdx', primary_key=True)  # Field name made lowercase.
    clid = models.ForeignKey('Tbuser', models.DO_NOTHING, db_column='clId')  # Field name made lowercase.
    clchapter = models.IntegerField(db_column='clChapter')  # Field name made lowercase.
    clstage = models.IntegerField(db_column='clStage')  # Field name made lowercase.
    cltime = models.IntegerField(db_column='clTime')  # Field name made lowercase.
    clgrade = models.IntegerField(db_column='clGrade')  # Field name made lowercase.
    clcommands = models.IntegerField(db_column='clCommands')  # Field name made lowercase.
    cltrying = models.IntegerField(db_column='clTrying')  # Field name made lowercase.
    clerror = models.IntegerField(db_column='clError')  # Field name made lowercase.
    clcode = models.TextField(db_column='clCode')  # Field name made lowercase.
    cldisable = models.IntegerField(db_column='clDisable')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbgamelog'


class Tbgamelog2(models.Model):
    clid = models.IntegerField(db_column='clId')  # Field name made lowercase.
    clchapter = models.IntegerField(db_column='clChapter')  # Field name made lowercase.
    clstage = models.IntegerField(db_column='clStage')  # Field name made lowercase.
    cltime = models.IntegerField(db_column='clTime')  # Field name made lowercase.
    clgrade = models.IntegerField(db_column='clGrade')  # Field name made lowercase.
    clcommands = models.IntegerField(db_column='clCommands')  # Field name made lowercase.
    cltrying = models.IntegerField(db_column='clTrying')  # Field name made lowercase.
    clerror = models.IntegerField(db_column='clError')  # Field name made lowercase.
    clcode = models.TextField(db_column='clCode')  # Field name made lowercase.
    cldisable = models.IntegerField(db_column='clDisable')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbgamelog2'


class Tbrank(models.Model):
    clid = models.ForeignKey('Tbuser', models.DO_NOTHING, db_column='clId')  # Field name made lowercase.
    clname = models.CharField(db_column='clName', max_length=255)  # Field name made lowercase.
    clrank = models.AutoField(db_column='clRank', primary_key=True)  # Field name made lowercase.
    cldate = models.IntegerField(db_column='clDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbrank'


class Tbrank2(models.Model):
    clid = models.IntegerField(db_column='clId', blank=True, null=True)  # Field name made lowercase.
    clname = models.CharField(db_column='clName', max_length=255)  # Field name made lowercase.
    clrank = models.AutoField(db_column='clRank', primary_key=True)  # Field name made lowercase.
    cldate = models.IntegerField(db_column='clDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbrank2'


class Tbuser(models.Model):
    clid = models.AutoField(db_column='clId', primary_key=True)  # Field name made lowercase.
    claccount = models.CharField(db_column='clAccount', max_length=255)  # Field name made lowercase.
    clpassword = models.CharField(db_column='clPassword', max_length=255)  # Field name made lowercase.
    clrank = models.IntegerField(db_column='clRank', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbuser'


class Tbuser2(models.Model):
    clid = models.AutoField(db_column='clId', primary_key=True)  # Field name made lowercase.
    claccount = models.CharField(db_column='clAccount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clpassword = models.CharField(db_column='clPassword', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clrank = models.IntegerField(db_column='clRank', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbuser2'
