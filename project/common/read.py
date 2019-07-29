#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Comment    : 
@Time       : 2019/7/22 19:53
@Author     : libaojie
@File       : read.py
@Software   : PyCharm
"""
import xlrd

from project import config
from project.common.engine import Engine
from project.plugin.log_tool import LogTool
from project.plugin.utils import Utils


class Read(object):

    def __init__(self):
        pass

    def run(self):
        _excel = xlrd.open_workbook(Utils.get_path(config.ExcelPath))
        if not _excel:
            LogTool.error(f"文件路径不正确！{config.ExcelPath}")
            return False

        Utils.clear_code(config.OutPath)
        Engine.dataAccess.dict.handle(_excel)
        Engine.dataAccess.application.handle(_excel)
        Engine.dataAccess.serv.handle(_excel)
        Engine.dataAccess.menu.handle(_excel)
        Engine.dataAccess.menu_serv.handle(_excel)
        Engine.dataAccess.role.handle(_excel)
        Engine.dataAccess.role_menu.handle(_excel)
        Engine.dataAccess.role_serv.handle(_excel)
        Engine.dataAccess.org.handle(_excel)
        Engine.dataAccess.user.handle(_excel)
        Engine.dataAccess.group.handle(_excel)
        Engine.dataAccess.user_group.handle(_excel)
        Engine.dataAccess.role_group.handle(_excel)
        LogTool.print("----")
        return True






