#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Comment    : 
@Time       : 2018/11/14 9:09
@Author     : libaojie
@File       : web_tool.py
@Software   : PyCharm
"""
import json

import requests

from project import config


class Web(object):

    @staticmethod
    def request_get(url, payload):
        val = None
        respone = requests.get(f"{config.BaseUrl}{url}", headers=config.Hearder, params=payload)
        if respone.status_code == 200:
            val = json.loads(respone.text)
        return val

    @staticmethod
    def request_post(url, payload):
        val = None
        respone = requests.post(f"{config.BaseUrl}{url}", headers=config.Hearder, json=payload)
        if respone.status_code == 200:
            val = json.loads(respone.text)
        return val
