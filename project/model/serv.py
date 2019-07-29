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


class Serv(ListBase):

    def __init__(self):
        super().__init__()
        self.table_name = 'ca_service'
        self.tbl_filed = ["", "app_id.application.app_name.id", "serv_code", "serv_name", "serv_url", "request_type",
                          "remark"]

    def get_sheet(self):
        return "服务列表"

    def get_type(self):
        return ServEntity


class ServEntity(EntityBase):
    """
       字典
       """

    def __init__(self):
        super(ServEntity, self).__init__()
        self.app_id = ""
        self.serv_code = ""
        self.serv_name = ""
        self.serv_url = ""
        self.request_type = ""
