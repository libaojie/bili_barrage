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


class MenuServ(ListBase):

    def __init__(self):
        super().__init__()
        self.table_name = 'ca_menu_serv'
        self.tbl_filed = ["", "menu_id.menu.menu_fname.id", "serv_id.serv.serv_name.id"]

    def get_sheet(self):
        return "菜单服务关系"

    def get_type(self):
        return MenuServEntity


class MenuServEntity(EntityBase):
    """
       字典
       """

    def __init__(self):
        super(MenuServEntity, self).__init__()
        self.menu_id = ""
        self.serv_id = ""
