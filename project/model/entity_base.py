#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Comment    : 
@Time       : 2019/7/22 19:43
@Author     : libaojie
@File       : entity_base.py
@Software   : PyCharm
"""
import datetime
from enum import Enum

from project.common.engine import Engine
from project.plugin.utils import Utils


class EnumDelFlag(Enum):
    """
    是否删除枚举
    """
    # 全部
    all = None
    view = '0'
    delete = '1'


class EntityBase(object):
    """
    实体表基类
    """

    def __init__(self, remark=''):
        self.id = Utils.get_uuid()
        self.del_flag = EnumDelFlag.view.value
        self.create_time = Utils.get_currer_time()
        self.update_time = Utils.get_currer_time()
        self.remark = remark
        self.create_user = ''
        self.update_user = ''

    def get_key(self):
        pass

    def get_value(self, key):
        if key == "":
            return None

        if not hasattr(self, key):
            return None

        val = getattr(self, key)

        if val is None:
            return "null"
        elif isinstance(val, datetime.datetime):
            return f"to_date('{val.strftime('%Y-%m-%d %H:%M:%S')}', 'yyyy-mm-dd hh24:mi:ss')"
        else:
            return f"'{val}'"

    def get_sql(self, field, table_name):
        """
        保存用户
        :return:
        """
        param = ','.join([self.get_value(v) for v in field if hasattr(self, v)])

        field = [k.split('.')[0] for k in field]
        sql = f"insert into {table_name} ({','.join(field)}) values ({param});"
        return sql
