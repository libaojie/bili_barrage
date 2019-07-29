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


class RoleMenu(ListBase):

    def __init__(self):
        super().__init__()
        self.table_name = 'ca_role_menu'
        self.tbl_filed = ["", "role_id.role.role_name.id", "menu_id.menu.menu_fname.id"]

    def get_sheet(self):
        return "角色菜单关系"

    def get_type(self):
        return RoleMenuEntity


class RoleMenuEntity(EntityBase):
    """
       字典
       """

    def __init__(self):
        super(RoleMenuEntity, self).__init__()
        self.menu_id = ""
        self.role_id = ""
