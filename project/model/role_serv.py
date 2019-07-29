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


class RoleServ(ListBase):

    def __init__(self):
        super().__init__()
        self.table_name = 'ca_role_serv'
        self.tbl_filed = ["", "role_id.role.role_name.id", "serv_id.serv.serv_name.id"]

    def get_sheet(self):
        return "角色服务关系"

    def get_type(self):
        return RoleServEntity


class RoleServEntity(EntityBase):
    """
       字典
       """

    def __init__(self):
        super(RoleServEntity, self).__init__()
        self.role_id = ""
        self.serv_id = ""
