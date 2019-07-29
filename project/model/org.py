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


class Org(ListBase):

    def __init__(self):
        super().__init__()
        self.table_name = 'ca_org'
        self.tbl_filed = ["", "org_code", "p_org_id.org.org_name.id", "org_name", "org_abb", "remark"]

    def get_sheet(self):
        return "组织结构"

    def get_type(self):
        return OrgEntity


class OrgEntity(EntityBase):
    """
       字典
       """

    def __init__(self):
        super(OrgEntity, self).__init__()
        self.org_code = ""
        self.p_org_id = ""
        self.org_name = ""
        self.org_abb = ""
