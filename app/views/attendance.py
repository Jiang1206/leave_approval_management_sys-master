#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, session, make_response, render_template, redirect
from app.views import attendance_blue
from app import *

# 中文注释
@attendance_blue.before_request
def check_login():
    '''
    检查用户是否已登录
    '''
    if 'role' not in session:
        # 如果用户未登录，则跳转到登录页面
        if request.path == '/attendance/':
            return redirect('/session')
        else:
            return make_response({'state': 'fail', 'msg': '请登录后操作'}, 401)
    if session.get('role').get('role') != '考勤':
        return make_response({'state': 'fail', 'msg': '非法操作, 拒绝访问'}, 403)

@attendance_blue.route('/')
def root():
    rid = request.cookies.get('rid')
    args = {}
    result = db.execute('SELECT * FROM teacher WHERE tid=?', (rid, ))
    if len(result):
        result = result[0]
        args = {
            'tid': result['tid'],
            'name': result['name'],
            'gender': result['gender'],
            'telphone': result['telphone']
        }
    else:
        args = {
            'rid': session.get('role').get('rid'),
            'name': session.get('role').get('name'),
        }
    return render_template('/attendance.html', **args)
