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


class Role(ListBase):

    def __init__(self):
        super().__init__()
        self.table_name = 'ca_role'
        self.tbl_filed = ["", "app_id.application.app_name.id", "role_code", "role_name", "remark"]

    def get_sheet(self):
        return "角色列表"

    def get_type(self):
        return RoleEntity


class RoleEntity(EntityBase):
    """
       字典
       """

    def __init__(self):
        super(RoleEntity, self).__init__()
        self.app_id = ""
        self.role_code = ""
        self.role_name = ""
