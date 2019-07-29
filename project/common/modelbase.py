#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Comment    : 
@Time       : 2018/10/12 14:21
@Author     : libaojie
@File       : modelbase.py
@Software   : PyCharm
"""
from abc import abstractmethod, ABCMeta


class ModelBase(metaclass=ABCMeta):
    """
    基类
    """

    @abstractmethod
    def init(self):
        """
        初始化
        :return:
        """
        pass

    @abstractmethod
    def destroy(self):
        """
        销毁
        :return:
        """
        pass

    @abstractmethod
    def run(self):
        pass
