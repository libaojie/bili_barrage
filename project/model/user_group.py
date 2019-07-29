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


class UserGroup(ListBase):

    def __init__(self):
        super().__init__()
        self.table_name = 'ca_user_grp'
        self.tbl_filed = ["", "grp_id.group.grp_name.id", "user_id.user.user_name.id"]

    def get_sheet(self):
        return "用户用户组关系"

    def get_type(self):
        return UserGroupEntity


class UserGroupEntity(EntityBase):
    """
       字典
       """

    def __init__(self):
        super(UserGroupEntity, self).__init__()
        self.grp_id = ""
        self.user_id = ""
