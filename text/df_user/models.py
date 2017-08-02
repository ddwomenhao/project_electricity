#coding=utf-8
from django.db import models

# Create your models here.

class user_name(models.Model):

    username = models.CharField(max_length=20,help_text='用户名')

    password = models.CharField(max_length=40,help_text='密码')#密码需要加密,加密长度为40个字节

    email = models.EmailField(help_text='邮箱')

