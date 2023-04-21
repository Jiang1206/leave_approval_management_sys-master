#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

class Datetime:
    @staticmethod
    def diff(minuend, minus, format=r'%Y-%m-%d %H:%M:%S'):
        return datetime.strptime(minuend, format) - datetime.strptime(minus, format)
    # 计算两个时间的时间差
    # 参数 minuend：被减数，minus：减数，format：时间格式，默认为 r'%Y-%m-%d %H:%M:%S'

    @staticmethod
    def year(dt, format=r'%Y-%m-%d %H:%M:%S'):
        return datetime.strptime(dt, format).year
    # 返回时间的年份
    # 参数 dt：时间，format：时间格式，默认为 r'%Y-%m-%d %H:%M:%S'

    @staticmethod
    def month(dt, format=r'%Y-%m-%d %H:%M:%S'):
        return datetime.strptime(dt, format).month
    # 返回时间的月份
    # 参数 dt：时间，format：时间格式，默认为 r'%Y-%m-%d %H:%M:%S'

    @staticmethod
    def day(dt, format=r'%Y-%m-%d %H:%M:%S'):
        return datetime.strptime(dt, format).day
    # 返回时间的日
    # 参数 dt：时间，format：时间格式，默认为 r'%Y-%m-%d %H:%M:%S'

    @staticmethod
    def hour(dt, format=r'%Y-%m-%d %H:%M:%S'):
        return datetime.strptime(dt, format).hour
    # 返回时间的小时
    # 参数 dt：时间，format：时间格式，默认为 r'%Y-%m-%d %H:%M:%S'

    @staticmethod
    def minute(dt, format=r'%Y-%m-%d %H:%M:%S'):
        return datetime.strptime(dt, format).minute
    # 返回时间的分钟
    # 参数 dt：时间，format：时间格式，默认为 r'%Y-%m-%d %H:%M:%S'

    @staticmethod
    def second(dt, format=r'%Y-%m-%d %H:%M:%S'):
        return datetime.strptime(dt, format).second
    # 返回时间的秒数
    # 参数 dt：时间，format：时间格式，默认为 r'%Y-%m-%d %H:%M:%S'
