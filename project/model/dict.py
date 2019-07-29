#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Comment    : 
@Time       : 2018/11/14 9:33
@Author     : libaojie
@File       : session.py
@Software   : PyCharm
"""

from project.model.entity_base import EntityBase
from project.model.list_base import ListBase


class Dict(ListBase):

    def __init__(self):
        super().__init__()
        self.table_name = 'ca_dict'
        self.tbl_filed = ["", "dict_code", "dict_name", "dict_key", "dict_val", "remark"]

    def get_sheet(self):
        return "数据字典"

    def get_type(self):
        return DictEntity


class DictEntity(EntityBase):
    """
       字典
       """

    def __init__(self):
        super(DictEntity, self).__init__()
        self.dict_code = ""
        self.dict_name = ""
        self.dict_key = ""
        self.dict_val = ""
        self.is_sys_parm = ""
