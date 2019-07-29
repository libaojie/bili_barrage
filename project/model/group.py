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


class Group(ListBase):

    def __init__(self):
        super().__init__()
        self.table_name = 'ca_group'
        self.tbl_filed = ["", "grp_code", "grp_name", "remark"]

    def get_sheet(self):
        return "用户组"

    def get_type(self):
        return GroupEntity


class GroupEntity(EntityBase):
    """
       字典
       """

    def __init__(self):
        super(GroupEntity, self).__init__()
        self.grp_code = ""
        self.grp_name = ""
