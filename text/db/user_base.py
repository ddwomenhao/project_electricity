#coding=utf-8
from django.db import models

class Base(models.Model):

    creat_time = models.DateTimeField(auto_now_add=True,help_text='创建的时间')

    updae_time = models.DateTimeField(auto_now=True,help_text='更新时间')

    isdelete = models.BooleanField(default=False)
