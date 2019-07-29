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


class Application(ListBase):

    def __init__(self):
        super().__init__()
        self.table_name = 'ca_application'
        self.tbl_filed = ["", "app_code", "app_name", "app_abb", "app_view_ip", "app_view_port", "app_sevr_ip",
                          "app_sevr_port", "app_type", "default_menu", "default_skin", "remark"]

    def get_sheet(self):
        return "应用列表"

    def get_type(self):
        return ApplicationEntity


class ApplicationEntity(EntityBase):
    """
       字典
       """

    def __init__(self):
        super(ApplicationEntity, self).__init__()
        self.app_code = ""
        self.app_name = ""
        self.app_abb = ""
        self.app_view_ip = ""
        self.app_view_port = ""
        self.app_sevr_ip = ""
        self.app_sevr_port = ""
        self.app_type = ""
        self.default_menu = ""
        self.default_skin = ""


