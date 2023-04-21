#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.classes import User

# 中文注释
class Role(User):
    # 初始化函数，用于初始化一个Role对象
    def __init__(self, name, password, rid, role):
        # 调用父类的构造函数
        super().__init__(name, password)
        # 将rid赋值给__rid
        self.__rid = rid
        # 将role赋值给__role
        self.__role = role

    # 获取rid属性
    @property
    def rid(self):
        # 返回__rid
        return self.__rid

    # 设置rid属性
    @rid.setter
    def rid(self, rid):
        # 判断rid是否为自然数，若不是则抛出TypeError异常
        if not isinstance(rid, int) or rid < 0:
            raise TypeError('类型错误: rid 必须为自然数.')
        # 将rid赋值给__rid
        self.__rid = rid
        # 返回self
        return self

    # 获取role属性
    @property
    def role(self):
        # 返回__role
        return self.__role

    # 设置role属性
    @role.setter
    def role(self, role):
        # 判断role是否为学生、辅导员、教务处、考勤人员、管理员，若不是则抛出TypeError异常
        if role not in ('学生', '辅导员', '教务处', '考勤人员', '管理员'):
            raise TypeError('类型错误: role 必须为 [学生|辅导员|教务处|考勤人员|管理员].')
        # 将role赋值给__role
        self.__role = role
        # 返回self
        return self