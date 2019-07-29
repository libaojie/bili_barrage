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


class RoleGroup(ListBase):

    def __init__(self):
        super().__init__()
        self.table_name = 'ca_grp_role'
        self.tbl_filed = ["", "grp_id.group.grp_name.id", "role_id.role.role_name.id"]

    def get_sheet(self):
        return "角色用户组关系"

    def get_type(self):
        return RoleGroupEntity


class RoleGroupEntity(EntityBase):
    """
       字典
       """

    def __init__(self):
        super(RoleGroupEntity, self).__init__()
        self.grp_id = ""
        self.role_id = ""
