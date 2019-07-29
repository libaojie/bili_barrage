#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Comment    : 装饰器
@Time       : 2018/5/18 16:06
@Author     : libaojie
@File       : data_process.py
@Software   : PyCharm
"""
import datetime as dt

from project.plugin.log_tool import LogTool


def log_fun(func):
    """
    获取执行函数名
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        LogTool.print('开始函数：【{0}】'.format(func.__name__))
        _stime = dt.datetime.now()
        _ret = func(*args, **kwargs)
        _etime = dt.datetime.now()
        LogTool.print('结束函数：【{0}】, 执行时间：【{1}】'.format(func.__name__, _etime - _stime))
        return _ret

    return wrapper


def get_run_numb(func):
    """
    给函数画标志位
    :param func:
    :return:
    """
    num = [0]

    def wrapper(*args, **kwargs):
        num[0] += 1
        print('--------------{0}执行次数【{1}】--------------'.format(
            func.__name__, num[0]))
        return func(*args, **kwargs)

    return wrapper
