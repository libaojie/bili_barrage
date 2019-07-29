#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Comment    : 检测工具
@Time       : 2018/5/18 16:06
@Author     : libaojie
@File       : data_process.py
@Software   : PyCharm
"""

from project.plugin.log_tool import LogTool


# -----------------------------------------------------------------------------------------------
# 数据判断
# -----------------------------------------------------------------------------------------------
def is_null(val):
    '''
    检测不明类型是否为空
    :param val:
    :return:
    '''
    if val is None:
        return True

    if isinstance(val, str) and val.strip() == '':
        return True

    if isinstance(val, list) and len(val) == 0:
        return True

    return False


# -----------------------------------------------------------------------------------------------
# 数据转化
# -----------------------------------------------------------------------------------------------

def change_to_int(numb):
    """
    转化为int
    :param numb:
    :return:
    """
    _result = None

    if isinstance(numb, str) or isinstance(numb, float):
        try:
            _result = int(numb)
        except Exception as e:
            LogTool.error("{0}转int失败：{1}".format(type(numb), numb))
        finally:
            return _result

    return _result
