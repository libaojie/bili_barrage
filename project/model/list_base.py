#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Comment    : 
@Time       : 2019/7/23 8:57
@Author     : libaojie
@File       : list_base.py
@Software   : PyCharm
"""
from project import config
from project.common.engine import Engine
from project.model.entity_base import EntityBase
from project.plugin.log_tool import LogTool
from project.plugin.utils import Utils


class ListBase(object):
    def __init__(self):
        self.table_name = ""
        self.items = []
        self.sql = ""
        self.common_filed = ['id', 'del_flag', 'create_time', 'update_time', 'remark', 'create_user', 'update_user']
        self.tbl_filed = []

    def get_sheet(self):
        pass

    def get_type(self):
        return EntityBase

    def handle(self, excel):

        _sheet = excel.sheet_by_name(self.get_sheet())
        if not _sheet:
            LogTool.error(f"sheet页内容为空！")
            return False

        self.init_data(_sheet)

    def init_data(self, _sheet):
        self.sql = f"\n\n\n-----------------------------------\n-- {self.table_name}\n-----------------------------------\n\n"

        for r in range(_sheet.nrows):
            # 标题直接忽略
            if r < 1:
                continue
            row = _sheet.row_values(r)
            item = None

            for i in range(len(self.tbl_filed)):
                # 区Excel的值
                if len(row) <= i:
                    continue
                val = row[i]

                if i == 0:
                    if val == '' or int(val) > 0:
                        # 此行无效
                        break
                    else:
                        item = self.get_type()()

                # 取名
                filed_name = self.tbl_filed[i]
                if filed_name == "":
                    continue

                keys = filed_name.split('.')
                if len(keys) == 4:

                    key = keys[0]
                    # 转化val
                    new_val = Engine.dataAccess.get(keys[1], keys[2], val, keys[3])
                    if new_val is None:
                        LogTool.print(f"{self.get_sheet()}页{keys[0]}列{r}行中 找不到此项: {keys[1]}表{keys[2]}列中，无【{val}】")
                    val = new_val
                else:
                    key = filed_name

                # 赋值
                if hasattr(item, key):
                    setattr(item, key, val)
            pass

            if item is not None:
                self.sql = f"{self.sql}\n{self.get_sql(item, self.table_name)}"
                self.items.append(item)
        pass

        Utils.write_file(config.OutPath, self.sql)

        # 处理字段
        # self.tbl_filed = [ k.split('.')[0] for k in self.tbl_filed]



    def get_sql(self, item, table_name):
        filed = list(set([k.split('.')[0] for k in self.tbl_filed if k != ''] + self.common_filed))
        return item.get_sql(filed, table_name)


