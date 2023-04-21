#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash

# 你
class User:
    """ 用户类 """
    def __init__(self, name, password):
        # 初始化用户
        if not name or not password:
            raise ValueError('值错误: 用户名和密码不能为空.')
        self.__id = -1
        self.__name = str(name)
        self.__password = str(password)
        self.__hash_password = generate_password_hash(self.__password)[21:]

    @property
    def id(self):
        # 获取用户id
        return self.__id

    @id.setter
    def id(self, id):
        # 设置用户id
        if not isinstance(id, int):
            try:
                id = int(id)
            except:
                raise TypeError(f'类型错误: id 必须为自然数 (id={id}).')
        if id < 0:
            raise TypeError('类型错误: id 必须大于 0.')
        self.__id = id
        return self

    @property
    def name(self):
        # 获取用户名
        return self.__name

    @name.setter
    def name(self, name):
        # 设置用户名
        if not name:
            raise ValueError('值错误: 用户名不能为空.')
        self.__name = str(name)
    @property
    # 注释
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        # 如果密码为空，抛出ValueError异常
        if not password:
            raise ValueError('值错误: 密码不能为空.')
        # 将密码转换为字符串
        self.__password = str(password)
        # 生成密码的hash值
        self.__hash_password = generate_password_hash(self.__password)[21:]

    @property
    def hash_password(self):
        return self.__hash_password

    # 检查密码是否正确
    def check_password(self, pwhash):
        # 检查密码的hash值是否正确
        return check_password_hash(f'pbkdf2:sha256:260000${pwhash}', self.__password)