# coding=utf-8
from django.db import models
import copy
# 定义一个模型管理器类的抽象基类

class BaseModelManager(models.Manager):
    '''
    模型管理器类抽象基类
    '''
    def get_all_valid_fields(self):
        '''
        获取模型管理器对象所在模型类的属性列表
        '''
        # 获取模型管理器对象所在的模型类
        cls = self.model
        # 获取cls模型类的属性列表
        attr_list = cls._meta.get_all_field_names()
        return attr_list

    def create_one_object(self, **kwargs):
        '''
        往数据库中插入一条模型管理器对象所在的模型类数据
        '''
        # 获取模型管理器对象所在模型类的属性列表
        vaild_fields = self.get_all_valid_fields()
        # 拷贝kwargs
        kws = copy.copy(kwargs)

        # 去除模型类无效的属性
        #for k in kws.keys():
        for k in kws:
            if k not in vaild_fields:
                kwargs.pop(k)

        # 获取模型管理器对象所在的模型类
        cls = self.model # Passport
        obj = cls(**kwargs) # Passport(username='smart', password='123',email='smart@itcast.cn')
        # 保存进数据库
        obj.save()

        return obj

    def get_one_object(self, **filters):
        '''
        从数据库表中查出一条模型管理器对象所在模型类的数据
        '''
        try:
            obj = self.get(**filters)
        except self.model.DoesNotExist:
            obj = None
        return obj



















