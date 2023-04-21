#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 导入必要的库
from os import path
import sqlite3

# 数据库封装类
class Database:
    """ 封装数据库操作 """
    last_error = ''

    # 实现单例模式
    def __new__(cls, *arg, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self, db_path):
        # 检查数据库文件路径是否存在
        if not path.isfile(db_path):
            raise ValueError(f'无效的数据库文件路径({db_path}).')
        self.db_path = db_path

    def execute(self, sql, args=()):
        # 连接数据库
        connection = sqlite3.connect(self.db_path)
        result = None
        try:
            if sql[:6].lower() == 'select':
                # 设定返回的数据类型为字典
                connection.row_factory = sqlite3.Row
                result = connection.execute(sql, args).fetchall()
            if sql[:6].lower() in ('insert', 'delete', 'update'):
                with connection:
                    # 执行非查询操作，返回影响行数
                    result = connection.execute(sql, args).rowcount
        except sqlite3.IntegrityError as e:
            Database.last_error = e
            result = None
        except sqlite3.Error as e:
            Database.last_error = e
            raise e
        finally:
            # 关闭数据库连接
            connection.close()
        return result

    def executemany(self, sql, args=()):
        # 连接数据库
        connection = sqlite3.connect(self.db_path)
        result = None
        try:
            if sql[:6].lower() == 'select':
                # 设定返回的数据类型为字典
                connection.row_factory = sqlite3.Row
                result = connection.executemany(sql, args).fetchall()
            if sql[:6].lower() in ('insert', 'delete', 'update'):
                with connection:
                    # 执行非查询操作，返回影响行数
                    result = connection.executemany(sql, args).rowcount
        except sqlite3.IntegrityError as e:
            Database.last_error = e
            result = None
        except sqlite3.Error as e:
            Database.last_error = e
            raise e
        finally:
            # 关闭数据库连接
            connection.close()
        return result
