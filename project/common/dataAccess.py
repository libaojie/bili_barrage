#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Comment    : 
@Time       : 2019/7/22 19:55
@Author     : libaojie
@File       : dataAccess.py
@Software   : PyCharm
"""
from project.model.application import Application
from project.model.dict import Dict
from project.model.group import Group
from project.model.menu import Menu
from project.model.menu_serv import MenuServ
from project.model.org import Org
from project.model.role import Role
from project.model.role_group import RoleGroup
from project.model.role_menu import RoleMenu
from project.model.role_serv import RoleServ
from project.model.serv import Serv
from project.model.user import User
from project.model.user_group import UserGroup


class DataAccess(object):

    def __init__(self):
        self.dict = Dict()
        self.application = Application()
        self.serv = Serv()
        self.menu = Menu()
        self.menu_serv = MenuServ()
        self.role = Role()
        self.role_menu = RoleMenu()
        self.role_serv = RoleServ()
        self.org = Org()
        self.user = User()
        self.group = Group()
        self.user_group = UserGroup()
        self.role_group = RoleGroup()

    def get(self, table, in_key, val, out_key):
        # ret = []
        if hasattr(self, table):
            data = getattr(self, table)
            if data is None:
                return None

            for item in data.items:
                if hasattr(item, in_key) and hasattr(item, out_key) and getattr(item, in_key) == val:
                    # ret.append(out_key)
                    return getattr(item, out_key)
        return None
