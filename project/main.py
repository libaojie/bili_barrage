#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Comment    : 主函数
@Time       : 2018/5/18 16:06
@Author     : libaojie
@File       : data_process.py
@Software   : PyCharm
"""
import os
import sys
import traceback

from project import config
from project.common.engine import Engine
from project.plugin.decorator import log_fun
from project.plugin.log_tool import LogTool
from project.plugin.utils import Utils

try:
    approot = os.path.dirname(os.path.abspath(__file__))
except NameError:
    approot = os.path.dirname(os.path.abspath(sys.argv[0]))

sys.path.append(os.path.split(approot)[0])


class App:
    """
    主程入口
    """

    def __init__(self):
        # 初始化日志模块
        LogTool.init(Utils.get_path(config.LogPath))
        Engine.init()
        pass

    @log_fun
    def run(self):
        Engine.run()


if __name__ == '__main__':
    try:
        app = App()
        app.run()
        # input('等待输入')
    except Exception as err:
        LogTool.error(traceback.format_exc())
