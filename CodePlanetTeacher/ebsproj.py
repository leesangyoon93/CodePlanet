# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Tbemailwhitelist(models.Model):
    clemail = models.CharField(db_column='clEmail', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbemailwhitelist'


class Tbgameinfo(models.Model):
    clid = models.IntegerField(db_column='clId')  # Field name made lowercase.
    clchapter = models.IntegerField(db_column='clChapter')  # Field name made lowercase.
    clstage = models.IntegerField(db_column='clStage')  # Field name made lowercase.
    clgrade = models.CharField(db_column='clGrade', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbgameinfo'


class Tbgamelog(models.Model):
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
        db_table = 'tbgamelog'


class Tbrank(models.Model):
    clid = models.IntegerField(db_column='clId')  # Field name made lowercase.
    clname = models.CharField(db_column='clName', max_length=255)  # Field name made lowercase.
    clrank = models.AutoField(db_column='clRank', primary_key=True)  # Field name made lowercase.
    cldate = models.IntegerField(db_column='clDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbrank'


class Tbuser(models.Model):
    clid = models.AutoField(db_column='clId', primary_key=True)  # Field name made lowercase.
    claccount = models.CharField(db_column='clAccount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clpassword = models.CharField(db_column='clPassword', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clrank = models.IntegerField(db_column='clRank', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbuser'
