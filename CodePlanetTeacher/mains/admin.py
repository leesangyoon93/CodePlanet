from django.contrib import admin

# Register your models here.
from mains.models import *
from django.contrib.auth.models import Group


admin.site.register(Tbemailwhitelist)
admin.site.register(Tbgameinfo)
admin.site.register(Tbgamelog)
admin.site.register(Tbrank)
admin.site.register(Tbuser)
admin.site.register(Teacher)
admin.site.unregister(Group)
