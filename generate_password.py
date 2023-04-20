#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash,check_password_hash

if __name__ == '__main__':
    pwd = input('请输入明文密码: ')
    hash_pwd = generate_password_hash(pwd)[21:]
    print('加密后的密码为: ')
    print(hash_pwd)

# 验证加密的密码是否正确
#     hash_pwd = 'tw4jUrbPxULDDlCD$7f4ba50da2856741786e855b43955600f44303e2f935a0b7f7e5f46ad5e7c5ef'
#     check_pwd = check_password_hash(f'pbkdf2:sha256:260000${hash_pwd}','123456')
#     print('密码是否正确: ')
#     print(check_pwd)