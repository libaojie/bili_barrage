#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Comment    : 
@Time       : 2018/10/12 10:18
@Author     : libaojie
@File       : engine.py
@Software   : PyCharm
"""
from project.plugin.log_tool import LogTool


class Engine(object):
    """
    引擎
    """
    __instance = None  # 定义一个类属性做判断
    dataProcess = None
    dataAccess = None

    def __new__(cls):
        if cls.__instance is None:
            # 如果__instance为空证明是第一次创建实例
            # 通过父类的__new__(cls)创建实例
            cls.__instance == object.__new__(cls)
            return cls.__instance
        else:
            # 返回上一个对象的引用
            return cls.__instance

    @classmethod
    def init(cls):
        """
        初始化
        :param handle_id:
        :return:
        """
        LogTool.info("引擎初始化！")

        from project.common.data_process import DataProcess
        cls.dataProcess = DataProcess()
        cls.dataProcess.init()




    @classmethod
    def run(cls):
        """
        启动
        :return:
        """
        LogTool.info('引擎启动')

        cls.dataProcess.run()
        cls.destroy()

    @classmethod
    def destroy(cls):
        """
        销毁数据 先init者后destory
        :return:
        """
        # cls.dataProcess.destroy()
        pass

