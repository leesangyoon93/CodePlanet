from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


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


class Tbrank(models.Model):
    clid = models.ForeignKey('Tbuser', models.DO_NOTHING, db_column='clId')  # Field name made lowercase.
    clname = models.CharField(db_column='clName', max_length=255)  # Field name made lowercase.
    clrank = models.AutoField(db_column='clRank', primary_key=True)  # Field name made lowercase.
    cldate = models.IntegerField(db_column='clDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbrank'


class Tbuser(models.Model):
    clid = models.AutoField(db_column='clId', primary_key=True)  # Field name made lowercase.
    claccount = models.CharField(db_column='clAccount', max_length=255, default="")  # Field name made lowercase.
    clpassword = models.CharField(db_column='clPassword', max_length=255, default="1234")  # Field name made lowercase.
    clrank = models.IntegerField(db_column='clRank', blank=True, null=True)  # Field name made lowercase.
    clclassroom = models.IntegerField(db_column='clClassRoom', null=True)
    clname = models.CharField(db_column='clName', null=True, max_length=255)
    clinfo = models.TextField(db_column='clInfo', null=True, max_length=255)

    class Meta:
        db_table = 'tbuser'


class TeacherManager(BaseUserManager):
    def create_user(self, email, corporation, birthday, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=TeacherManager.normalize_email(email),
            corporation=corporation,
            birthday=birthday
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, corporation, birthday, password):
        u = self.create_user(email=email,
                             corporation=corporation,
                             birthday=birthday,
                             password=password,
                             )
        u.is_admin = True
        u.save(using=self._db)
        return u


class Teacher(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    corporation = models.CharField(
        max_length=255,
        blank=False,
        default='')
    birthday = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = TeacherManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['corporation', 'birthday']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @staticmethod
    def createTeacher(email, corporation, birthday, password):
        teacher = Teacher.objects.create_user(email, corporation, birthday)
        teacher.set_password(password)
        teacher.save()
        return teacher


class ClassRoom(TimeStampedModel):
    teacher = models.ForeignKey(Teacher)
    className = models.CharField(max_length=255)
    classInfo = models.CharField(max_length=255)
    studentCount = models.IntegerField(default=0)
#
#
# class Student(TimeStampedModel):
#     classRoom = models.ForeignKey(ClassRoom)
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     extraInfo = models.TextField(max_length=255)
