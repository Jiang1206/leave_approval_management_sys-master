#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.classes import User

# 在
class Teacher(User):
    # 初始化类
    def __init__(self, name, password, tid, gender='', telphone=''):
        # 调用父类的构造函数
        super().__init__(name, password)
        # 将tid赋值给类变量
        self.__tid = tid
        # 将gender赋值给类变量
        self.gender = gender
        # 将telphone赋值给类变量
        self.telphone = telphone

    # 获取tid
    @property
    def tid(self):
        # 返回tid
        return self.__tid

    # 设置tid
    @tid.setter
    def tid(self, tid):
        # 判断tid的类型是否为自然数或者小于0
        if not isinstance(tid, int) or tid < 0:
            # 如果不是，抛出类型错误
            raise TypeError('类型错误: tid 必须为自然数.')
        # 将tid赋值给类变量
        self.__tid = tid
        # 返回self
        return self