#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Comment    : 
@Time       : 2018/7/30 16:01
@Author     : libaojie
@File       : utils.py
@Software   : PyCharm
"""
import datetime
import os
import sys
import uuid

from project.plugin.log_tool import LogTool


class Utils(object):

    @staticmethod
    def get_path(path):
        """
        获取路径
        :return:
        """
        approot = os.path.dirname(os.path.abspath(sys.argv[0]))
        return os.path.abspath(os.path.join(approot, "../", path))

    @staticmethod
    def get_uuid():
        return uuid.uuid1().hex.upper()


    @staticmethod
    def get_currer_time(dateformat=None):
        """
        获取当前时间
        :param dateformat:
        :return:
        """
        # return time.strftime(dateformat, time.localtime(time.time()))
        return datetime.datetime.now()

    @staticmethod
    def write_file(path, content):
        #LogTool.print(path)
        if not os.path.isdir(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

        # if os.path.isfile(path):
        #     os.remove(path)

        # 创建并打开一个新文件
        with open(path, 'a', encoding='utf-8') as f:
            f.write(content)

    @staticmethod
    def clear_code(path):

        if os.path.isdir(path):
            ls = os.listdir(path)
            for i in ls:
                c_path = os.path.join(path, i)
                Utils.clear_code(c_path)
        elif os.path.isfile(path):
            os.remove(path)

        # path = os.path.abspath(path)
        # ls = os.listdir(path)
        # for i in ls:
        #     c_path = os.path.join(path, i)
        #     if os.path.isdir(c_path):
        #         Utils.clear_code(c_path)
        #     else:
        #         os.remove(c_path)

