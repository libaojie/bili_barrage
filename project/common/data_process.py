#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Comment    : 进度
@Time       : 2018/5/18 16:06
@Author     : libaojie
@File       : data_process.py
@Software   : PyCharm
"""

from project.common.modelbase import ModelBase
from project.common.read import Read
from project.plugin import check_data_tool
from project.plugin.log_tool import LogTool


class DataProcess(ModelBase):
    """
    数据处理进程
    """

    def __init__(self):
        pass

    def init(self):
        pass

    def destroy(self):
        pass

    _cmd_list = [
        (None, ''),
        # (Dict, '数据字典'),
        # (Session, '登录'),
        # (UserAdd, '增加用户'),
        # (ApplicationAdd, '增加应用'),
        # (RoleAdd, '增加角色'),
        # (UserRoleAdd, '用户角色关系'),
        # (ServiceAdd, '增加服务'),
        # (RoleServAdd, '角色服务关系'),
        # (MenuAdd, '增加菜单'),
        # (RoleMenuAdd, '角色菜单关系'),
        # (MenuServAdd, '菜单服务关系'),
    ]

    def run(self):
        """
        开始执行
        :return:
        """
        read = Read()
        read.run()

        # str_list = [f'\t{index} : {value[1]}' for index, value in enumerate(self._cmd_list)]
        # LogTool.print('命令列表：\n{0}'.format('\n'.join(str_list)))
        #
        # while True:
        #     cmd = input("请输入要执行的命令:")
        #     if cmd == 'exit':
        #         quit()
        #     cmd = self._change_cmd(cmd)
        #     if len(cmd) > 0:
        #         break
        #
        # for c in cmd:
        #     LogTool.print("执行命令：{0}".format(c))
        #     if c < len(self._cmd_list):
        #         LogTool.print("执行操作：{0}".format(self._cmd_list[c][1]))
        #         _f = self._cmd_list[c][0]
        #         if _f is not None:
        #             __factory = ModelFactory(_f)
        #             __factory.run()
        # pass

    def _change_cmd(self, cmd):
        """
        解析cmd
        :param cmd:
        :return:
        """
        _ret = []
        min_cmd = 0
        max_cmd = len(self._cmd_list) - 1
        if cmd is None or check_data_tool.is_null(cmd) or cmd == '0':
            # _ret = [4, 5, 6, 7, 8, 9, 10, 11]
            pass
        else:
            if ' ' in cmd:
                cmd = cmd.replace(' ', ',')

            if '-' in cmd:
                cmd_list = cmd.split('-')
                if len(cmd_list) == 2:
                    start = check_data_tool.change_to_int(cmd_list[0])
                    end = check_data_tool.change_to_int(cmd_list[1])
                    if not start or not end or start < min_cmd or start > max_cmd or end < min_cmd or end > max_cmd:
                        LogTool.print("输入有误：{0}-{1}".format(start, end))
                    else:
                        for i in range(start, end + 1):
                            _ret.append(i)
                else:
                    LogTool.print("输入有误：{0}".format(cmd))

            elif ',' in cmd:
                cmd_list = cmd.split(',')
                for c in cmd_list:
                    c_numb = check_data_tool.change_to_int(c)
                    if not c_numb or c_numb < min_cmd or c_numb > max_cmd:
                        LogTool.print("输入有误：{0}".format(c_numb))
                    else:
                        _ret.append(c_numb)
            else:
                c_numb = check_data_tool.change_to_int(cmd)
                if not c_numb or c_numb < min_cmd or c_numb > max_cmd:
                    LogTool.print("输入有误：{0}".format(c_numb))
                else:
                    _ret.append(c_numb)

        return _ret


class ModelFactory(object):
    """
    算法模型工厂
    """

    def __init__(self, factory=None):
        """
        初始化
        :param DataAccess dataAccess: 数据持久层
        :param object factory: 算法模型
        """
        self.__factory = factory()

    def run(self):
        """
        运行
        :return:
        """
        self.__factory.run()
