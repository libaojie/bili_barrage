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


class Menu(ListBase):

    def __init__(self):
        super().__init__()
        self.table_name = 'ca_menu'
        self.tbl_filed = ["", "app_id.application.app_name.id", "p_menu_id.menu.menu_name.id", "menu_code", "menu_name",
                          "menu_url", "menu_type", "func_tag", "menu_fcode", "menu_fname", "menu_level", "other_func_tag", "remark"]

    def get_sheet(self):
        return "菜单列表"

    def get_type(self):
        return MenuEntity


class MenuEntity(EntityBase):
    """
       字典
       """

    def __init__(self):
        super(MenuEntity, self).__init__()
        self.app_id = ""
        self.p_menu_id = ""
        self.menu_code = ""
        self.menu_name = ""
        self.menu_url = ""
        self.menu_type = ""
        self.func_tag = ""
        self.menu_fcode = ""
        self.menu_fname = ""
        self.menu_level = ""
        self.other_func_tag = ""
