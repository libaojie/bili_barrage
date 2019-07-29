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


class User(ListBase):

    def __init__(self):
        super().__init__()
        self.table_name = 'ca_user'
        self.tbl_filed = ["", "user_code", "user_name", "login_name", "org_id.org.org_name.id", "email", "mobile",
                          "password",
                          "remark"]

    def get_sheet(self):
        return "用户列表"

    def get_type(self):
        return UserEntity


class UserEntity(EntityBase):
    """
       字典
       """

    def __init__(self):
        super(UserEntity, self).__init__()
        self.user_code = ""
        self.user_name = ""
        self.login_name = ""
        self.org_id = ""
        self.email = ""
        self.mobile = ""
        self.password = ""
