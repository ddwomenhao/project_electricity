# coding=utf-8
from django.db import models
from db.base_model import BaseModel # 导入抽象模型类
from db.base_manager import BaseModelManager # 导入抽象模型管理器类
from utils.get_hash import get_hash
# Create your models here.

class PassportManager(BaseModelManager):
    '''
    账户模型管理器类
    '''
    def add_one_passport(self, username, password, email):
        '''
        添加一个账户信息
        '''
        obj = self.create_one_object(username=username, password=password, email=email)
        return obj

    def get_one_passport(self, username, password=None):
        '''
        根据用户名和密码查找账户信息
        '''
        if password:
            obj = self.get_one_object(username=username, password=password)
        else:
            obj = self.get_one_object(username=username)
        return obj

'''
class PassportManager(models.Manager):
    #账户模型管理器类
    def add_one_passport(self, username, password, email):
        #添加一个账户信息
        # 获取模型管理器对象所在模型类的名字
        cls = self.model
        obj = cls()
        # 给obj对象创建对象属性并赋值
        obj.username = username
        obj.password = get_hash(password)
        obj.email = email
        # 保存进数据库
        obj.save()
        return obj

    def get_one_passport(self, username, password=None):
        #根据用户名和密码查找账户信息
        try:
            if password:
                # 根据用户名和密码来查
                obj = self.get(username=username, password=get_hash(password))
            else:
                # 只根据用户名来查
                obj = self.get(username=username)
        except self.model.DoesNotExist:
            obj=None
        return obj
'''
'''
class BookInfoManager(BaseModelManager):
    图书模型管理器类
    def add_one_book(self, atitle):
        obj = self.create_one_object(atitle=atitle)
        return obj


class BookInfo(BaseModel):
    atitle = models.CharField(max_length=20, help_text='图书标题')
    objects = BookInfoManager()
'''

'''
class AddressManger(BaseModelManager):
    #地址模型管理器类
    def add_one_address(self, recipicent_name):
        #添加一个地址信息
        obj = self.create_one_object(recipicent_name=recipicent_name)
        return obj

class Address(BaseModel):
    #地址类
    recipicent_name = models.CharField(max_length=20, help_text='收件人')

    objects = AddressManger()

Address.objects.add_one_address(recipicent_name='smart')
'''

class Passport(BaseModel):
    '''
    账户类
    '''
    username = models.CharField(max_length=20, help_text='用户名')
    password = models.CharField(max_length=40, help_text='密码')
    email = models.EmailField(help_text='邮箱')

    '''
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    '''

    # 创建一个自定义模型管理器的对象
    objects = PassportManager()

    class Meta:
        db_table = 's_user_account'