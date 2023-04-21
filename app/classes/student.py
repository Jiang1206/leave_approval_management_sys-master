#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.classes import User

# 中文
class Student(User):
    # 定义Student类，继承自User类
    def __init__(self, name, password, sid, tid='', gender='', department='', faculty='', major='', grade='', _class=''):
        # 初始化Student类，继承自User类
        super().__init__(name, password)
        # 将sid赋值给Student类的sid属性
        self.__sid = sid
        # 将tid赋值给Student类的tid属性
        self.tid= tid
        # 将gender赋值给Student类的gender属性
        self.gender = gender
        # 将department赋值给Student类的department属性
        self.department = department
        # 将faculty赋值给Student类的faculty属性
        self.faculty = faculty
        # 将major赋值给Student类的major属性
        self.major = major
        # 将grade赋值给Student类的grade属性
        self.grade = grade
        # 将_class赋值给Student类的_class属性
        self._class  = _class

    # 获取sid属性
    @property
    def sid(self):
        # 返回sid属性
        return self.__sid

    # 设置sid属性
    @sid.setter
    def sid(self, sid):
        # 判断sid属性的类型是否为自然数或者小于0
        if not isinstance(sid, int) or sid < 0:
            # 如果不是，抛出TypeError异常
            raise TypeError('类型错误: sid 必须为自然数.')
        # 将sid属性赋值给Student类的sid属性
        self.__sid = sid
        # 返回Student类
        return self